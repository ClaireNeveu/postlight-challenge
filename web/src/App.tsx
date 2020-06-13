import React from 'react';
import './App.css';

import {
    BrowserRouter as Router,
    Switch,
    Route,
} from "react-router-dom";

import EmployeeListing from './EmployeeListing';
import EmployeePage from './EmployeePage';

class App extends React.Component {

    render() {
        return (
            <Router>
                <Switch>
                    <Route path="/employee/:id" component={EmployeePage} />
                    <Route path="/" component={EmployeeListing} />
                </Switch>
            </Router>
        );
    }
}

export default App;
