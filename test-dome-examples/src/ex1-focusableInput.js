import React from 'react';

const FocusableInput = (props) => {
    const inputRef = React.useRef();
    React.useEffect(() => {
      if(props.shouldFocus){
        inputRef.current.focus()
      }
    })
    return (
      <form>
        <input  ref = {inputRef}/>
      </form>
    );
  };
  
export default FocusableInput