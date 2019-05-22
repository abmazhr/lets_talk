#!/usr/bin/env bash

echo -e "\e[1;34mcreating the virtual environment ...\e[0m" && \
python3 -m venv venv && \
echo -e "\e[1;34mactivating the virtual environment ...\e[0m" && \
source ./venv/bin/activate && \
echo -e "\e[1;34minstalling project's requirements ...\e[0m" && \
pip install -U pip -r requirements/prod-requirements.txt