.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| sort \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install-packages-dev: ## Install packages for the dev environment
	@echo -e "\e[1;34mcreating the virtual environment ...\e[0m" && \
		python3 -m venv venv && \
		echo -e "\e[1;34mactivating the virtual environment ...\e[0m" && \
		source ./venv/bin/activate && \
		echo -e "\e[1;34minstalling project's requirements ...\e[0m" && \
		pip install -U pip -r requirements/dev-requirements.txt

install-packages-prod: ## Install packages for the prod environment
	@echo -e "\e[1;34mcreating the virtual environment ...\e[0m" && \
		python3 -m venv venv && \
		echo -e "\e[1;34mactivating the virtual environment ...\e[0m" && \
		source ./venv/bin/activate && \
		echo -e "\e[1;34minstalling project's requirements ...\e[0m" && \
		pip install -U pip -r requirements/prod-requirements.txt

run-service: ## Running the service
	@echo -e "\e[1;34mactivating the virtual environment ...\e[0m" && \
		source ./venv/bin/activate && \
		echo -e "\e[1;34mredirecting to 'src' directory ...\e[0m" && \
		cd src && \
		echo -e "\e[1;34mrunning service ...\e[0m" && \
		python main.py

run-tests: ## Running test suite and generate coverage report
	@echo -e "\e[1;34mactivating the virtual environment ...\e[0m" && \
		source ./venv/bin/activate && \
		echo -e "\e[1;34mrunning 'pytest' with configs in '.coveragerc' file ...\e[0m" && \
		py.test \
			-vv \
			--cov . tests \
			--cov-report term-missing \
			--cov-report html:cov_html \
			--cov-report xml:cov.xml \
			--cov-config .coveragerc && \
		echo -e "\e[1;34mcleaning directory ...\e[0m" && \
		rm -r ./.pytest_cache/ 2> /dev/null && \
		rm ./.coverage 2> /dev/null

build-docker-image: ## Building docker image for the service
	@docker build --rm -f "Dockerfile" -t user-management-service:latest .

run-docker-container: ## Running docker container on service port specified (scale factor of 5 instances as just number)
	@docker-compose up -d --build --scale rest-api=5

stop-docker-container: ## Stopping docker container of the service
	@docker-compose down