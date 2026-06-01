import { useState } from "react"

const Child = ({value, onChange}) => {
    const handleChildChange = (event) => {
        onChange(event.input.value)
    }

    return (
        <input onChange={handleChildChange}>
            {value}
        </input>
    )
}

const Parent = () => {
    const [value, setValue] = useState('');

    // Ensure Methods are created in Parent if changes in both are wanted.
    const handleChildChange = (newValue) => {
        setValue(newValue)
    }

    return (
        <div>
            <p id='parentValue'>{value}</p>
            <Child value={value} onChange={handleChildChange}/>
        </div>
    )
}


export default Parent;