# HBnB – Backend Project

## Overview

This project is a simplified backend implementation of an AirBnB-like application.  
It is built using a layered architecture to separate responsibilities between models, services, and API layers.

The main goal is to practice designing and implementing a clean backend structure with RESTful endpoints, validation, and basic testing.

---

## Architecture

The project follows a 3-layer architecture:

### 1. Models (Business Logic Layer)
Contains the core entities:

- User
- Place
- Review
- Amenity
- BaseModel

Responsibilities:
- Data validation
- Attribute constraints
- Entity relationships
- Timestamp and ID management

---

### 2. Services (Facade Layer)

Located in `services/facade.py`

Responsibilities:
- Handle business logic
- Create, retrieve, update entities
- Connect API layer with models
- Manage repository interactions

---

### 3. API Layer (Presentation Layer)

Located in `api/v1/`

Endpoints:
- /users
- /places
- /reviews
- /amenities

Responsibilities:
- Handle HTTP requests
- Validate input via Flask-RESTx
- Return responses with correct status codes
- Provide Swagger documentation

---

## Project Structure
`
app/
├── models/
├── services/
├── api/
│ └── v1/
├── init.py
`

---

## Features

### Users
- Create user
- Get user by ID
- Get all users
- Update user
- Email validation

### Places
- Create place
- Get place(s)
- Update place
- Includes owner and amenities
- Validation for price, latitude, longitude

### Reviews
- Create review
- Get reviews
- Update review
- Delete review
- Get reviews by place

### Amenities
- Create amenity
- Get amenity(s)
- Update amenity

---

## Validation Rules

### User
- Required fields: first_name, last_name, email
- Email must be valid format

### Place
- price ≥ 0
- latitude ∈ [-90, 90]
- longitude ∈ [-180, 180]

### Review
- rating between 1 and 5
- text must not be empty
- must reference valid user and place

### Amenity
- name is required and max 50 characters

---

## Relationships

- User → Places (1 to many)
- Place → Reviews (1 to many)
- Place → Amenities (many to many)
- User → Reviews (1 to many)

---

## Data Flow

API → Facade → Models → Repository

---

## Testing

Tools used:
- cURL
- Swagger (Flask-RESTx)
- unittest / pytest

Example:
POST /api/v1/users/

Expected:
- 201 Created (success)
- 400 Bad Request (invalid data)

---

## API Documentation

Swagger UI:
http://127.0.0.1:5000/api/v1/

---

## Run Project
python run.py
or
flask run

---

## Notes

- UUID is used for all entities
- No database (in-memory storage only)
- DELETE supported only for reviews
- Focus is on architecture and backend design