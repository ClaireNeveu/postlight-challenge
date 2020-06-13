import React from 'react';

import { photoUrl } from './util';

const EmployeeListing = (props: { employees: Array<any> | null }) => {
    const { employees } = props;
    return (
        <div className="app">
            {employees?.map(employee => {
                return (
                    <div className="component__employee-card">
                        <img src={photoUrl(employee.photo_id)} />
                        <h2>{employee.name}</h2>
                    </div>
                );
            })}
        </div>
    );
};

export default EmployeeListing;