# Game of Thrones API Project
This project is a **RESTful API** built using **Flask** for managing Game of Thrones characters. The API includes endpoints for performing CRUD operations on an in-memory list of characters, with support for pagination, filtering, sorting, and validation. It also includes functionality to create, edit, and delete characters.

## Table of Contents
- [Project Overview](#project-overview)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Running the API](#running-the-api)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
This **Game of Thrones API** allows users to interact with a list of characters from the fictional world of *Game of Thrones*. It enables functionalities such as retrieving, filtering, sorting, adding, editing, and deleting characters. The API is designed with simplicity and extensibility in mind.

### Key Features:
- **Pagination**: Retrieve a subset of characters with `limit` and `skip` parameters.
- **Filtering**: Filter characters by attributes like name, house, and age.
- **Sorting**: Sort characters by specific attributes such as `name`, `age`, or `house`.
- **CRUD Operations**: Add, update, and delete characters.
- **Validation**: Ensure that character data is well-formed.

## API Endpoints
### 1. **Fetch all characters (with Pagination)**
- **GET `/characters`**
- **Query Parameters**:
  - `limit`: Number of results per page (default is 20 if not specified)
  - `skip`: Number of results to skip (default is 0 if not specified)
- **Description**: Returns a paginated list of characters.

### 2. **Fetch a specific character by ID**
- **GET `/characters/<int:id>`**
- **Description**: Returns a single character by their unique `id`.

### 3. **Fetch a filtered character list**
- **GET `/characters?name=<name>&house=<house>&age_more_than=<age>&age_less_than=<age>`**
- **Query Parameters**:
  - `name`: Filter by character name.
  - `house`: Filter by character's house.
  - `age_more_than`: Filter by characters older than the specified age.
  - `age_less_than`: Filter by characters younger than the specified age.
- **Description**: Returns a filtered list of characters. Supports case-insensitive filtering.

### 4. **Fetch a sorted character list**
- **GET `/characters?sort_asc=<field>&sort_des=<field>`**
- **Query Parameters**:
  - `sort_asc`: Sort by a field in ascending order (e.g., `name`, `age`, `house`).
  - `sort_des`: Sort by a field in descending order (e.g., `name`, `age`, `house`).
- **Description**: Returns a list of characters sorted by the specified field in ascending or descending order.

### 5. **Combine Filter and Sort**
- **GET `/characters?name=<name>&age_more_than=<age>&sort_asc=<field>`**
- **Description**: Combine filters and sorting in the same request.

### 6. **Add a new character to the list**
- **POST `/characters`**
- **Request Body**:

   json
  {
    "id": <uniqueid>,
    "name": "<charactername>",
    "house": "<characterhouse>",
    "age": <age>,
    "role": "<characterrole>"
  }

- **Description**: Adds a new character to the list. The server validates that all fields are properly filled.

### 7. **Edit a character**
- **PATCH `/characters/<int:id>`**
- **Request Body**:

  json
  {
    "name": "<newname>",
    "house": "<newhouse>",
    "age": <newage>,
    "role": "<newrole>"
  }

- **Description**: Edits an existing character by their `id`.

### 8. **Delete a character**
- **DELETE `/characters/<int:id>`**
- **Description**: Deletes a character from the list by their `id`.

## Project Structure

game-of-thrones-api/
├── app/
│   ├── init.py      # Contains createapp function to initialize the Flask app
│   ├── models.py        # Data models for character information
│   ├── routes.py        # API routes for the project
│   ├── data.py          # Static data or data fetching logic
├── tests/
│   ├── testroutes.py   # Unit tests for routes
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── run.py               # Entry point to run the Flask application

## Dependencies
This project requires the following Python packages:
- **Flask**: The web framework used to build the API.
- **pydantic**: For data validation.
- **pytest**: For running unit tests.

To install the dependencies, run: pip install -r requirements.txt

## Running the API
To start the Flask API, use the following command: python run.py

By default, the API will be available at `http://127.0.0.1:5000`.

## Running Tests
This project uses pytest for testing.

### Running Tests Locally
1. Ensure you have pytest installed. If not, install it using: pip install pytest
2. Run the tests by executing the following command: pytest
3. `pytest` will automatically discover all files that start with `test_` or end with `_test.py`, and it will execute all test functions within them.

The output will look something like this:
==================== test session starts ====================
collected 3 items

test_routes.py ...          [100%]

==================== 3 passed in 0.03 seconds ================

### Interpreting Test Results
- `.` (dot) means the test passed.
- `F` means the test failed.
- `E` means there was an error during the test.
If any tests fail, detailed error messages will indicate which tests failed and why, helping you to debug the issue.


### Running Tests in a Specific File
To run tests from a specific file, specify the file name: pytest tests/test_routes.py

This will run only the tests defined in `test_routes.py`.
---
## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please ensure that you write tests for any new features or bug fixes.
---
## License
This project is licensed under the MIT License - see the LICENSE file for details.

  
