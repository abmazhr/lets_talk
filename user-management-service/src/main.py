import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def main() -> None:
    from src.application.infrastructure.web.rest_implementation.flask_api.api import get_api
    from src.application.usecase.user.create import CreateUserUseCase
    from src.application.infrastructure.persistent.in_memory.in_memory import InMemoryUserDatabaseRepository

    # dependency injection
    db_repository = InMemoryUserDatabaseRepository()
    create_user_usecase = CreateUserUseCase(db_repository=db_repository)

    api = get_api(create_user_usecase=create_user_usecase)

    api.run(
        host='0.0.0.0',
        port=3000,
        debug=False
    )


if __name__ == "__main__":
    main()
