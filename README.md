# Logging Service

## Overview

This service provides two main functionalities:

1. **Log Ingestor**: Ingests and manages error logs with detailed information.
2. **Query Interface**: Provides a user interface for full-text search across logs with various filters.

## Log Ingestor

### Features

1. **Log Ingestion**: Ingests an error with the following details:
   - `message`
   - `error_level`
   - `api_name`
2. **Log Formatting**: Standardizes the format for logging across all APIs, including:
   - Timestamp
   - Log level
   - Source
   - Log message
3. **Logging Configuration**: Configures logging levels and file paths for each API through a configuration file.
4. **Error Handling**: Ensures robust error handling to prevent logging failures from disrupting the application's functionality.

## Query Interface

### Features

- Provides a user interface for full-text search across logs.
- Filters based on:
  - `level`
  - `log_string`
  - `timestamp`
  - `metadata.source`
- Ensures efficient and quick search results using Chroma Vector DB.

## Running the API

### Steps

1. **Navigate to the Project Directory**:
   ```sh
   cd path/to/project

2. **Create a Virtual Environment**:
   ```sh
   python -m venv .venv
   ```
3. **Activate the Virtual Environment**:
   - On Windows:
     ```sh
     activate
     ```
4. **Install the Requirements**:
   ```sh
   pip install -r requirements.txt
   ```
5. **Add folder for storing logs**:
   ```ssh
   mkdir "app/error_logs"
   ```
7. **Run the Uvicorn Server**:
   - On Windows:
     ```sh
     run
     ```

## API Usage

### Healthcheck Endpoint

- **Endpoint**: `GET http://127.0.0.1:8000/api/healthcheck`
- **Description**: Checks the health of the backend server.

### Postman Collection

For detailed API usage and endpoints, refer to the Postman collection:
[Postman Collection](https://www.postman.com/shivansh-team/workspace/pibit-ai/collection/25468789-1399f18f-f5c9-452d-badd-369a05757037?action=share&creator=25468789)
