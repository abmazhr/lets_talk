#!/usr/bin/env bash

echo -e "\e[1;34mactivating the virtual environment ...\e[0m" && \
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