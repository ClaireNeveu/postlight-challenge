import db
from app import run_app

print('Setting up Database')

db._metadata.create_all(db._engine)

print('Running')

run_app()
