### Project Overview
The project is an income and expenses management system developed in Python using FastAPI. It helps users track their monthly budgets efficiently.

### Database
The data management is handled using MongoDB.

### Server-Side Development
The server-side development is done in Python.

### Functionalities
- User Management: Register, login, and update profile.
- Income and Expenses Management: Create, update, delete, and retrieve data.
- Visualization: Option to fetch data suitable for visualization using Matplotlib.

### Directory Structure
```
- app/
  - db_management/
    - conect_db.py
    - expense_collection.py
    - income_collection.py
    - user_collection.py
  - models/
    - Expense.py
    - Income.py
    - User.py
  - routes/
    - expense_route.py
    - income_route.py
    - user_route.py
  - services/
    - expense_service.py
    - income_service.py
    - user_service.py
    - visualization_service.py
  - validators/
    - string_validator.py
  - main.py
- tests/
  - user_test.py
```

### File Descriptions
- **db_management**: Contains files for database connection and collections management.
- **models**: Includes model definitions for Expense, Income, and User objects.
- **routes**: Consists of route definitions for expenses, incomes, and users.
- **services**: Contains service files for managing expenses, incomes, users, and visualization.
- **validators**: Includes a validator file for string validation.
- **tests**: Contains the user tests file for testing user-related functionalities.
- **main.py**: Entry point of the application.

### Usage
1. Set up the MongoDB database connection.
2. Run the FastAPI server using `uvicorn main:app`.
3. Access the API endpoints to manage incomes, expenses, and users.
