#!/bin/bash

echo "Display env"
env
echo
echo "Flake8"
find . -iname "*.py" | xargs flake8
echo
echo "Unittests"
nosetests
echo
