# School Library Management System

This project is a backend API for a School Library Management System built using FastAPI, SQLAlchemy, and PostgreSQL. The system allows managing books, students, and inventory, with features such as adding books, registering students, issuing/returning books, and fetching the top 5 most popular books.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Database Models](#database-models)
- [Populating Dummy Data](#populating-dummy-data)

## Requirements

- Python 3.9+
- PostgreSQL
- Poetry (for dependency management)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd school_library_management_system
   
2. Install dependencies using Poetry:
   ```bash
   poetry install

3. Activate the virtual environment:
   ```bash
   poetry shell
   
## Database Setup

1. Install PostgreSQL:
   
   1. Using Homebrew (Recommended for macOS):<br/>
   
      ```bash
      brew install postgresql
   
   2. After installation, start PostgreSQL using:
      
      ```bash
      brew services start postgresql
   3. Verify the installation by checking the PostgreSQL version:

      ```bash
      psql --version
      
2. Access PostgreSQL with psql:
   1. Launch the PostgreSQL interactive terminal:

       ```bash
      psql postgres
   3. Create a new database user (role) with a password:

       ```bash
      CREATE USER your_username WITH PASSWORD 'your_password';
   5. Create the database for your project:

       ```bash
      CREATE DATABASE school_library_management;
   7. Grant all privileges to your user on the new database:

      ```bash
      GRANT ALL PRIVILEGES ON DATABASE school_library_management TO your_username;
      
3. Update the database configuration in app/core/config.py:

      ```bash
      DATABASE_URL = "postgresql://username:password@localhost:5433/school_library_db"

## Running the Application

   1. To start the FastAPI server, run:
      
      ```bash
      uvicorn app.main:app --reload
   3. Once the server is running, you can access your API through the following URLs:
      
      ```bash
      Base URL: http://127.0.0.1:8000
   4. #### Swagger Documentation:
       Swagger UI is a popular tool for visualizing and interacting with your API. It provides a user-friendly interface where you can see all the available endpoints, their required        parameters, and try out the API directly from the browser. It’s a great way to explore and test your API's functionality.
      ```bash
      Swagger Documentation: http://127.0.0.1:8000/docs
   5. ####Redoc Documentation:
      Redoc is another tool for generating interactive API documentation. It focuses on providing a clean and organized view of your API specifications, making it easy for developers       to understand and navigate through the API’s endpoints. Redoc is known for its detailed and customizable documentation layout.
      ```bash
      Redoc Documentation: http://127.0.0.1:8000/redoc
      
## Project Structure 

```
school_library_management_system/
│
├── app/
│   ├── api/                         # Contains API endpoints for handling HTTP requests
│   │   └── endpoints/               # Directory for organizing specific endpoint routes
│   │       ├── books.py             # Endpoints related to book operations (e.g., adding, fetching books)
│   │       ├── students.py          # Endpoints related to student operations (e.g., registering, fetching students)
│   │       └── inventory.py         # Endpoints for managing book inventory (e.g., issuing, returning books)
│   ├── core/
│   │   └── config.py                # Application configuration settings (e.g., database connection)
│   ├── db/                          # Database-related files
│   │   ├── models.py                # SQLAlchemy models representing database tables
│   │   ├── session.py               # Database session management and connection handling
│   │   └── crud.py                  # CRUD (Create, Read, Update, Delete) operations for interacting with the database
│   ├── schemas/                     # Pydantic schemas for data validation and serialization
│   │   ├── book.py                  # Schemas for book-related data
│   │   ├── student.py               # Schemas for student-related data
│   │   └── inventory.py             # Schemas for inventory-related data
│   ├── dummy/                       # Directory for populating the database with dummy data
│   │   └── dummy_data.py            # Script for populating the database with sample data for testing purposes               
│   └── main.py                      # The main entry point for the FastAPI application
├── poetry.lock                      # Poetry lock file
├── pyproject.toml                   # Poetry configuration file for managing dependencies
└── README.md                        # Project documentation
```

## API Endpoints

- `POST /api/books/`: Adds a new book to the system.
- `GET /api/books/`: Retrieves all books stored in the database.
- `GET /api/books/{book_id}`: Retrieves a specific book by its unique ID.
- `PUT /api/books/{book_id}`: Updates an existing book based on its ID.
- `DELETE /api/books/{book_id}`: Deletes a book from the database using its ID.
- `POST /api/students/`: Adds a new student to the system.
- `GET /api/students/`: Retrieves all students stored in the database.
- ` GET /api/students/{student_id}`: Retrieves a specific student by their unique ID.
- `PUT /api/students/{student_id}`: Updates an existing student based on their ID.
- `DELETE /api/students/{student_id}`: Deletes a student from the database using their ID.
- `POST /api/inventory/`: Adds a new inventory record.
- `GET /api/inventory/`: Retrieves all inventory records stored in the database.
- `GET /api/inventory/{inventory_id}`: Retrieves a specific inventory record by its unique ID.
- `PUT /api/inventory/{inventory_id}`: Updates an existing inventory record based on its ID.
- `DELETE /api/inventory/{inventory_id}`: Deletes an inventory record from the database using its ID.
- `GET /api/books/populae`: Retrieves the 5 most popular books along with the number of times they were issued.

## Database Models

### Book
   Table Name: books
```
id: Integer, Primary Key
title: String, Book Title
author: String, Author Name
total_copies: Integer, Total Copies of the Book
issued_copies: Integer, Issued Copies of the Book (Default: 0)
```
### Student
Table Name: students
```
id: Integer, Primary Key
name: String, Student Name
email: String, Student Email (Unique)
borrowed_books_count: Integer, Number of Borrowed Books (Default: 0)
```
### Inventory
Table Name: inventory
```
id: Integer, Primary Key
book_id: Integer, Foreign Key (Books)
student_id: Integer, Foreign Key (Students)
```

## Populating Dummy Data
To populate the tables with dummy data, run the following command:
   ```bash
   python app/dummy/dummy_data.py
   ```

This `README.md` provides comprehensive instructions and documentation for setting up, running, and understanding the project.
