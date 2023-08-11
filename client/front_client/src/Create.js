import {useState} from "react";

const Create = () => {

    const[name, setTitle] = useState("");
    const[content, setContent] = useState("");
    const handleSubmit = (e) =>{
        e.preventDefault();
        const task = {name, content}
        console.log(JSON.stringify(task))
        fetch("http://localhost:8000/tasks", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(task)
        }).then(()=>
        console.log("task added"))
    }
    return (
        <div>
            <h2>Add new task</h2>
            <form onSubmit={(e)=>handleSubmit(e)}>
                <label>Task title:</label>
                <input
                type="text"
                required
                value ={name}
                onChange={(e) => setTitle(e.target.value)}
                />
                <label>Task content:</label>
                <textarea required
                value={content}
                onChange={(e) => setContent(e.target.value)}></textarea>
                <button>Add task</button>
            </form>

        </div>
    )
}
export default Create