function formatError(data, status) {
  if (!data) return `Request failed (${status})`;
  if (typeof data === "string") return data;
  if (data.error) return String(data.error);
  if (data.detail) return String(data.detail);
  const parts = Object.entries(data).map(([key, value]) => {
    const message = Array.isArray(value) ? value.join(" ") : String(value);
    return `${key}: ${message}`;
  });
  return parts.join(" ") || `Request failed (${status})`;
}

export async function api(path, { method = "GET", body } = {}) {
  const response = await fetch(`/api${path}`, {
    method,
    headers: body === undefined ? undefined : { "Content-Type": "application/json" },
    body: body === undefined ? undefined : JSON.stringify(body),
  });

  if (response.status === 204) return null;

  const text = await response.text();
  let data = null;
  if (text) {
    try {
      data = JSON.parse(text);
    } catch {
      data = text;
    }
  }

  if (!response.ok) {
    throw new Error(formatError(data, response.status));
  }
  return data;
}

export const usersApi = {
  list: () => api("/users/"),
  create: (body) => api("/users/", { method: "POST", body }),
  update: (id, body) => api(`/users/${id}/`, { method: "PUT", body }),
  remove: (id) => api(`/users/${id}/`, { method: "DELETE" }),
  byUsername: (username) => api(`/users/username/${encodeURIComponent(username)}/`),
  tasks: (id) => api(`/users/${id}/tasks/`),
};

export const tasksApi = {
  list: () => api("/tasks/"),
  create: (body) => api("/tasks/", { method: "POST", body }),
  update: (id, body) => api(`/tasks/${id}/`, { method: "PUT", body }),
  patch: (id, body) => api(`/tasks/${id}/`, { method: "PATCH", body }),
  remove: (id) => api(`/tasks/${id}/`, { method: "DELETE" }),
};

export function toDateInput(value) {
  if (!value) return "";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return "";
  const pad = (part) => String(part).padStart(2, "0");
  return `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())}T${pad(date.getHours())}:${pad(date.getMinutes())}`;
}

export function fromDateInput(value) {
  if (!value) return null;
  return new Date(value).toISOString();
}

export function formatWhen(value) {
  if (!value) return "No due date";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;
  return date.toLocaleString(undefined, {
    month: "short",
    day: "numeric",
    hour: "numeric",
    minute: "2-digit",
  });
}
