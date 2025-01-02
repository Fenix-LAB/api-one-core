# Backend for One Core
This is the backend for One Core, a project that aims to provide a database of all the information needed for this enterprise to work. This backend is built using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.10+ based on standard Python type hints.

## Installation
To install the backend, you need to have Python 3.10+ installed on your machine. You can download it from the [official website](https://www.python.org/downloads/). After installing Python, you can clone this repository and install the dependencies using the following commands:
```bash
git clone 
cd api-one-core
```
Then, you can create a virtual environment and install the dependencies:
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```
After installing the dependencies, you can run the backend using the following command:
```bash
python main.py
```

## Apply black formatter
To apply the black formatter to the code, you can run the following command:
```bash
black --config .\pyproject.toml .
```

## Create database backup
To create a backup of the database, first enter the database container:
```bash
docker exec -it <hash> bash
```
Then, you can run the following command to create a backup of the database:
```bash
pg_dump -U postgres one-core-db > /var/lib/postgresql/data/one-core-db-backup.sql
```
Finally, you can copy the backup to your local machine using the following command (outside the container):
```bash
docker cp <hash>:/var/lib/postgresql/data/one-core-db-backup.sql .
```

On my end I have a volume mounted to the container so I don't need to copy the backup to my local machine. I can just copy it from the volume