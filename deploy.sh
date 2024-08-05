#!/bin/bash

# Остановить и удалить старые контейнеры, сети и тома, созданные docker-compose
docker-compose down
docker rmi site_vizit

# Запустить контейнеры
docker-compose up -d
