import React from 'react'

function Example(){
    const [test,settest] = React.useState("Hello")

    return(
        <div>{test}</div>
    )
}

export default Example