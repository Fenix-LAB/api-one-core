# Database PostgreSQL
We build a PostgreSQL database with Docker. The database is used to store the data of the application.

### Image:

https://hub.docker.com/_/postgres

### Docker build and run

Build the image of PostgreSQL

```bash
docker build -f Dockerfile -t my_image_one_core .
```

Run a container with the image of PostgreSQL

```bash
docker run -d \
--name one_core_db \
-p 5432:5432 \
-e POSTGRES_PASSWORD=onecore77 \
-v ${PWD}/pgdata:/var/lib/postgresql/data \
my_image_one_core
```

One line

```bash
docker run -d --name one_core_db -p 5432:5432 -e POSTGRES_PASSWORD=onecore77 -v ${PWD}/pgdata:/var/lib/postgresql/data my_image_one_core
```

### Docker run database

Run a container with the image of PostgreSQL


```bash
docker run -d \
--name one_core_db \
-p 5432:5432 \
-e POSTGRES_PASSWORD=onecore77 \
-v ${PWD}:/home/postgres/pgdata/data \
postgres:latest
```

### Docker exec

```bash
docker exec -it <id_container> bash
```

```bash
docker exec -it <id_container> psql -u postgres
```

### Load backup

```bash
psql -U potgres -d medical_db -f medicalrecords.sql
```

### SQL Shell

Init the SQL Shell

```bash
psql -U postgres
```

Create database:

```bash
create database <name>;
```

Show databases:

```bash
\l
```

Change database:

```bash
\c <name>
```

Show tables:

```bash
\dt
```

Get information of a table:

```bash
\d+ "<name>";
```

Show data of a table:

```bash
SELECT * <"FROM table_name">;
```

Delete a table:

```bash
DROP TABLE <"table_name">;
```