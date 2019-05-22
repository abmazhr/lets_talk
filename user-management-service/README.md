# User Management Service

This service is responsible of doing user logic like registrations

# Architecture (simplified onion/clean architecture)

![users_management_service_architecture](users_management_service_architecture.png)

# Explanation
* simple clean architecture implementation
* simple in-memory database implementation (Plugins as needed to be changed)
* simple flask rest-api implementation     (Plugins as needed to be changed)

# Usage
* `$ ./install_packages_dev.sh` or `$ sh install_packages_dev.sh`      # For installing dev requirements
* `$ ./install_packages_prod.sh` or `$ sh install_packages_prod.sh`    # For installing prod requirements
* `$ ./run_tests.sh` or `$ sh run_tests.sh`                            # For running tests
* `$ ./run_service.sh` or `$ sh run_service.sh`                        # For running service

### Example post request
* [http](https://httpie.org/) tool
    * `$ http post :3000/users name='abdulrahman' age=25 password='test' email='abmazhr@gmail.com'`
* [curl](https://curl.haxx.se) tool
    * `$ curl -d '{"name":"abdulrahman", "age": 25, "password": "test", "email": "abmazhr@gmail.com"}' -H "Content-Type: application/json" -X POST http://localhost:3000/users`


# Todo
- [ ] Adding configuration files to tweak service behaviours/preferences at runtime
- [ ] Adding auth/jwt mechanism if needed user communications later (better be)