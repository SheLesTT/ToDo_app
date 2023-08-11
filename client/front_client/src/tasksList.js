const TasksList = ({tasks, }) => {




    return  (
        <div className="task_container">
        {tasks.map((task) => (

            <div className="task" key={task.id}>
                <h2> {task.name}</h2>
                <p>{task.content}</p>

            </div>

        ))}
    </div>
    )
}

export default TasksList