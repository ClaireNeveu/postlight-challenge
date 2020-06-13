from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
import cattr

# TODO read from config
_engine = create_engine(
    "postgresql+psycopg2://postgres:devpass@postgres/postlight",
    pool_size=5
)

# TODO: move this out of a top-level global into a context variable managed by pyramid
pool = _engine.connect()

_metadata = MetaData()
department = Table('department', _metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
)

job = Table('job', _metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('description', String),
)

employee = Table('employee', _metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('photo_id', Integer),
    Column('job', Integer, ForeignKey("job.id")),
    Column('department', Integer, ForeignKey("department.id")),
    Column('location', String),
)

# TODO set up a relation between table and type to make deserialization automatic
def execute(return_type, statement):
    return (cattr.structure(r, return_type) for r in pool.execute(statement).fetchall())

def executeOne(return_type, statement):
    raw_response = pool.execute(statement).fetchone()
    if raw_response is None:
        return None
    return cattr.structure(raw_response, return_type)

def executeVoid(statement):
    raw_response = pool.execute(statement)
