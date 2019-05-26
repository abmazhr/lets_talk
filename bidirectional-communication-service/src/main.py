import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def main() -> None:
    from src.application.infrastructure.web.sockets.implementation.flask_sockets_implementation.io import get_io
    from src.application.usecase.user.check_creds import CheckUserCredentialsUseCase
    from src.application.infrastructure.internal_services_communication.via_http.requests_http_client import \
        RequestsHttpClient
    from src.configs import (
        SERVICE_HOST,
        SERVICE_PORT
    )

    # dependency injection
    http_client = RequestsHttpClient()
    check_user_creds_usecase = CheckUserCredentialsUseCase(http_client=http_client)

    api, io = get_io(
        check_user_creds_usecase=check_user_creds_usecase
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
