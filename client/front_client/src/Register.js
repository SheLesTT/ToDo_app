import {UserContext} from "./UserContext";
import {useState} from "react";
import {useContext} from "react";
import ErrorMessage from "./ErrorMessage";



const Register = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [conformPassword, setConfirmPassword] = useState("");
    const [error, setError] = useState(null);
    const [, setToken] = useContext(UserContext);

    const submitRegistration = async () => {
        const requestOptions = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({email, password})

        }
            const response = await fetch("http://127.0.0.1:8000/users", requestOptions);
            const data = await response.json();
            console.log(data.access_token + "token")
            if(
        !response.ok
        )
            {
                setError(data.detail);
            }
        else
            {
                setToken(data.access_token);
            }
    }
    const handleSubmit = (e) => {
            e.preventDefault();
            if (password === conformPassword && password.length >=4){
                submitRegistration()

            }
            else{
                setError("Ensure the passwords are the same and are at least 4 characters")
            }
        }
    return (
        <div className="column">
            <form onSubmit={handleSubmit} className="box">
                <h1 className="title has-text_centred">Register</h1>
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
                <div className="field">
                    <label className="label">Confirm password</label>
                    <div className="control">
                        <input type="password"
                               placeholder="Enter password"
                               value={conformPassword}
                               onChange={(e) => setConfirmPassword(e.target.value)}
                               className="input"
                               required
                        />
                    </div>
                </div>
                <ErrorMessage message={error}/>
                <br/>
                <button className="button is-primary" type="submit">Register</button>
            </form>
        </div>
    )
}

    export default Register
