
DROP TABLE IF EXISTS department;
CREATE TABLE department (
  id serial,
  name text,
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS job;
CREATE TABLE job (
  id serial,
  name text,
  description text,
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS employee;
CREATE TABLE employee (
  id serial,
  name text, -- Not everybody has a first/last name pattern, single name field is better
  photo_id integer,
  job integer REFERENCES job(id),
  department integer REFERENCES department(id),
  location text, -- Could probably structure this more
  PRIMARY KEY (id)
);
