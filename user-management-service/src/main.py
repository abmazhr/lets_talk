import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def main() -> None:
    from src.application.infrastructure.web.rest_implementation.flask_api.api import get_api
    from src.application.usecase.user.create import CreateUserUseCase
    from src.application.usecase.user.check_creds import CheckUserCredentialsUseCase
    from src.application.infrastructure.persistent.mongodb.mongodb import MongoUserDatabaseRepository
    from src.configs import (
        SERVICE_HOST,
        SERVICE_PORT,
        MONGODB_HOST,
        MONGODB_PORT,
        MONGODB_NAME
    )

    # dependency injection
    db_repository = MongoUserDatabaseRepository(configs={
        'MONGODB_HOST': MONGODB_HOST,
        'MONGODB_PORT': MONGODB_PORT,
        'MONGODB_NAME': MONGODB_NAME
    })
    create_user_usecase = CreateUserUseCase(db_repository=db_repository)
    check_user_credentials_usecase = CheckUserCredentialsUseCase(db_repository=db_repository)

    api = get_api(
        create_user_usecase=create_user_usecase,
        check_user_credentials_usecase=check_user_credentials_usecase
    )

    api.run(
        host=SERVICE_HOST,
        port=SERVICE_PORT,
        debug=False
    )


if __name__ == "__main__":
    main()
