import { useEffect, useState } from "react";
import { formatWhen, usersApi } from "../api";
import { useAuth } from "../auth";

const emptyUser = { username: "", email: "", password: "" };

export default function UsersPage() {
  const { user: currentUser, signIn } = useAuth();
  const [people, setPeople] = useState([]);
  const [form, setForm] = useState(emptyUser);
  const [editingId, setEditingId] = useState(null);
  const [lookup, setLookup] = useState("");
  const [selected, setSelected] = useState(null);
  const [assigned, setAssigned] = useState([]);
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);

  async function loadPeople() {
    const rows = await usersApi.list();
    setPeople(rows);
    return rows;
  }

  async function showTasks(person) {
    setSelected(person);
    setAssigned(await usersApi.tasks(person.id));
  }

  useEffect(() => {
    loadPeople().catch((err) => setError(err.message));
  }, []);

  function startEdit(person) {
    setEditingId(person.id);
    setForm({
      username: person.username,
      email: person.email,
      password: person.password || "",
    });
  }

  async function handleSubmit(event) {
    event.preventDefault();
    setBusy(true);
    setError("");
    try {
      if (editingId) {
        const updated = await usersApi.update(editingId, form);
        if (updated.id === currentUser.id) signIn(updated);
      } else {
        await usersApi.create(form);
      }
      setForm(emptyUser);
      setEditingId(null);
      await loadPeople();
    } catch (err) {
      setError(err.message);
    } finally {
      setBusy(false);
    }
  }

  async function remove(person) {
    if (!window.confirm(`Delete ${person.username}? Their tasks will be removed too.`)) return;
    setError("");
    try {
      await usersApi.remove(person.id);
      if (selected?.id === person.id) {
        setSelected(null);
        setAssigned([]);
      }
      await loadPeople();
    } catch (err) {
      setError(err.message);
    }
  }

  async function findByUsername(event) {
    event.preventDefault();
    setError("");
    try {
      const person = await usersApi.byUsername(lookup.trim());
      await showTasks(person);
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <section>
      <div className="page-head">
        <div>
          <h1>People</h1>
          <p className="muted">Create, update, and look up users. Select someone to see their tasks.</p>
        </div>
      </div>
      {error ? <div className="banner">{error}</div> : null}
      <div className="layout">
        <form className="card stack" onSubmit={handleSubmit}>
          <strong>{editingId ? "Edit person" : "New person"}</strong>
          <label>
            Username
            <input
              value={form.username}
              onChange={(event) => setForm({ ...form, username: event.target.value })}
              required
            />
          </label>
          <label>
            Email
            <input
              type="email"
              value={form.email}
              onChange={(event) => setForm({ ...form, email: event.target.value })}
              required
            />
          </label>
          <label>
            Password
            <input
              type="password"
              value={form.password}
              onChange={(event) => setForm({ ...form, password: event.target.value })}
              required
            />
          </label>
          <div className="actions">
            <button className="btn" type="submit" disabled={busy}>
              {busy ? "Saving..." : editingId ? "Save person" : "Add person"}
            </button>
            {editingId ? (
              <button
                className="btn ghost"
                type="button"
                onClick={() => {
                  setEditingId(null);
                  setForm(emptyUser);
                }}
              >
                Cancel
              </button>
            ) : null}
          </div>
        </form>
        <div className="stack">
          <form className="card row" onSubmit={findByUsername}>
            <label style={{ flex: 1 }}>
              Find by username
              <input value={lookup} onChange={(event) => setLookup(event.target.value)} required />
            </label>
            <button className="btn" type="submit">
              Find
            </button>
          </form>
          <div className="card table-wrap">
            <table>
              <thead>
                <tr>
                  <th>Username</th>
                  <th>Email</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                {people.map((person) => (
                  <tr
                    key={person.id}
                    className={selected?.id === person.id ? "selected clickable" : "clickable"}
                    onClick={() => showTasks(person).catch((err) => setError(err.message))}
                  >
                    <td>{person.username}</td>
                    <td>{person.email}</td>
                    <td>
                      <div className="actions">
                        <button
                          className="btn ghost"
                          type="button"
                          onClick={(event) => {
                            event.stopPropagation();
                            startEdit(person);
                          }}
                        >
                          Edit
                        </button>
                        <button
                          className="btn danger"
                          type="button"
                          onClick={(event) => {
                            event.stopPropagation();
                            remove(person);
                          }}
                          disabled={person.id === currentUser.id}
                        >
                          Delete
                        </button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <div className="card stack">
            <strong>{selected ? `Tasks for ${selected.username}` : "Assigned tasks"}</strong>
            {selected && assigned.length === 0 ? <p className="muted">No tasks assigned.</p> : null}
            {!selected ? <p className="muted">Select a person to load GET /api/users/&lt;id&gt;/tasks/.</p> : null}
            {assigned.map((task) => (
              <div key={task.id}>
                <strong>{task.completed ? "Done" : "Open"} · {task.title}</strong>
                <div className="meta">{formatWhen(task.due_date)}</div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
