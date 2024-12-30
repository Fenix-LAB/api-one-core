# image: postgres
FROM postgres:latest
# Set environment variables
ENV POSTGRES_USER postgres
ENV POSTGRES_DB one-core-db

# Copy the database initialization script:
COPY init_db.sh /docker-entrypoint-initdb.d/
# Make it executable:
RUN chmod +x /docker-entrypoint-initdb.d/init_db.sh

# This is the default port for postgres
EXPOSE 5432  