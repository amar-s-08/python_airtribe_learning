import { NavLink, Navigate, Route, Routes } from "react-router-dom";
import { useAuth } from "./auth";
import LoginPage from "./pages/LoginPage";
import TasksPage from "./pages/TasksPage";
import UsersPage from "./pages/UsersPage";

function Shell() {
  const { user, signOut } = useAuth();

  return (
    <div className="shell">
      <aside className="sidebar">
        <div className="brand">
          <strong>Taskboard</strong>
          <span>Work assigned to people</span>
        </div>
        <nav className="nav">
          <NavLink to="/tasks" end>
            My tasks
          </NavLink>
          <NavLink to="/tasks/all">All tasks</NavLink>
          <NavLink to="/people">People</NavLink>
        </nav>
        <div className="sidebar-user">
          <div>
            Signed in as <strong>{user.username}</strong>
          </div>
          <button className="btn secondary" type="button" onClick={signOut}>
            Sign out
          </button>
        </div>
      </aside>
      <main className="main">
        <Routes>
          <Route path="/tasks" element={<TasksPage mode="mine" />} />
          <Route path="/tasks/all" element={<TasksPage mode="all" />} />
          <Route path="/people" element={<UsersPage />} />
          <Route path="*" element={<Navigate to="/tasks" replace />} />
        </Routes>
      </main>
    </div>
  );
}

export default function App() {
  const { user } = useAuth();

  return (
    <Routes>
      <Route path="/login" element={user ? <Navigate to="/tasks" replace /> : <LoginPage />} />
      <Route path="/*" element={user ? <Shell /> : <Navigate to="/login" replace />} />
    </Routes>
  );
}
