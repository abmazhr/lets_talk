from typing import List, Callable


def register_handler() -> List[Callable]:
    from getpass import getpass

    from requests import session

    from src.configs import (
        USER_MANAGEMENT_SERVICE_HOST,
        USER_MANAGEMENT_SERVICE_PORT
    )
    from src.utils import db, MenuItems

    username = input("⇝ Username: ")
    if username == '':
        print("Username can't be empty.")
        return register_handler()

    password = getpass(prompt="⇝ Password: ")
    if password == '':
        print("Password can't be empty.")
        return register_handler()

    email = input("⇝ Email: ")

    try:
        age = int(input("⇝ Age: "))
    except ValueError:
        print('Age should be a number')
        return register_handler()

    http_session = session()
    try:
        response = http_session.post(
            url=f'http://{USER_MANAGEMENT_SERVICE_HOST}:{USER_MANAGEMENT_SERVICE_PORT}/users',
            json={
                'name': username,
                'password': password,
                'email': email,
                'age': age
            }
        )

        if response.status_code != 200:
            print('Error registering your username, please try again.')
            return register_handler()

        db['username'] = username
        db['password'] = password
        db['email'] = email
        db['age'] = age

        return [
            MenuItems.LOGIN_WITH_EXISTED_USER,
            MenuItems.CHAT,
            MenuItems.EXIT
        ]
    except:
        print('Error registering your username, please try again later.')
        return [
            MenuItems.REGISTER_NEW_USER,
            MenuItems.LOGIN_WITH_EXISTED_USER,
            MenuItems.EXIT
        ]
