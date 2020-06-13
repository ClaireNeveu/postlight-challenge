import React from 'react';
import { Link } from "react-router-dom";

import { photoUrl } from './util';

const EmployeeCard = (props: { employee: any }) => {
    const { employee } = props;
    return (
        <div className="component__employee-card">
            <img src={photoUrl(employee.photo_id)} />
            <h2><Link to={`/employee/${employee.id}`}>{employee.name}</Link></h2>
        </div>
    );
};

export default EmployeeCard;
