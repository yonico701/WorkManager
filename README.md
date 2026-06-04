# WorkManager

WorkManager is a backend system for managing service jobs between customers and service providers.

The project was developed as a learning and portfolio project while studying Computer Engineering and focuses on object-oriented design, REST APIs, layered architecture, and database integration.

---

## Features

### Customer Management

* Create customers
* View customer details
* Update customer address
* Add and remove customer notes
* Activate and deactivate customers
* View customer jobs

### Service Provider Management

* Create service providers
* Manage professions
* Update base price
* Manage availability
* Activate and deactivate providers
* View provider jobs

### Job Management

* Create jobs
* Assign providers to jobs
* Schedule jobs
* Start jobs
* Complete jobs
* Cancel jobs
* Update job information

---

## Architecture

The project follows a layered architecture:

```text
Flask Routes
     ↓
Service Layer
     ↓
Repository Layer
     ↓
MySQL Database
```

### Project Structure

```text
WorkManager/
│
├── models/
│   ├── User.py
│   ├── Customer.py
│   ├── ServiceProvider.py
│   └── Job.py
│
├── repositories/
│   ├── customer_repository.py
│   ├── provider_repository.py
│   ├── job_repository.py
│   ├── user_repository.py
│   └── db_connection.py
│
├── services/
│   ├── customer_service.py
│   ├── provider_service.py
│   ├── job_service.py
│   └── System.py
│
├── tests/
│
├── archive/
│
└── app.py
```

---

## Technologies

* Python
* Flask
* MySQL
* REST API
* Git
* GitHub

---

## Design Patterns

### Repository Pattern

The repository layer is responsible for all database operations and isolates SQL logic from business logic.

### Service Layer

The service layer contains business rules and validations.

Examples:

* Provider availability validation
* Job status validation
* Profession matching validation
* Customer existence validation

---

## API Examples

### Create Customer

```http
POST /customers
```

### Get Customer

```http
GET /customers/{customer_id}
```

### Create Job

```http
POST /jobs
```

### Assign Provider

```http
PATCH /jobs/{job_id}/assign
```

### Complete Job

```http
PATCH /jobs/{job_id}/complete
```

---

## Current Status

Completed:

* Object Oriented Design
* MySQL Integration
* Repository Layer
* Service Layer
* Flask REST API
* Postman Testing
* Git & GitHub Integration

Planned:

* Backend Refactoring
* React Frontend
* Authentication & Authorization
* AWS Deployment
* CI/CD Pipeline

---

## Author

Yonatan Cohen

B.Sc. Computer Engineering

Ruppin Academic Center
