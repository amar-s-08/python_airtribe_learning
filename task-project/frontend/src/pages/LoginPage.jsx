import { useState } from "react";
import { usersApi } from "../api";
import { useAuth } from "../auth";

const emptyAccount = { username: "", email: "", password: "" };

export default function LoginPage() {
  const { signIn } = useAuth();
  const [username, setUsername] = useState("");
  const [account, setAccount] = useState(emptyAccount);
  const [creating, setCreating] = useState(false);
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);

  async function handleSignIn(event) {
    event.preventDefault();
    setBusy(true);
    setError("");
    try {
      const user = await usersApi.byUsername(username.trim());
      signIn(user);
    } catch (err) {
      setError(err.message);
    } finally {
      setBusy(false);
    }
  }

  async function handleCreate(event) {
    event.preventDefault();
    setBusy(true);
    setError("");
    try {
      const user = await usersApi.create(account);
      signIn(user);
    } catch (err) {
      setError(err.message);
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="login-wrap">
      <form className="login-card" onSubmit={creating ? handleCreate : handleSignIn}>
        <div>
          <h1>{creating ? "Create an account" : "Sign in"}</h1>
          <p className="muted">
            {creating
              ? "This saves a user with POST /api/users/."
              : "Looks up your account with GET /api/users/username/<username>/."}
          </p>
        </div>
        {error ? <div className="banner">{error}</div> : null}
        {creating ? (
          <>
            <label>
              Username
              <input
                value={account.username}
                onChange={(event) => setAccount({ ...account, username: event.target.value })}
                required
              />
            </label>
            <label>
              Email
              <input
                type="email"
                value={account.email}
                onChange={(event) => setAccount({ ...account, email: event.target.value })}
                required
              />
            </label>
            <label>
              Password
              <input
                type="password"
                value={account.password}
                onChange={(event) => setAccount({ ...account, password: event.target.value })}
                required
              />
            </label>
          </>
        ) : (
          <label>
            Username
            <input value={username} onChange={(event) => setUsername(event.target.value)} required />
          </label>
        )}
        <button className="btn" type="submit" disabled={busy}>
          {busy ? "Working..." : creating ? "Create account" : "Sign in"}
        </button>
        <button
          className="btn ghost"
          type="button"
          onClick={() => {
            setCreating((value) => !value);
            setError("");
          }}
        >
          {creating ? "I already have an account" : "Need an account?"}
        </button>
      </form>
    </div>
  );
}
