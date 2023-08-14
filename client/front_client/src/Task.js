const Task = ({id,name}) => {

    return(

        <div className="task" key={id}>

            <div className="checkbox_container">
                <label className="round-checkbox">
                    <input type ="checkbox"/>
                    <span className="checkbox_custom"></span>
                </label>
            </div>

            <p className="task_title"> {name}</p>

        </div>
    )


}

export default Task