from http import HTTPStatus

from fastapi import FastAPI

from src.schemas import Message, UserList, UserPublic, UserSchema

app = FastAPI()

data_base = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def hello_world():
    return {'message': 'Hello World'}


@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    data_base.append(user)
    return user


@app.get('/users', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': data_base}
