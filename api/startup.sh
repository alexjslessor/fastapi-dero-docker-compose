#!/bin/bash

uvicorn api.backend.main:app --port 5000 --reload

# if git branch | grep -q "develop"
# then
    # echo "on develop"
# else
    # echo "not on develop"
# fi


# npm/yarn deps
# npm install noble node-beacon-scanner --save
# yarn add noble node-beacon-scanner




# GIT CMDS
# remove item from cache
# git rm --cached products.csv

# clear all items from cache
# > git rm -r --cached . 
# > git add . 
# > git commit -m 'git cache cleared'
# > git push



# PYTHON CMDS

# virtualenvwrapper
#   make new env:
#   - mkvirtualenv <env name>
#   list envs:
#   - lsvirtualenv
#   show details
#    - showvirtualenv
#   delete virtualenv:
#   - rmvirtualenv



# PKGS
# pip install fastapi-users \
#             fastapi-mail \
#             aiofiles \#required for FileResponse
#             motor \# required for fastapi-users
#             gunicorn[gthread] \
#             uvicorn[standard] \
#             orjson \
#             google-cloud-storage \
#             mongoengine \
#             python-multipart \
#             pandas \
#             WeasyPrint \
#             pytest-cov \
#             selenium

# ASYNC TEST PKGS
# pip install httpx \
            # asgi-lifespan \
            # pytest-asyncio

# SELENIUM PYTEST
# pytest test_login.py

# SETUP COVERAGE + PYTEST
# definitions:
#   addopts:
#       - https://docs.pytest.org/_/downloads/en/stable/pdf/
#       - This contains a command-line (parsed by the py:mod:shlex module) that will be prepended to the command line
#         given by the user, see Builtin configuration file options for more information.

# testing dependancies
# pip install pytest-cov

# DIR STRUCTURE
# ~/tests
# ~/tests/conftest.py



# BASH CMDS
## NODE SERIAL PORT COMMANDS
#list serial ports:
#dmesg | grep tty


