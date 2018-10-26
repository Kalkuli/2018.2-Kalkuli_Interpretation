#!/bin/bash

set -e
set -u


if [ $TRAVIS_PULL_REQUEST != "false" -o $TRAVIS_BRANCH != "master" ]
then
    echo "Skipping deployment on branch=$TRAVIS_BRANCH, PR=$TRAVIS_PULL_REQUEST"
    exit 0;
fi

# Heroku Deployment
# docker login -u _ -p "$HEROKU_TOKEN" registry.heroku.com
# docker build -t registry.heroku.com/kalkuli-interpretation/web -f Dockerfile.prod .
# docker push registry.heroku.com/kalkuli-interpretation/web
# heroku container:release web -a kalkuli-interpretation

# Zappa Deployment
pip3 install zappa
zappa update dev