import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def main() -> None:
    from src.application.infrastructure.web.sockets.implementation.flask_sockets_implementation.io import get_io
    from src.application.usecase.user.check_creds import CheckUserCredentialsUseCase
    from src.application.infrastructure.internal_services_communication.via_http.requests_http_client import \
        RequestsHttpClient
    from src.application.infrastructure.message_broker.in_memory import InMemoryMessageBroker
    from src.application.infrastructure.persistent.in_memory import InMemoryOnlineUsersPersistent
    from src.application.usecase.user.add_online_user import AddOnlineUserUseCase
    from src.application.usecase.user.publish_online_user import PublishOnlineUserUseCase
    from src.application.usecase.user.remove_online_user import RemoveOnlineUserUseCase
    from src.configs import (
        SERVICE_HOST,
        SERVICE_PORT
    )

    # dependency injection
    http_client = RequestsHttpClient()
    in_memory_inline_user_persistent = InMemoryOnlineUsersPersistent()
    in_memory_message_broker = InMemoryMessageBroker()

    check_user_creds_usecase = CheckUserCredentialsUseCase(http_client=http_client)
    add_online_user_usecase = AddOnlineUserUseCase(online_user_persistent=in_memory_inline_user_persistent)
    remove_online_user_usecase = RemoveOnlineUserUseCase(online_user_persistent=in_memory_inline_user_persistent)
    publish_online_user_usecase = PublishOnlineUserUseCase(message_broker=in_memory_message_broker)

    api, io = get_io(
        check_user_creds_usecase=check_user_creds_usecase,
        add_online_user_usecase=add_online_user_usecase,
        remove_online_user_usecase=remove_online_user_usecase,
        publish_online_user_usecase=publish_online_user_usecase
    )

    # maybe replace with logger later? ;)
    print(f"Service is running at : http://{SERVICE_HOST}:{SERVICE_PORT}")
    io.run(
        app=api,
        host=SERVICE_HOST,
        port=SERVICE_PORT,
        debug=False
    )


if __name__ == '__main__':
    main()
