import React, {useState, useEffect} from 'react';
import Textfield from "./textfield";
import Home from "./Home";
// import './App.css'


function App() {
    const [data, setData] = useState('');

    useEffect(() => {
        // Fetch data from the FastAPI backend
        fetch('http://localhost:8000/tasks/6').then(
            res => res.json()
        ).then(
            data => {
                setData(data)
                // console.log(data)
            }
        )
    }, []);

    return (
        <div className="content">
            <Home/>
            {(typeof data.content === 'undefined') ? (
                <p>Loading.iiii..</p>
            ) : (
                <div>
                <p>{data.id}</p>
                <p>{data.content}</p>
                <p>{data.name}</p>
                </div>

            )}
            <div>
                <h1>Text Field Example</h1>
                <Textfield />
            </div>

        </div>
    );
}

export default App;