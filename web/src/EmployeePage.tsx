import React from 'react';

import { photoUrl, WithUrlParams } from './util';

class EmployeePage extends React.Component<WithUrlParams<{ id: string }>, {}> {

    _dataFetch: any = null

    state: { employees: Array<any> | null } = {
        employees: null,
    };

    // TODO Add centralized state management instead of per-component
    async _loadEmployee() {
        const employeeId = this.props.match.params.id;
        const response = await fetch(`http://localhost:4010/employee/${employeeId}`);
        return response.json();
    }

    componentDidMount() {
        this._dataFetch = this._loadEmployee().then(result => {
            this._dataFetch = null;
            this.setState({ employee: result.data });
        });
    }

    componentWillUnmount() {
        if (this._dataFetch) {
            this._dataFetch.cancel();
        }
    }

    render() {
        const employee: any | null = this.state.employees;
        if (employee === null) {
            return (
                <div className="App">
                    loading
                </div>
            );
        }
        return (
            <div className="component__employee-card">
                <img src={photoUrl(employee.photo_id)} />
                <h2>{employee.name}</h2>
            </div>
        );
    }
}

export default EmployeePage;