import React from 'react';


// React is loaded and is available as React and ReactDOM
// imports should NOT be used
const CommentList = (props) => {

const [currentVal, setCurrentVal] = React.useState("");
const [valuesList, setValuesList] = React.useState([])

function handleClick(){
    if(currentVal !== "" && currentVal !== null){
        setValuesList([...valuesList, currentVal]);
        setCurrentVal("")
    }

}
    return (<div>
        <form>
          <input type="text" onChange={(event) => setCurrentVal(event.target.value)} value = {currentVal}/>
          <input type="button" value="Post" onClick={handleClick}/>
        </form>
        <ul>
            {
                valuesList.map((item,i) =>
                
                    // {console.log(item)}
                    <li key={i}>{item}</li>
                )
            }
        </ul>
      </div>);
  }
  

  export default CommentList;

  