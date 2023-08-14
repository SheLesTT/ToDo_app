import React, {useRef, useState} from "react";
import Create from "./Create";
import Task from "./Task";
const TasksList = ({tasks, }) => {

    const[to_do, setToDo] = useState(tasks);

    const addTask = (task) =>{
        setToDo([...to_do, task]);
        console.log(to_do)
    }



    return  (
        <div>

        <div  className="task_container">
        {to_do.map((task) => (

            <Task key={task.id} id={task.id} name={task.name}/>

        ))}


    </div>
        <div>
            <Create onAddTask={addTask}/>
        </div>
        </div>
    )

}

export default TasksList