import {useState, useEffect} from "react";
import TasksList from "./tasksList";
import UseFetch from "./useFetch";
import Create from "./Create";

const Home = () => {
    const {data :tasks, error, isPending} = UseFetch('http://localhost:8000/tasks');
    console.log(tasks)
    // const HandleClick = (name) =>{
    //     name = setName(name)
    // }
    // const handleDelete = (id) =>{
    //     const newTasks = tasks.filter(blog => blog.id !== id);
    //     setTasks(newTasks);
    // }

    return (
        <div>
            {error && <div>{error}</div>}
            {isPending && <div>Loading.iiii..</div>}
            {tasks && <TasksList tasks={tasks} />}

            {/*<div><Create/></div>*/}
        </div>

    );
}

export default Home