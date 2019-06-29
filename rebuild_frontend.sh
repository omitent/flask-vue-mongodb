#!/bin/bash

cd frontend/
docker-compose exec frontend yarn build
cd ../
docker-compose up -d --force-recreate nginx
