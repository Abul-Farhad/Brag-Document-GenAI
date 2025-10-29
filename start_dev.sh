#!/bin/bash

# Start PostgreSQL
echo "Starting PostgreSQL..."
docker compose up -d

# Wait for services to be ready
echo "Waiting for services to start..."
sleep 5

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Start Django development server
echo "Starting Django development server..."
python manage.py runserver