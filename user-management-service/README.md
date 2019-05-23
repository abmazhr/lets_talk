# User Management Service

This service is responsible of doing user logic like registrations

# Architecture (simplified onion/clean architecture)

![users_management_service_architecture](users_management_service_architecture.png)

# Explanation

- simple clean architecture implementation
- simple in-memory database implementation (Plugins as needed to be changed)
- simple flask rest-api implementation (Plugins as needed to be changed)

# Usage

- `$ make` # For all the possible commands currently available for the project
  ![current_make_list](current_make_list.png)

### Example post request

- [http](https://httpie.org/) tool
  - `$ http post :3000/users name='abdulrahman' age=25 password='test' email='abmazhr@gmail.com'`
- [curl](https://curl.haxx.se) tool
  - `$ curl -d '{"name":"abdulrahman", "age": 25, "password": "test", "email": "abmazhr@gmail.com"}' -H "Content-Type: application/json" -X POST http://localhost:3000/users`

# Todo

- [ ] Implementing some sort of read database (postgresql maybe?) since with load-balancing we got different instances each with different in-memory database so data is not consisted, yet
- [ ] Adding configuration files to tweak service behaviours/preferences at runtime
- [ ] Adding auth/jwt mechanism if needed user communications later (better be)
