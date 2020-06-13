import db
from app import run_app

print('Setting up Database')

db._metadata.drop_all(db._engine)
db._metadata.create_all(db._engine)

print('Importing test data')
engineers = [
    'Alice',
    'Anna Fisher',
    'Adrienne Phelps',
    'Hillary Landry',
    'Israel Wade',
    'Norah Peck',
    'Eve Colon',
    'Emerson Riley',
    'Wayne Obrien'
]
pms = [
    'Bob',
    'Livia Travis',
    'Yaritza Walter',
    'Pierre Stokes',
    'Roland Vincent',
    'Brooklynn Gray',
    'Emerson Logan',
    'Mallory Frederick',
    'Gregory Bass',
]


db.executeVoid(db.department.insert().values(name='Engineering'))
db.executeVoid(db.department.insert().values(name='Product'))
db.executeVoid(db.job.insert().values(name='L3 Engineer', description='mid-level engineer'))
db.executeVoid(db.job.insert().values(name='L2 Product Manager', description='beginner PM'))
for name in engineers:
    db.executeVoid(db.employee.insert().values(
        name=name,
        photo_id=895430,
        job=1,
        department=1,
        location='New York'
    ))
for name in pms:
    db.executeVoid(db.employee.insert().values(
        name=name,
        photo_id=8765541,
        job=2,
        department=2,
        location='New York'
    ))

print('Running')

run_app()
