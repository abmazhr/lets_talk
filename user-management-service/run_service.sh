#!/usr/bin/env bash

echo -e "\e[1;34mactivating the virtual environment ...\e[0m" && \
source ./venv/bin/activate && \
echo -e "\e[1;34mredirecting to 'src' directory ...\e[0m" && \
cd src && \
echo -e "\e[1;34mrunning service ...\e[0m" && \
python main.py