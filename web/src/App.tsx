import React from 'react';
import './App.css';

import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from "react-router-dom";

import EmployeeListing from './EmployeeListing';
import EmployeePage from './EmployeePage';

class App extends React.Component {

    _dataFetch: any = null

    state: { employees: Array<any> | null } = {
        employees: null,
    };

    // TODO move to separate API handler
    async _loadEmployees() {
        const response = await fetch('http://localhost:4010/employees');
        return response.json();
    }

    componentDidMount() {
        this._dataFetch = this._loadEmployees().then(result => {
            this._dataFetch = null;
            this.setState({ employees: result.data });
        });
    }

    componentWillUnmount() {
        if (this._dataFetch) {
            this._dataFetch.cancel();
        }
    }

    render() {
        const employees: Array<any> | null = this.state.employees;
        console.log(employees);
        // TODO make a higher-level component that handles loading
        if (employees === null) {
            return (
                <div className="App">
                    loading
                </div>
            );
        }
        return (
            <Router>
                <Switch>
                    <Route path="/employee/:id" component={EmployeePage} />
                    <Route path="/"><EmployeeListing employees={employees} /></Route>
                </Switch>
            </Router>
        );
    }
}

export default App;
