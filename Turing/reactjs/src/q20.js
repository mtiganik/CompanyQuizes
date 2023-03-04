import React from 'react'

function Q20(){
    let [count, setCount] =React.useState(0);
    React.useEffect(() => {
        let id = setInterval(() => {
            setCount(++count)
        },1000);
        return () => clearInterval(id);
    },[])
    return<h1>{count}</h1>
}

export default Q20