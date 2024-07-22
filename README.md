# avkr17
# Flask Postgres Docker Application

Приложение демонстрирует простую структуру Flask, интеграцию с базой данных PostgreSQL и использование Docker для развертывания.

## Установка с использованием Docker контейнеров

### 1. Предварительные требования:

- Docker (последняя версия)
- Docker Compose (последняя версия)

### 2. Клонируйте репозиторий

### 3. Настройте переменные окружения:

Создайте файл `.env` в корневой директории проекта и настройте необходимые переменные окружения:

``` bash
DB_URL=postgres://user:password@db/db_name
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=db_name
```
Замените `db_name`, `user` и `password` на ваши значения.

### 4. Запустите приложение:

Используйте Docker Compose для сборки и запуска контейнеров:

``` bash
docker compose up --build
```

После успешного запуска контейнеров приложение будет доступно по адресу http://localhost:5000

## Локальный запуск приложения

### 1. Предварительные требования

Перед началом работы убедитесь, что на вашей машине установлены следующие компоненты:

- Python 3.10 или более поздняя версия
- PostgreSQL 16.0 или более поздняя версия
- pip 22.0 или более поздняя версия

### 2. Клонируйте репозиторий

### 3. Создайте виртуальное окружение:

``` bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Установите зависимости

``` bash
pip install -r requirements.txt
```

### 5. Настройте базу данных

 Откройте терминал и выполните следующую команду для создания новой базы данных и пользователя PostgreSQL:

  ``` bash
  psql -U postgres
  ```

Вместо `postgres` подставьте ваше имя пользователя в PostgreSQL.

После этого выполните следующие SQL команды в интерактивной консоли:

```sql
CREATE DATABASE db_name;
CREATE USER user WITH ENCRYPTED PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE db_name TO user;
```

Замените `db_name`, `user` и `password` на ваши значения.

### 6. Настройте переменные окружения:

Создайте файл `.env` в корневой директории проекта и настройте необходимые переменные окружения:

``` bash
DB_URL=postgres://user:password@db/db_name
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=db_name
```
Замените `db_name`, `user` и `password` на ваши значения.

### 7. Инициализация базы данных

Запустите миграции для создания необходимых таблиц в базе данных:

```bash
flask db upgrade
```

### 8. Запустите приложение командой: 

```bash
python runserver.py
```

Приложение будет доступно по адресу: http://localhost:5000


