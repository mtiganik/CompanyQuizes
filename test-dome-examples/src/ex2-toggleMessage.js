import React from 'react';

// Replace class with function!!

function Message() {
    const [hidden, setHidden] = React.useState(true)

      return (<React.Fragment>
            <a href="#" onClick={() => setHidden(!hidden)}>Want to buy a new car?</a>
            <p hidden={hidden}>Call +11 22 33 44 now!</p>
          </React.Fragment>);
  }
  
export default Message