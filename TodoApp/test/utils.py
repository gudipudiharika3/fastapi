from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from..main import app
from ..database import Base
from fastapi.testclient import TestClient
import pytest
from ..models import Todos,Users
from ..routers.auth import bcrypt_context
SQLALCHEMY_DATABASE_URL = "sqlite:///./testdb.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args = {"check_same_thread": False},
    poolclass = StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    print("Using overridden get_db")
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def override_get_current_user():
    return {'user_name':'harikapadmini', 'id':1, 'user_role': 'admin'}

client = TestClient(app)

@pytest.fixture
def test_todo():
    todo = Todos(
        title = 'Learn to code!',
        description = "Need to lean everyday!",
        priority=5,
        complete=False,
        owner_id=1   # matches up with our fake created user id
    )
    db = TestingSessionLocal() #we should add testing db otherwise it add stuff of pdb and delete all the production db
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection: #After the testing it will delete todos because of yield stmt before
        connection.execute(text("DELETE FROM todos;"))
        connection.commit()


@pytest.fixture
def test_user():
    user = Users(
        user_name = 'harikapadmini',
        email = 'harika@gmail.com',
        first_name = 'harika',
        last_name = 'padmini',
        hashed_password = bcrypt_context.hash("testpassword"),
        role = "admin",
        phone_number = '9132077688',
    )
    db= TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    with engine.connect() as connection:  # After the testing it will delete todos because of yield stmt before
        connection.execute(text("DELETE FROM users;"))
        connection.commit()