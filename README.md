# FODOIST

`Fodoist` is a full stack todo application built with FARM stack. FastAPI and MongoDB on the backend and ReactJS on the frontend.

<hr>

### How to run Locally?

## Backend

Here is full tutorial how you can setup your own backend in this amazing stack.



maded by  ( osama Esmael Deghidy )

To run the backend, you need to have local mongodb instance running on you can setup a deployed instance using [MongoDB Atlas](https://www.mongodb.com/atlas/database).

### Setting up python environment

Run the following to create a virtual environment for the project. (Assuming you have python installed on local machine)

```bash
python -m virtualenv env
# OR
python -m venv env
#OR
python -m venv --system-site-packages env
#OR
python3 -m venv env

# if still doesn't work, google is your best friend!
```

If you're running the deployed instance, make sure to change the database connection string in `.env` file on the backend.

### Setting up `.env` file

To setup `.env` file on the backend, create a file named `.env` in `/backend/app`.
Add the following in the `.env` file.

```txt
JWT_SECRET_KEY=<RAMDOM_STRING>
JWT_REFRESH_SECRET_KEY=<RANDOM_SECTURE_LONG_STRING>
MONGO_CONNECTION_STRING=<MONGO_DB_CONNECTION_STRING>
# mongodb://localhost:27017/ <-- for local running instances
```

### Installing dependencies

Assuming you are in the base directory.

```bash
cd backend
pip install -r requirements.txt
```

### Activating virtual environment

```bash
# Windows
env/Scripts/activate

# MacOs + Linux
source env/bin/activate
```

### Running the backend

Assuming you are in the backend directory.

```bash
uvicorn app.app:app --reload
```

# API Documentation

## Base URL
The API is deployed at:
```
http://<your-deployment-url>
```

---

## Authentication
The API uses **JWT (JSON Web Token)** for authentication. You need to include the token in the `Authorization` header for all requests (except login and registration).

```plaintext
Authorization: Bearer <your_token>
```

To obtain a token, use the **Login** endpoint.

---

## Endpoints

### 1. User Authentication
#### Register User
- **URL:** `/auth/register`
- **Method:** `POST`
- **Description:** Registers a new user.
- **Request Body:**
  ```json
  {
    "username": "string",
    "email": "string",
    "password": "string"
  }
  ```
- **Response:**
  ```json
  {
    "message": "User registered successfully!"
  }
  ```

#### Login User
- **URL:** `/auth/login`
- **Method:** `POST`
- **Description:** Logs in a user and returns a JWT token.
- **Request Body:**
  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```
- **Response:**
  ```json
  {
    "access_token": "your_jwt_token"
  }
  ```

---

### 2. Todo Operations
#### Create a Todo
- **URL:** `/todos/`
- **Method:** `POST`
- **Description:** Creates a new todo for the authenticated user.
- **Request Body:**
  ```json
  {
    "title": "string",
    "description": "string",
    "status": "string",
    "due_date": "yyyy-mm-dd"
  }
  ```
- **Response:**
  ```json
  {
    "id": "string",
    "title": "string",
    "description": "string",
    "status": "string",
    "due_date": "yyyy-mm-dd",
    "user_id": "string"
  }
  ```

#### Get All Todos
- **URL:** `/todos/`
- **Method:** `GET`
- **Description:** Retrieves all todos for the authenticated user.
- **Response:**
  ```json
  [
    {
      "id": "string",
      "title": "string",
      "description": "string",
      "status": "string",
      "due_date": "yyyy-mm-dd",
      "user_id": "string"
    }
  ]
  ```

#### Get a Single Todo
- **URL:** `/todos/{todo_id}`
- **Method:** `GET`
- **Description:** Retrieves a single todo by its ID.
- **Response:**
  ```json
  {
    "id": "string",
    "title": "string",
    "description": "string",
    "status": "string",
    "due_date": "yyyy-mm-dd",
    "user_id": "string"
  }
  ```

#### Update a Todo
- **URL:** `/todos/{todo_id}`
- **Method:** `PUT`
- **Description:** Updates an existing todo by its ID.
- **Request Body:**
  ```json
  {
    "title": "string",
    "description": "string",
    "status": "string",
    "due_date": "yyyy-mm-dd"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Todo updated successfully!"
  }
  ```

#### Delete a Todo
- **URL:** `/todos/{todo_id}`
- **Method:** `DELETE`
- **Description:** Deletes a todo by its ID.
- **Response:**
  ```json
  {
    "message": "Todo deleted successfully!"
  }
  ```

---

## Postman Collection
- A Postman collection demonstrating all API endpoints is included in the repository under the file: `postman_collection.json`.
- Import it into Postman to easily test the API.

---

## Error Handling
The API provides proper error messages and status codes:
- **401 Unauthorized:** When authentication fails or token is missing.
- **404 Not Found:** When a resource (e.g., Todo) is not found.
- **400 Bad Request:** For invalid input data.
- **500 Internal Server Error:** For unexpected server errors.

---



