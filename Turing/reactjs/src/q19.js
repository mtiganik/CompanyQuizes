import React from 'react'

const Example = () => {
    const [count, setCount] = React.useState(0)
    const [email, setEmail] = React.useState("")

    React.useEffect(() => {
        console.log("Submission count", count);
    }, [count, email])
    return(
        <form>
            <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            />
            <button onClick={() => setCount(count +1)}>Submit</button>
        </form>
    )
}
export default Example