// React 16.x code below
import React from 'react';

// Create the Label React component here
const Label = ({value, color}) => {
    const styling = {
        color: color
    }

    return (
        <div style={styling}>
            {value}
        </div>
    )
}

const Label2 = ({value, color}) => {
    return (
        <div style={{color:color}}>
            {value}
        </div>
    )
}

// Modify this function if you want to change the preview
// It will not be evaluated as part of the assessment
export function Preview() {
    return <Label value={'Solution'} color={'blue'} />;
}

// Do not change
export default Label;