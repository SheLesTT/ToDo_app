import {useEffect, useState} from "react";

const useFetch = (url) => {

    const [data, setData] = useState(null)
    const [isPending, setIsPending] = useState(true)
    const [error, setError] = useState(null)
    useEffect(()=>{
        fetch(url)
            .then(res =>{
                console.log(res)
                if(!res.ok){
                    throw new Error('Could not fetch data from server')
                }

                return res.json()
            })
            .then((data) => {
                setData(data)
                setIsPending(false)
                setError(null)
            })
            .catch(err => {
                setError(err.message)
                setIsPending(false)
            })
        console.log(data)
    },[])

    return {
        data,
        isPending,
        error
    }
}

export default useFetch;