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

## Deployment
To deploy the backend, I am using AWS lambda, which is a serverless compute service that runs your code in response to events and automatically manages the underlying compute resources for you. You can deploy the backend using the following command:

Build the backend using the AWS SAM CLI:
```bash
sam build
```

Test the backend locally using the AWS SAM CLI:
```bash
sam local start-api
```

This command will start a local server that simulates the AWS Lambda environment. You can test the backend by sending requests to the local server using a tool like Postman or curl.

Deploy the backend using the AWS SAM CLI:
```bash
sam deploy --guided
```
This command will prompt you for some information, such as the stack name, AWS region, and whether you want to save the configuration for future deployments. After providing the required information, the command will deploy the backend to AWS Lambda.

To create a sam package, you can run the following command:
```bash
sam package --output-template-file packaged.yaml --s3-bucket <your-s3-bucket>
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