import React, { useState } from 'react';
import { BeatLoader } from 'react-spinners';
import './index.css';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

// process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";

function App() {
  const [inputValue, setInputValue] = useState('');
  const [response, setResponse] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsLoading(true);
    const response = await fetch('http://localhost:8000/api/endpoint', {
      method: 'POST',
      body: JSON.stringify({ input: inputValue }),
      headers: { 'Content-Type': 'application/json' }
    });
    const responseData = await response.json();
    setResponse(responseData);
    setIsLoading(false);
  };

  return (
    <Router>
      <Switch>
        <Route exact path="/">
          <div className="container">
            <form onSubmit={handleSubmit}>
              <div className="input-container">
                <input
                  type="text"
                  id="inputField"
                  placeholder="What's on your mind?"
                  value={inputValue}
                  onChange={(event) => setInputValue(event.target.value)}
                />
                <button type="submit">Submit</button>
              </div>
            </form>
            {isLoading && (
              <div className="loader">
                <BeatLoader size={15} color={'#36D7B7'} loading={isLoading} />
              </div>
            )}
            {response && (
              <div className="response">
                <p>Bhagwad Gita:</p>
                <p>{response.message}</p>
              </div>
            )}
          </div>
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
