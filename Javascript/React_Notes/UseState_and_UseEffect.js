import { useEffect, useState } from "react"

const MyComponent = () => {
    const [variable, setVariable] = useState(0);

    useEffect(() => {
        console.log(variable)
    }, []) // The Array at the end dictates how many times this is ran in a sense, giving this an empty array has it run once or twice then stop, whereas no array has it run continuously over and over again.
}