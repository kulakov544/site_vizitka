#!/bin/bash

# Удалить все остановленные контейнеры и неиспользуемые образы
docker container prune -f
docker image prune -af
docker system prune -af

# Остановить и удалить старые контейнеры, сети и тома, созданные docker-compose
docker-compose down

# Запустить контейнеры
docker-compose up -d
