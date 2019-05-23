from typing import Union, Dict

import bcrypt
from pymongo import MongoClient

from src.application.infrastructure.persistent.mongodb.models import Models
from src.domain.entity.error import Error
from src.domain.entity.success import Success
from src.domain.entity.user import User as UserEntity
from src.domain.gateway.user_database_repository import UserDatabaseRepository


class MongoUserDatabaseRepository(UserDatabaseRepository):

    def __init__(self, *, configs: Dict[str, str] = None) -> None:
        super().__init__(configs=configs)
        self.__db = MongoClient(configs.get('MONGODB_HOST'), configs.get('MONGODB_PORT')).users_management
        self.__models = Models(db=self.__db)

    def save_user(self, *, user: UserEntity) -> Union[Error, Success]:
        if self.__does_exist_before(user=user):
            return Error(reason=f'This username {user.name} does exist before, use different username please.')

        database_user = self.__models.User(
            name=user.name,
            password=bcrypt.hashpw(user.password.encode(), bcrypt.gensalt()),
            age=user.age,
            email=user.email
        )
        try:
            database_user.commit()
            dumped_database_user = database_user.dump()
            return Success(data=UserEntity(
                id=dumped_database_user['id'],
                name=dumped_database_user['name'],
                password=dumped_database_user['password'],
                age=dumped_database_user['age'],
                email=dumped_database_user['email']
            ))
        except:
            return Error(reason=f'Error saving user {user.name} into database.')

    def __does_exist_before(self, *, user: UserEntity) -> bool:
        return self.__models.User.find_one({"name": user.name}) is not None
