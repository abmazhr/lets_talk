.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| sort \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install-packages-dev-locally: ## Install packages for the dev environment [locally]
	@echo -e "\e[1;34mcreating the virtual environment ...\e[0m" && \
		python3 -m venv venv && \
		echo -e "\e[1;34mactivating the virtual environment ...\e[0m" && \
		source ./venv/bin/activate && \
		echo -e "\e[1;34minstalling project's requirements ...\e[0m" && \
		pip install -U pip -r requirements/dev-requirements.txt

install-packages-prod-locally: ## Install packages for the prod environment [locally]
	@echo -e "\e[1;34mcreating the virtual environment ...\e[0m" && \
		python3 -m venv venv && \
		echo -e "\e[1;34mactivating the virtual environment ...\e[0m" && \
		source ./venv/bin/activate && \
		echo -e "\e[1;34minstalling project's requirements ...\e[0m" && \
		pip install -U pip -r requirements/prod-requirements.txt

run-service-locally: ## Running the service [locally]
	@echo -e "\e[1;34mactivating the virtual environment ...\e[0m" && \
		source ./venv/bin/activate && \
		echo -e "\e[1;34mredirecting to 'src' directory ...\e[0m" && \
		cd src && \
		echo -e "\e[1;34mrunning service ...\e[0m" && \
		python main.py

run-tests-locally: ## Running test suite [locally] and generate coverage report
	@echo -e "\e[1;34mactivating the virtual environment ...\e[0m" && \
		source ./venv/bin/activate && \
		echo -e "\e[1;34mrunning 'pytest' with configs in '.coveragerc_locally' file ...\e[0m" && \
		py.test \
			-r s \
			-vvs \
			--cov . tests \
			--cov-report term-missing \
			--cov-report html:cov_html \
			--cov-report xml:cov.xml \
			--cov-config .coveragerc_locally && \
		echo -e "\e[1;34mcleaning directory ...\e[0m" && \
		rm -r ./.pytest_cache/ 2> /dev/null && \
		rm ./.coverage 2> /dev/null