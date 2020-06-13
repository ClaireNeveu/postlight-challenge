import React from 'react';
import { Link } from "react-router-dom";

import EmployeeCard from './EmployeeCard';
import { photoUrl, WithQueryParams } from './util';

class EmployeeListing extends React.Component<WithQueryParams<{ 'page[after]': string | null }>, {}> {

    _dataFetch: any = null

    state: { employees: any | null, nextPage: string | null } = {
        employees: null,
        nextPage: null
    };

    // TODO move this to an API client
    async _loadEmployees() {
        const query = this.props.location?.query;
        const after = query ? query['page[after]'] : null;
        console.log('query', this.props);
        const response = (after
            ? await fetch(`http://localhost:4010/employees?page[after]=${after}`)
            : await fetch('http://localhost:4010/employees')
        );
        return response.json();
    }

    // TODO Add centralized state management instead of per-component
    componentDidMount() {
        this._dataFetch = this._loadEmployees().then(result => {
            this._dataFetch = null;
            this.setState({ employees: result.data, nextPage: result.links.next });
        });
    }

    componentWillUnmount() {
        if (this._dataFetch) {
            this._dataFetch.cancel();
        }
    }

    render() {
        const employees: Array<any> | null = this.state.employees;
        const nextPage = this.state.nextPage;
        if (employees === null) {
            return (
                <div className="App">
                    loading
                </div>
            );
        }
        return (
            <div className="app">
                {employees?.map(employee => <EmployeeCard employee={employee} />)}
                <div>{nextPage ? <Link to={`/?page[after]=${nextPage}`} >Next Page</Link> : 'End'}</div>
            </div>
        );
    }
}

export default EmployeeListing;