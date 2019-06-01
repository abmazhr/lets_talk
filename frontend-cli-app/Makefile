.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| sort \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install-packages: ## Install packages for the environment
	@echo -e "\e[1;34mcreating the virtual environment ...\e[0m" && \
		python3 -m venv venv && \
		echo -e "\e[1;34mactivating the virtual environment ...\e[0m" && \
		source ./venv/bin/activate && \
		echo -e "\e[1;34minstalling project's requirements ...\e[0m" && \
		pip install -U pip -r requirements.txt

run-service: ## Running the service
	@echo -e "\e[1;34mactivating the virtual environment ...\e[0m" && \
		source ./venv/bin/activate && \
		echo -e "\e[1;34mredirecting to 'src' directory ...\e[0m" && \
		cd src && \
		echo -e "\e[1;34mrunning service ...\e[0m" && \
		python main.py