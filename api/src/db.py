from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

# TODO read from config
db_engine = create_engine(
    "postgresql+psycopg2://postgres:devpass@localhost/postlight",
    pool_size=5
)
pool = db_engine.connect()

metadata = MetaData()
department = Table('department', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
)

job = Table('job', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('description', String),
)

employee = Table('job', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('photo_id', Integer),
    Column('job', Integer, ForeignKey("job.id")),
    Column('department', Integer, ForeignKey("department.id")),
    Column('location', String),
)

# Obviously not where we would be doing this in production
metadata.create_all(engine)
