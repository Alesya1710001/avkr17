# avkr17
# Flask Postgres Docker Application

Приложение демонстрирует простую структуру Flask, интеграцию с базой данных PostgreSQL и использование Docker для развертывания.

## Установка

### 1. Предварительные требования:

- Docker (последняя версия)
- Docker Compose (последняя версия)

### 2. Клонируйте репозиторий

### 3. Настройте окружение:

Создайте файл `.env` в корневой директории проекта и настройте необходимые переменные окружения:

``` bash
DB_URL=postgres://user:password@db/db_name \
POSTGRES_USER=user \
POSTGRES_PASSWORD=password \
POSTGRES_DB=db_name \
```

### 4. Установите зависимости

``` bash
pip install -r requirements.txt
```

Убедитесь, что все необходимые зависимости указаны в файле `requirements.txt`.

### 5. Запустите приложение:

Используйте Docker Compose для сборки и запуска контейнеров:


``` bash
docker-compose up --build
```

## Использование

После успешного запуска контейнеров приложение будет доступно по адресу http://localhost:5000

