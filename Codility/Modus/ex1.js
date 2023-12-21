import React from "react"

export default function LoginForm({ onSubmit }) {
    const [username, setUserame] = React.useState("");
    const [password, setPassword] = React.useState("");

    const handleSubmit = (event) => {
        event.preventDefault();
        onSubmit(username, password);
        }
    const submitEnabled = username.length > 0 && password.length > 0 

    return (<div>
        <input type="text" id="username-input" onChange={(event) => setUserame(event.target.value)} value = {username} />
        <input type="password" id="password-input" onChange={(event) => setPassword(event.target.value)} value = {password} />
        <input type="submit" id="login-button" disabled={!submitEnabled} onClick={handleSubmit}></input>
    </div>);
  }
  