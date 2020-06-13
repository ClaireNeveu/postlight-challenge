import React from 'react';

import EmployeeCard from './EmployeeCard';
import { photoUrl } from './util';

const EmployeeListing = (props: { employees: Array<any> | null }) => {
    const { employees } = props;
    return (
        <div className="app">
            {employees?.map(employee => <EmployeeCard employee={employee} />)}
        </div>
    );
};

export default EmployeeListing;