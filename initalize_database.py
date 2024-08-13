import mysql.connector

# The SQL for creating the table
create_table_query = """
CREATE TABLE IF NOT EXISTS aircraft (
    aircraft_id INT AUTO_INCREMENT PRIMARY KEY,
    model_name VARCHAR(100) NOT NULL,
    manufacturer VARCHAR(100) NOT NULL,
    aircraft_serial_number INT NOT NULL,
    configuration INT NOT NULL, -- Passenger or cargo capacity
    last_flight DATE, -- Date of the first flight
    certificate_of_airworthiness BOOLEAN DEFAULT TRUE, -- Is the aircraft currently servicable?
    country_of_origin VARCHAR(100), -- Country where the aircraft was manufactured
    country_of_registration VARCHAR(100), -- Country where the aircraft is registered
    engine_type VARCHAR(100), -- Type of engine
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
"""

# The SQL for inserting a single row (placeholders for values)
insert_data_query = """
INSERT INTO aircraft (model_name, manufacturer, aircraft_serial_number, configuration, last_flight, certificate_of_airworthiness, country_of_origin, country_of_registration, engine_type)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

# The data to be inserted
aircraft_data = [
    ('Boeing 737-800', 'Boeing', 33541, 189, '2024-08-10', True, 'United States', 'Ireland', 'CFM56-7B'),
    ('Boeing 737-800', 'Boeing', 33813, 189, '2024-08-12', True, 'United States', 'Ireland', 'CFM56-7B'),
    ('Boeing 737-800', 'Boeing', 33922, 189, '2024-07-28', True, 'United States', 'Ireland', 'CFM56-7B'),
    ('Boeing 737-800', 'Boeing', 34117, 189, '2024-07-30', True, 'United States', 'Ireland', 'CFM56-7B'),
    ('Boeing 737-800', 'Boeing', 34266, 189, '2024-08-01', True, 'United States', 'Ireland', 'CFM56-7B'),
    ('Airbus A320-200', 'Airbus', 2172, 174, '2024-08-09', True, 'France', 'Ireland', 'CFM56-5B4/3'),
    ('Airbus A320-200', 'Airbus', 2238, 174, '2024-08-07', True, 'France', 'Ireland', 'CFM56-5B4/3'),
    ('Airbus A330-300', 'Airbus', 952, 317, '2024-08-05', True, 'France', 'Ireland', 'Trent 772B-60'),
    ('Airbus A330-300', 'Airbus', 1010, 317, '2024-08-02', True, 'France', 'Ireland', 'Trent 772B-60'),
    ('Airbus A330-300', 'Airbus', 1093, 317, '2024-08-03', True, 'France', 'Ireland', 'Trent 772B-60'),
    ('Boeing 777-200', 'Boeing', 32628, 224, '2024-08-08', True, 'United States', 'United Kingdom', 'GE90-94B'),
    ('Boeing 777-200', 'Boeing', 32644, 224, '2024-08-06', True, 'United States', 'United Kingdom', 'GE90-94B'),
    ('Airbus A320-200', 'Airbus', 1456, 180, '2024-08-01', True, 'France', 'United Kingdom', 'V2527-A5'),
    ('Airbus A320-200', 'Airbus', 1478, 180, '2024-07-29', True, 'France', 'United Kingdom', 'V2527-A5'),
    ('Boeing 787-9', 'Boeing', 38618, 214, '2024-08-05', True, 'United States', 'United Kingdom', 'GEnx-1B64'),
    ('Boeing 787-9', 'Boeing', 38625, 214, '2024-08-04', True, 'United States', 'United Kingdom', 'GEnx-1B64'),
    ('Airbus A350-1000', 'Airbus', 282, 331, '2024-08-03', True, 'France', 'United Kingdom', 'Trent XWB-97'),
    ('Airbus A350-1000', 'Airbus', 291, 331, '2024-08-02', True, 'France', 'United Kingdom', 'Trent XWB-97'),
    ('Airbus A320-200', 'Airbus', 7123, 182, '2024-08-11', True, 'France', 'United States', 'V2527-A5'),
    ('Airbus A320-200', 'Airbus', 7134, 182, '2024-08-10', True, 'France', 'United States', 'V2527-A5'),
    ('Airbus A320-200', 'Airbus', 7142, 182, '2024-08-09', True, 'France', 'United States', 'V2527-A5'),
    ('Airbus A320-200', 'Airbus', 7150, 182, '2024-08-08', True, 'France', 'United States', 'V2527-A5'),
    ('Airbus A320-200', 'Airbus', 7161, 182, '2024-08-07', True, 'France', 'United States', 'V2527-A5'),
    ('Airbus A320-200', 'Airbus', 7167, 182, '2024-08-06', True, 'France', 'United States', 'V2527-A5'),
    ('Airbus A320-200', 'Airbus', 7174, 182, '2024-08-05', True, 'France', 'United States', 'V2527-A5'),
    ('Boeing 737-800', 'Boeing', 34908, 189, '2024-08-12', True, 'United States', 'United States', 'CFM56-7B'),
    ('Boeing 737-800', 'Boeing', 34923, 189, '2024-08-11', True, 'United States', 'United States', 'CFM56-7B'),
    ('Boeing 737-800', 'Boeing', 34938, 189, '2024-08-10', True, 'United States', 'United States', 'CFM56-7B'),
    ('Boeing 737-800', 'Boeing', 34953, 189, '2024-08-09', True, 'United States', 'United States', 'CFM56-7B'),
    ('Boeing 737-800', 'Boeing', 34968, 189, '2024-08-08', True, 'United States', 'United States', 'CFM56-7B'),
    ('Airbus A320neo', 'Airbus', 8889, 165, '2024-08-07', True, 'France', 'Japan', 'CFM LEAP-1A'),
    ('Airbus A320neo', 'Airbus', 8891, 165, '2024-08-06', True, 'France', 'Japan', 'CFM LEAP-1A'),
    ('Boeing 787-9', 'Boeing', 38471, 215, '2024-08-05', True, 'United States', 'Japan', 'GEnx-1B64'),
    ('Boeing 787-9', 'Boeing', 38489, 215, '2024-08-04', True, 'United States', 'Japan', 'GEnx-1B64'),
    ('Boeing 777-300ER', 'Boeing', 41712, 264, '2024-08-03', True, 'United States', 'Japan', 'GE90-115B'),
    ('Boeing 777-300ER', 'Boeing', 41723, 264, '2024-08-02', True, 'United States', 'Japan', 'GE90-115B'),
    ('Airbus A380-800', 'Airbus', 247, 516, '2024-08-01', True, 'France', 'France', 'Trent 970B-84'),
    ('Airbus A380-800', 'Airbus', 258, 516, '2024-07-31', True, 'France', 'France', 'Trent 970B-84'),
    ('Airbus A380-800', 'Airbus', 269, 516, '2024-07-29', True, 'France', 'France', 'Trent 970B-84'),
    ('Airbus A350-900', 'Airbus', 182, 324, '2024-08-10', True, 'France', 'France', 'Trent XWB-84'),
    ('Airbus A350-900', 'Airbus', 191, 324, '2024-08-09', True, 'France', 'France', 'Trent XWB-84'),
    ('Boeing 787-9', 'Boeing', 38394, 280, '2024-08-08', True, 'United States', 'France', 'GEnx-1B74/75'),
    ('Boeing 787-9', 'Boeing', 38415, 280, '2024-08-07', True, 'United States', 'France', 'GEnx-1B74/75'),
    ('Airbus A320-200', 'Airbus', 7633, 174, '2024-08-06', True, 'France', 'France', 'CFM56-5B4/3'),
    ('Airbus A320-200', 'Airbus', 7651, 174, '2024-08-05', True, 'France', 'France', 'CFM56-5B4/3'),
    ('Airbus A320-200', 'Airbus', 7682, 174, '2024-08-04', True, 'France', 'France', 'CFM56-5B4/3'),
    ('Airbus A320-200', 'Airbus', 7713, 174, '2024-08-03', True, 'France', 'France', 'CFM56-5B4/3'),
    ('Airbus A320-200', 'Airbus', 7744, 174, '2024-08-02', True, 'France', 'France', 'CFM56-5B4/3') 
]

###
### Creating the Database
###
# estblishing connection with the mysql server
mydb = mysql.connector.connect(
    host="localhost", user="root",
    password=""
)

# initalising the connection in mycursor
mycursor = mydb.cursor()
# executing SQL to create the database
mycursor.execute("CREATE DATABASE IF NOT EXISTS aircraft_database")
# Closing the cursor
mycursor.close()
# Closing the mysql connection
mydb.close()
# Checking the code got this far
print("Database Created")

###
### Creating the Table
###
# Connecting to the database created above
mydb = mysql.connector.connect(
    host="localhost", user="root",
    password="", database="aircraft_database"
)

# initalising the connection in mycursor
mycursor = mydb.cursor()
# executing SQL to create the table
mycursor.execute(create_table_query)
print("Table Created")

###
### Populating the table
###
for aircraft in aircraft_data:
    mycursor.execute(insert_data_query, aircraft)
    print("Inserted ID:", mycursor.lastrowid)

mydb.commit()
mycursor.close()
mydb.close()

print("Table has been populated")