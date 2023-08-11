import React, { useRef } from "react";
import UpdateList from "./UpdateList";
const TasksList = ({tasks, }) => {




    return  (
        <div  className="task_container">
        {tasks.map((task) => (

            <div className="task" key={task.id}>

                <div className="checkbox_container">
                    <label className="round-checkbox">
                         <input type ="checkbox"/>
                         <span className="checkbox_custom"></span>
                    </label>
                </div>

                <p className="task_title"> {task.name}</p>

            </div>

        ))}
    </div>
    )
}

export default TasksList