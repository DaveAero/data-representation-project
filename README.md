# Aircraft Management Flask Application

This repository contains a Flask web application for managing aircraft data. The application allows users to log in, view aircraft details, create new aircraft entries, update existing ones, and delete entries. The application connects to a MySQL database to store and retrieve aircraft data.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Application Structure](#application-structure)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Database Initialization](#database-initialization)

## Installation
1. **Clone the repository:**

   ```bash
   git clone https://github.com/DaveAero/data-representation-project.git
   cd data-representation-project
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```
   
  
3. **Activate the virtual environment:**
  * On Windows:
   
   ```bash
   venv\Scripts\activate
   ```

4. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration
Configuration settings such as the database connection details (host, username, password, and database name) are located in the dbconfig.py file. Update this file with your MySQL credentials:

  ```python
  # dbconfig.py

  db_host = 'your_host'
  db_user = 'your_username'
  db_password = 'your_password'
  db_database = 'your_database'
  ```
**If running on Local machine**
* host:"localhost",
* user:"root",
* password:"",
* database:"aircraft"

## Running the Application
1. **Start the Flask server:**

   ```bash
   python rest_server.py
   ```
   The server will start on http://127.0.0.1:5000.

2. **Access the application:**

   Open a web browser and go to http://127.0.0.1:5000/login to access the login page.

## Application Structure
* **rest_server.py:** The main Flask server file that defines the application routes and logic.
* **aircraft_DAO.py:** Data Access Object (DAO) file that handles interactions with the MySQL database for aircraft data.
* **initialize_database.py:** Script to initialize the MySQL database and create the required tables.
* **dbconfig.py:** Configuration file containing database connection details.
* **templates/:** Directory containing HTML template files (aircraft.html, login.html).
* **static/: Directory for static files like CSS, JavaScript, and images.

## Usage
### Login
Navigate to http://127.0.0.1:5000/login and enter your username and password to log in.

<details>
  <summary>Need to login?</summary>

  You can use the Admin login.  
  **User:** "admin"  
  **Password:** "password123"

</details>

### View Aircraft
After logging in, you will be redirected to the aircraft management page where you can view all aircraft entries.

## Create, Update, and Delete Aircraft
* **Create:** Click the "Create" button to add a new aircraft entry.
* **Update:** Click the "Update" button next to an aircraft entry to modify its details.
* **Delete:** Click the "Delete" button next to an aircraft entry to remove it from the database.

## Logout
Click the "Logout" button on the top-right corner to log out of the application.

## Endpoints
* **GET /login:** Displays the login page.
* **POST /login:** Authenticates the user and starts a session.
* **GET /logout:** Logs out the user and ends the session.
* **GET /aircraft:** Displays the aircraft management page.
* **GET /aircraftdata:** Fetches all aircraft data in JSON format.
* **POST /aircraft:** Adds a new aircraft entry to the database.
* **PUT /aircraft/<id>:** Updates an existing aircraft entry.
* **DELETE /aircraft/<id>:** Deletes an aircraft entry from the database.

## Database Initialization
The initialize_database.py script will create the database and tables required for the application. Make sure to update the database configuration in dbconfig.py before running the script.
