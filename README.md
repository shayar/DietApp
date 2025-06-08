# Diet App

A production-ready template featuring:

- **Python (FastAPI) service** for AI/ML tasks

The service is containerized with Docker, follows scalable architecture, and exposes interactive API documentation (Swagger/OpenAPI).

---

## Table of Contents

- [Features](#features)
- [Folder Structure](#folder-structure)
- [Quickstart](#quickstart)
- [API Overview](#api-overview)
- [Example Usage](#example-usage)
- [Testing](#testing)
- [Folder/Code Explanation](#foldercode-explanation)
- [License](#license)

---

## Features

### Python FastAPI AI Service

- Demo AI endpoint (`/ai/predict`)
- Production-style modular code structure
- Swagger UI docs by default
- Example unit tests with pytest

### Dockerized

- Run the service with a single command using Docker Compose
- `.env`-driven configuration for secrets

---

## Folder Structure

```
DietApp/
│
├── ai-service/         # Python FastAPI AI microservice
│   ├── app/
│   │   ├── api/
│   │   ├── main.py
│   │   ├── services/
│   │   └── utils/
│   ├── tests/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env
│
├── docker-compose.yml
├── README.md
└── .env                # (optional) project-level configs
```

---

## Quickstart

1. **Clone the repository**

```sh
git clone <repo-url>
cd DietApp
```

2. **Configure environment variables**

- `ai-service/.env` (add as needed for real integration)

3. **Run with Docker Compose**

```sh
docker-compose up --build
```

- FastAPI AI: [http://localhost:8000](http://localhost:8000)

4. **Explore API Documentation**

- FastAPI Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## API Overview

### FastAPI AI Endpoints (`/ai`)

| Route    | Method | Description             | Auth Required? |
| -------- | ------ | ----------------------- | :------------: |
| /predict | POST   | Returns reversed string |       No       |

See `/docs` for interactive documentation.

---

## Example Usage

### Use the AI Service

```sh
curl -X POST http://localhost:8000/ai/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"hello world"}'
```

---

## Testing

- **Python**
  ```sh
  docker-compose exec ai-service pytest
  ```

---

## Folder/Code Explanation

### ai-service/

- `app/api/`: API routers (1 file per domain)
- `app/services/`: Database or ML model logic
- `app/utils/`: Logger and utilities
- `app/main.py`: FastAPI app, router registration
- `tests/`: Pytest unit tests

### docker-compose.yml

- Launches the service for development.

---

## License

MIT
