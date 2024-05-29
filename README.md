# Income and expenses management


## Table of Contents
- [Project-Overview](#Project-Overview)
- [System-Specification](#System-Specification)
- [Routes](#routes)
- [Usage](#usage)
- [Installing](#Installing)


## Project-Overview
The project is an income and expenses management system developed in Python using FastAPI. It helps users track their monthly budgets efficiently.

## System-Specification

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

### Documentation
You can find detailed and high-quality documentation in each file
## Routes

### User Routes
#### Sign-in 
```
GET /user/{email}/{password}
```
**Request:** email and password.

**Params**

| Parameter | Description                               |
|-----------|-------------------------------------------|
| email     | user name the user entered at sign-up     |
| password  | user password the user entered at sign-up |

**Response:** User object.

#### Sign-up 
```
POST /user/
```
**Request:** User object.

**Object properties**

| property | Description   |
|----------|---------------|
| email    | user email    |
| name     | user name     |
| password | user password |

**Response:** True.


#### User update
```
PUT /user/{email}
```
**Request:** Email and user object.

**Params**

| Parameter | Description                               |
|-----------|-------------------------------------------|
| email     | user name the user entered at sign-up     |

**Object properties to update**

| property | Description   |
|----------|---------------|
| email    | user email    |
| name     | user name     |
| password | user password |

**Response:** True.

### Expense Route 

#### Retrieve Expense
```
GET /expense/{expense_id}
```
**Request:** Expense ID.

**Params**

| Parameter   | Description                                         |
|-------------|-----------------------------------------------------|
| expense_id  | The unique identifier of the expense to retrieve    |

**Response:** The expense object corresponding to the expense_id.

#### Retrieve All Expenses Associated with Email
```
GET /expenses/{email}
```

**Request:** Email address.

**Params**

| Parameter | Description |
|------------|-----------------------------------------------------------|
| email | The email address associated with the expenses to retrieve|

**Response:** List of expense objects associated with the provided email.


#### Insert New Expense
```
POST /expenses/
```

**Request:** Expense object to insert.

**Required Object Properties**

| Property | Description |
|------------|---------------------|
| expense | The expense object. |

**Response:** True if the insertion is successful.



#### Update Expense
```
PUT /expenses/{expense_id}
```

**Request:** Expense ID and updated expense object.

**Params**

| Parameter | Description |
|---------------|--------------------------------------------------|
| expense_id | The unique identifier of the expense to update |

**Object properties to update**

| Property | Description                                      |
|-----------|--------------------------------------------------|
| id | Expense ID (required but automatically numbered) |
| user_email | Email of the user that expense the mony          |
| amount| amount of expense                                |
| description | A brief description of the expense               |
| target | Destination to which the expenditure was made    |
| date | The date on which the expenditure was made       |

**Response:** True if the update is successful.


#### Delete Specific Expense
```
DELETE /expenses/{expense_id}
```

**Request:** Expense ID to delete.

**Params**

| Parameter | Description |
|---------------|--------------------------------------------------|
| expense_id | The unique identifier of the expense to delete |


**Response:** True if the deletion is successful.


#### Delete All Expenses Associated with Email
```
DELETE /expenses/{email}
```

**Request:** Email address associated with the expenses to delete.

**Params**

| Parameter | Description |
|------------|-----------------------------------------------------------------|
| email | The email address associated with the expenses to be deleted |


**Response:** True if all deletions are successful.


#### Visualization for Expenses by Year
```
GET /expenses/{email}/{year}
```

**Request:** Email and year for visualization.

**Params**

| Parameter | Description |
|------------|---------------------------------------|
| email | The email of the user for visualization |
| year | Year for expenses visualization |

**Response:** True if the visualization is successfully displayed.





### Income Route 

#### Retrieve Income
```
GET /income/{income_id}
```

**Request:** Income ID.

**Params**

| Parameter  | Description                           |
|------------|---------------------------------------|
| income_id  | Unique identifier of the income        |

**Response:** The income object corresponding to the income_id.

#### Retrieve All Incomes Associated with Email
```
GET /incomes/{email}
```

**Request:** Email address.

**Params**

| Parameter  | Description                           |
|------------|---------------------------------------|
| email      | The email address associated with the incomes to retrieve |

**Response:** List of income objects associated with the provided email.

#### Insert New Income
```
POST /incomes/
```

**Request:** Income object to insert.

**Required Object Properties**

| Property   | Description         |
|------------|---------------------|
| income     | The income object   |

**Response:** True if the insertion is successful.

#### Update Income
```
PUT /incomes/{income_id}
```

**Request:** Income ID and updated income object.

**Params**

| Parameter  | Description                         |
|------------|-------------------------------------|
| income_id  | Unique identifier of the income      |

**Object properties to update**

| Property | Description                                   |
|-----------|-----------------------------------------------|
| id | Income ID (required but automatically numbered) |
| user_email | Email of the user that income the mony        |
| amount| amount of income                              |
| description | A brief description of the income             |
| source | Destination to which the incomeiture was made |
| date | The date on which the income was made  |

**Response:** True if the update is successful.

#### Delete Specific Income
```
DELETE /incomes/{income_id}
```

**Request:** Income ID to delete.

**Params**

| Parameter  | Description                           |
|------------|---------------------------------------|
| income_id  | Unique identifier of the income        |

**Response:** True if the deletion is successful.

#### Delete All Incomes Associated with Email
```
DELETE /incomes/{email}
```

**Request:** Email address associated with the incomes to delete.

**Params**

| Parameter  | Description                          |
|------------|--------------------------------------|
| email      | The email address associated with the incomes to be deleted     |

**Response:** True if all deletions are successful.

#### Visualization for Incomes by Year
```
GET /incomes/{email}/{year}
```

**Request:** Email and year for visualization.

**Params**

| Parameter  | Description                           |
|------------|---------------------------------------|
| email      | The email of the user for visualization |
| year       | Year for income visualization          |

**Response:** True if the visualization is successfully displayed.

## Usage
Server Base URI: http://127.0.0.1:8000 Use this Basic url with the correct route listed below

see Api: http://127.0.0.1:8000/docs
 

## Installing
Download this package, and then run:

```
pip install requirements.txt
```
and the server side runs!

