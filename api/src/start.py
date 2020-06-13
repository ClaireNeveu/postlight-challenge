import db
from app import run_app

print('Setting up Database')

db._metadata.create_all(db._engine)

print('Importing test data')
db.executeVoid(db.department.insert().values(name='Engineering'))
db.executeVoid(db.department.insert().values(name='Product'))
db.executeVoid(db.job.insert().values(name='L3 Engineer', description='mid-level engineer'))
db.executeVoid(db.job.insert().values(name='L2 Product Manager', description='beginner PM'))
db.executeVoid(db.employee.insert().values(
    name='Alice',
    photo_id=895430,
    job=1,
    department=1,
    location='New York'
))
db.executeVoid(db.employee.insert().values(
    name='Bob',
    photo_id=8765541,
    job=2,
    department=2,
    location='New York'
))

print('Running')

run_app()
