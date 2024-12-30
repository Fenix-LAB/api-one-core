#!/bin/bash

# Function to check if the database exists
database_exists() {
    psql -U postgres -lqt | cut -d \| -f 1 | grep -wq "$1"
}

# Check if the database exists
if database_exists "one-core-db"; then
    echo "Database 'one-core-db' already exists."
else
    echo "Creating database 'one-core-db'..."
    # Create the database
    psql -U postgres -c "CREATE DATABASE one-core-db;"
    echo "Database 'one-core-db' created."
fi