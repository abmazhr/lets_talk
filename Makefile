.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| sort \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

run-services: ## Running docker container on services port specified (scale factor of 5 instances as just number)
	@docker-compose build rest-api sockets-server mongodb nginx && \
	 	docker-compose up -d --scale rest-api=5 --scale sockets-server=5 mongodb nginx

stop-services: ## Stopping docker container of the services
	@docker-compose down