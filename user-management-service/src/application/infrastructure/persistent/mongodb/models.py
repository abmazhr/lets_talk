from pymongo import MongoClient
from umongo import Instance, Document, fields


class Models:
    def __init__(self, *, db: MongoClient) -> None:
        self._instance = Instance(db)

        @self._instance.register
        class User(Document):
            name = fields.StringField(required=True, unique=True)
            password = fields.StringField(required=True)
            age = fields.IntegerField(required=True)
            email = fields.EmailField(required=False)

            class Meta:
                collection = db.user

        self.User = User
