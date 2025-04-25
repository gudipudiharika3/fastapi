from fastapi import status
from .utils import *
from ..routers.auth import get_current_user
from ..routers.users import get_db

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get("/user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['user_name'] == 'harikapadmini'
    assert response.json()['email'] == 'harika@gmail.com'
    assert response.json()['first_name'] == 'harika'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '9132077688'

def test_change_password_success(test_user):
    response = client.put('/user/password',json = {"password":"testpassword","new_password":"newpassword"})
    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_change_password_invalid_current_password(test_user):
    response = client.put('user/password',json = {"password":"wrong_password","new_password":"newpassword"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail':'Error on password change'}
def test_change_phone_number_success(test_user):
    response = client.put('user/phonenumber/8987390898')
    assert response.status_code == status.HTTP_204_NO_CONTENT

