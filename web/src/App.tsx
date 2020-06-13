import React from 'react';
import logo from './logo.svg';
import './App.css';

class App extends React.Component {

    _dataFetch: any = null

    state = {
        employees: null,
    };

    // TODO move to separate API handler
    async _loadEmployees() {
        let response = await fetch('http://localhost:4010/employees');
        return response.json();
    }

    componentWillMount() {
        this._dataFetch = this._loadEmployees().then(employees => {
            this._dataFetch = null;
            this.setState({employees});
        });
    }

    componentWillUnmount() {
        if (this._dataFetch) {
            this._dataFetch.cancel();
        }
    }

    render() {
        return (
            <div className="App">
              <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>
                  Edit <code>src/App.tsx</code> and save to reload.
                </p>
                <a
                  className="App-link"
                  href="https://reactjs.org"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  Learn React
                </a>
              </header>
            </div>
        );
    }
}

export default App;
