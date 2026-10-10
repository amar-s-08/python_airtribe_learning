import { useEffect, useMemo, useState } from "react";
import { formatWhen, fromDateInput, tasksApi, toDateInput, usersApi } from "../api";
import { useAuth } from "../auth";

const emptyForm = {
  title: "",
  description: "",
  due_date: "",
  completed: false,
  user: "",
};

export default function TasksPage({ mode }) {
  const { user } = useAuth();
  const [tasks, setTasks] = useState([]);
  const [people, setPeople] = useState([]);
  const [form, setForm] = useState(emptyForm);
  const [editingId, setEditingId] = useState(null);
  const [filter, setFilter] = useState("open");
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);

  const mine = mode === "mine";

  async function load() {
    setError("");
    try {
      const [taskRows, userRows] = await Promise.all([
        mine ? usersApi.tasks(user.id) : tasksApi.list(),
        usersApi.list(),
      ]);
      setTasks(taskRows);
      setPeople(userRows);
    } catch (err) {
      setError(err.message);
    }
  }

  useEffect(() => {
    load();
  }, [mode, user.id]);

  const visible = useMemo(() => {
    return tasks.filter((task) => {
      if (filter === "open") return !task.completed;
      if (filter === "done") return task.completed;
      return true;
    });
  }, [tasks, filter]);

  function startEdit(task) {
    setEditingId(task.id);
    setForm({
      title: task.title,
      description: task.description,
      due_date: toDateInput(task.due_date),
      completed: task.completed,
      user: String(task.user),
    });
  }

  function resetForm() {
    setEditingId(null);
    setForm(emptyForm);
  }

  async function handleSubmit(event) {
    event.preventDefault();
    setBusy(true);
    setError("");
    const payload = {
      user: Number(mine ? user.id : form.user),
      title: form.title.trim(),
      description: form.description.trim(),
      completed: form.completed,
      due_date: fromDateInput(form.due_date),
    };
    try {
      if (editingId) {
        await tasksApi.update(editingId, payload);
      } else {
        await tasksApi.create(payload);
      }
      resetForm();
      await load();
    } catch (err) {
      setError(err.message);
    } finally {
      setBusy(false);
    }
  }

  async function toggle(task) {
    setError("");
    try {
      await tasksApi.patch(task.id, { completed: !task.completed });
      await load();
    } catch (err) {
      setError(err.message);
    }
  }

  async function remove(task) {
    if (!window.confirm(`Delete "${task.title}"?`)) return;
    setError("");
    try {
      await tasksApi.remove(task.id);
      if (editingId === task.id) resetForm();
      await load();
    } catch (err) {
      setError(err.message);
    }
  }

  const ownerName = (userId) => people.find((person) => person.id === userId)?.username || `User ${userId}`;

  return (
    <section>
      <div className="page-head">
        <div>
          <h1>{mine ? "My tasks" : "All tasks"}</h1>
          <p className="muted">
            {mine
              ? `Loaded with GET /api/users/${user.id}/tasks/.`
              : "Loaded with GET /api/tasks/."}
          </p>
        </div>
      </div>
      {error ? <div className="banner">{error}</div> : null}
      <div className="layout">
        <form className="card stack" onSubmit={handleSubmit}>
          <strong>{editingId ? "Edit task" : "New task"}</strong>
          {!mine ? (
            <label>
              Assigned to
              <select
                value={form.user}
                onChange={(event) => setForm({ ...form, user: event.target.value })}
                required
              >
                <option value="">Choose a person</option>
                {people.map((person) => (
                  <option key={person.id} value={person.id}>
                    {person.username}
                  </option>
                ))}
              </select>
            </label>
          ) : null}
          <label>
            Title
            <input
              value={form.title}
              onChange={(event) => setForm({ ...form, title: event.target.value })}
              required
            />
          </label>
          <label>
            Description
            <textarea
              value={form.description}
              onChange={(event) => setForm({ ...form, description: event.target.value })}
              required
            />
          </label>
          <label>
            Due
            <input
              type="datetime-local"
              value={form.due_date}
              onChange={(event) => setForm({ ...form, due_date: event.target.value })}
            />
          </label>
          <label className="checkbox-line">
            <input
              type="checkbox"
              checked={form.completed}
              onChange={(event) => setForm({ ...form, completed: event.target.checked })}
            />
            Completed
          </label>
          <div className="actions">
            <button className="btn" type="submit" disabled={busy}>
              {busy ? "Saving..." : editingId ? "Save changes" : "Add task"}
            </button>
            {editingId ? (
              <button className="btn ghost" type="button" onClick={resetForm}>
                Cancel
              </button>
            ) : null}
          </div>
        </form>
        <div>
          <div className="filters">
            {[
              ["open", "Open"],
              ["done", "Done"],
              ["all", "All"],
            ].map(([value, label]) => (
              <button
                key={value}
                type="button"
                className={filter === value ? "active" : ""}
                onClick={() => setFilter(value)}
              >
                {label}
              </button>
            ))}
          </div>
          <div className="task-list">
            {visible.length === 0 ? <div className="empty">No tasks in this view.</div> : null}
            {visible.map((task) => (
              <article key={task.id} className={task.completed ? "task done" : "task"}>
                <input
                  className="check"
                  type="checkbox"
                  checked={task.completed}
                  onChange={() => toggle(task)}
                  aria-label={`Mark ${task.title} ${task.completed ? "open" : "complete"}`}
                />
                <div className="stack">
                  <div>
                    <h3>{task.title}</h3>
                    <p>{task.description}</p>
                    <p className="meta">
                      {formatWhen(task.due_date)}
                      {mine ? "" : ` · ${ownerName(task.user)}`}
                    </p>
                  </div>
                  <div className="actions">
                    <button className="btn ghost" type="button" onClick={() => startEdit(task)}>
                      Edit
                    </button>
                    <button className="btn danger" type="button" onClick={() => remove(task)}>
                      Delete
                    </button>
                  </div>
                </div>
              </article>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
