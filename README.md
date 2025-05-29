# my-ai-project

A production-ready monorepo template featuring:

- **Node.js (Express) API** for user management
- **Python (FastAPI) service** for AI/ML tasks

Both services are containerized with Docker, follow scalable architecture, and expose interactive API documentation (Swagger/OpenAPI).

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

### Node.js API

- User registration, login, JWT-based authentication
- Security best practices: Helmet, CORS, hashed passwords
- Swagger/OpenAPI docs auto-generated
- Example unit tests with Jest

### Python FastAPI AI Service

- Demo AI endpoint (`/ai/predict`)
- Production-style modular code structure
- Swagger UI docs by default
- Example unit tests with pytest

### Dockerized & Orchestrated

- Run both services with a single command using Docker Compose
- `.env`-driven configuration for secrets

---

## Folder Structure

```
DietApp/
│
├── api/           # Node.js Express API microservice
│   ├── src/
│   │   ├── controllers/
│   │   ├── middlewares/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── app.js
│   │   └── server.js
│   ├── tests/
│   ├── Dockerfile
│   ├── package.json
│   └── .env
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
   cd my-ai-project
   ```

2. **Configure environment variables**

   - `node-api/.env` (example):
     ```
     JWT_SECRET=supersecret
     ```
   - `ai-service/.env` (empty or add as needed for real integration)

3. **Run with Docker Compose**

   ```sh
   docker-compose up --build
   ```

   - Node.js API: [http://localhost:3000](http://localhost:3000)
   - FastAPI AI: [http://localhost:8000](http://localhost:8000)

4. **Explore API Documentation**
   - Node.js Swagger: [http://localhost:3000/api-docs](http://localhost:3000/api-docs)
   - FastAPI Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## API Overview

### Node.js API Endpoints (`/api/users`)

| Route     | Method | Description    | Auth Required? |
| --------- | ------ | -------------- | :------------: |
| /register | POST   | Register user  |       No       |
| /login    | POST   | Login, get JWT |       No       |
| /profile  | GET    | Get profile    |   Yes (JWT)    |

See `/api-docs` for interactive documentation.

### FastAPI AI Endpoints (`/ai`)

| Route    | Method | Description             | Auth Required? |
| -------- | ------ | ----------------------- | :------------: |
| /predict | POST   | Returns reversed string |       No       |

See `/docs` for interactive documentation.

---

## Example Usage

### Register a user

```sh
curl -X POST http://localhost:3000/api/users/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password"}'
```

### Login

```sh
curl -X POST http://localhost:3000/api/users/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password"}'
```

### Use the AI Service

```sh
curl -X POST http://localhost:8000/ai/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"hello world"}'
```

---

## Testing

- **Node.js**
  ```sh
  docker-compose exec node-api npm test
  ```
- **Python**
  ```sh
  docker-compose exec ai-service pytest
  ```

---

## Folder/Code Explanation

### node-api/

- `controllers/`: Business logic for each resource (user, etc.)
- `middlewares/`: Auth, error handlers, input validation, etc.
- `routes/`: API endpoints, with Swagger docs in JSDoc
- `services/`: External dependencies (e.g., database, external APIs)
- `utils/`: Logger, helper functions
- `app.js`/`server.js`: Main Express app and startup logic
- `tests/`: Jest test files

### ai-service/

- `app/api/`: API routers (1 file per domain)
- `app/services/`: Database or ML model logic
- `app/utils/`: Logger and utilities
- `app/main.py`: FastAPI app, router registration
- `tests/`: Pytest unit tests

### docker-compose.yml

- Launches both services for full-stack development.

---

## License

MIT
