import React from 'react'

class Username extends React.Component {
  
    state = { value: "" };
  
    changeValue(value) {
      this.setState({ value });
    }
  
    render() {
      const { value } = this.state;
      return <h1>{value}</h1>;
    }
  }
  
  function Apps() {
    const [text, setText] = React.useState("r")
    const val = React.useRef("Hello")

    function clickHandler() {
      //console.log(text)
      val.current = text
      Username.setState({val})
      //console.log(param)
    }
  
    return (
      <div>
        <button onClick={clickHandler}>Change Username</button>
        <input type="text" value={text} onChange={(e) => setText(e.target.value)}/>
        <Username ref={Username => {window.Username = Username}}/>
      </div>
    );
  }
  
  export default Apps