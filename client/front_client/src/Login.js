import {useContext, useState} from "react";
import {UserContext} from "./UserContext";
import ErrorMessage from "./ErrorMessage";



const Login = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState(null);
    const [, setToken] = useContext(UserContext);

    const submitLogin = async () => {
        const requestOptions = {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: JSON.stringify(`grant_type=&username=${email}&password=${password}&client_id=&client_secret=`)
        }
        const response = await fetch("http://127.0.0.1:8000/login", requestOptions);
        const data = await response.json();
        if (!response.ok) {
            setError(data.detail);
        } else {
            setToken(data.access_token);
        }
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        submitLogin();
    }
    return (
        <div className="column">
            <form onSubmit={handleSubmit} className="box">
                <h1 className="title has-text_centred">Login</h1>
                <div className="field">
                    <label className="label">Email Adress</label>
                    <div className="control">
                        <input type="email"
                               placeholder="Enter email"
                               value={email}
                               onChange={(e) => setEmail(e.target.value)}
                               className="input"
                               required
                        />
                    </div>
                </div>
                <div className="field">
                    <label className="label">Password</label>
                    <div className="control">
                        <input type="password"
                               placeholder="Enter password"
                               value={password}
                               onChange={(e) => setPassword(e.target.value)}
                               className="input"
                               required
                        />
                    </div>
                </div>

                <ErrorMessage message={error}/>
                <br/>
                <button className="button is-primary" type="submit">Login</button>
            </form>
        </div>

    )
}
export default Login