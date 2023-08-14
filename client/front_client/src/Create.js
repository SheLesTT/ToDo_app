import {useState} from "react";
import {useEffect} from "react";
import {useRef} from "react";

const Create = ({onAddTask}) => {

    const[name, setTitle] = useState("");
    const[content, setContent] = useState("");
    useEffect(()=>{
        document.addEventListener("keydown",detectKeyDown,true)
            return () => {
      document.removeEventListener("keydown", detectKeyDown, true);
    };
    },)


    const detectKeyDown = (e)=>{
        if(e.key==="Enter"){
            e.preventDefault()
            handleSubmit()
        }

    }
    const handleSubmit = () =>{
        // e.preventDefault();
        const task = {name, content}
        console.log(JSON.stringify(task))
        onAddTask(task)
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
            <form onSubmit={(e)=> handleSubmit(e)}>
                <label>Task title:</label>
                <input
                type="text"
                required
                value ={name}
                onChange={(e) => setTitle(e.target.value)}
                className="new_task_field"/>

            </form>

        </div>
    )
}
export default Create