import mysql.connector

# Define the database and table creation script
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

insert_data_query = """
INSERT INTO aircraft (model_name, manufacturer, aircraft_serial_number, configuration, last_flight, certificate_of_airworthiness, country_of_origin, country_of_registration, engine_type)
VALUES
('Boeing 737-800', 'Boeing', 33541, 189, '2024-08-10', TRUE, 'United States', 'Ireland', 'CFM56-7B'),
('Boeing 737-800', 'Boeing', 33813, 189, '2024-08-12', TRUE, 'United States', 'Ireland', 'CFM56-7B'),
('Boeing 737-800', 'Boeing', 33922, 189, '2024-07-28', TRUE, 'United States', 'Ireland', 'CFM56-7B'),
('Boeing 737-800', 'Boeing', 34117, 189, '2024-07-30', TRUE, 'United States', 'Ireland', 'CFM56-7B'),
('Boeing 737-800', 'Boeing', 34266, 189, '2024-08-01', TRUE, 'United States', 'Ireland', 'CFM56-7B'),
('Airbus A320-200', 'Airbus', 2172, 174, '2024-08-09', TRUE, 'France', 'Ireland', 'CFM56-5B4/3'),
('Airbus A320-200', 'Airbus', 2238, 174, '2024-08-07', TRUE, 'France', 'Ireland', 'CFM56-5B4/3'),
('Airbus A330-300', 'Airbus', 952, 317, '2024-08-05', TRUE, 'France', 'Ireland', 'Trent 772B-60'),
('Airbus A330-300', 'Airbus', 1010, 317, '2024-08-02', TRUE, 'France', 'Ireland', 'Trent 772B-60'),
('Airbus A330-300', 'Airbus', 1093, 317, '2024-08-03', TRUE, 'France', 'Ireland', 'Trent 772B-60'),
('Boeing 777-200', 'Boeing', 32628, 224, '2024-08-08', TRUE, 'United States', 'United Kingdom', 'GE90-94B'),
('Boeing 777-200', 'Boeing', 32644, 224, '2024-08-06', TRUE, 'United States', 'United Kingdom', 'GE90-94B'),
('Airbus A320-200', 'Airbus', 1456, 180, '2024-08-01', TRUE, 'France', 'United Kingdom', 'V2527-A5'),
('Airbus A320-200', 'Airbus', 1478, 180, '2024-07-29', TRUE, 'France', 'United Kingdom', 'V2527-A5'),
('Boeing 787-9', 'Boeing', 38618, 214, '2024-08-05', TRUE, 'United States', 'United Kingdom', 'GEnx-1B64'),
('Boeing 787-9', 'Boeing', 38625, 214, '2024-08-04', TRUE, 'United States', 'United Kingdom', 'GEnx-1B64'),
('Airbus A350-1000', 'Airbus', 282, 331, '2024-08-03', TRUE, 'France', 'United Kingdom', 'Trent XWB-97'),
('Airbus A350-1000', 'Airbus', 291, 331, '2024-08-02', TRUE, 'France', 'United Kingdom', 'Trent XWB-97'),
('Airbus A320-200', 'Airbus', 7123, 182, '2024-08-11', TRUE, 'France', 'United States', 'V2527-A5'),
('Airbus A320-200', 'Airbus', 7134, 182, '2024-08-10', TRUE, 'France', 'United States', 'V2527-A5'),
('Airbus A320-200', 'Airbus', 7142, 182, '2024-08-09', TRUE, 'France', 'United States', 'V2527-A5'),
('Airbus A320-200', 'Airbus', 7150, 182, '2024-08-08', TRUE, 'France', 'United States', 'V2527-A5'),
('Airbus A320-200', 'Airbus', 7161, 182, '2024-08-07', TRUE, 'France', 'United States', 'V2527-A5'),
('Airbus A320-200', 'Airbus', 7167, 182, '2024-08-06', TRUE, 'France', 'United States', 'V2527-A5'),
('Airbus A320-200', 'Airbus', 7174, 182, '2024-08-05', TRUE, 'France', 'United States', 'V2527-A5'),
('Boeing 737-800', 'Boeing', 34908, 189, '2024-08-12', TRUE, 'United States', 'United States', 'CFM56-7B'),
('Boeing 737-800', 'Boeing', 34923, 189, '2024-08-11', TRUE, 'United States', 'United States', 'CFM56-7B'),
('Boeing 737-800', 'Boeing', 34938, 189, '2024-08-10', TRUE, 'United States', 'United States', 'CFM56-7B'),
('Boeing 737-800', 'Boeing', 34953, 189, '2024-08-09', TRUE, 'United States', 'United States', 'CFM56-7B'),
('Boeing 737-800', 'Boeing', 34968, 189, '2024-08-08', TRUE, 'United States', 'United States', 'CFM56-7B'),
('Airbus A320neo', 'Airbus', 8889, 165, '2024-08-07', TRUE, 'France', 'Japan', 'CFM LEAP-1A'),
('Airbus A320neo', 'Airbus', 8891, 165, '2024-08-06', TRUE, 'France', 'Japan', 'CFM LEAP-1A'),
('Boeing 787-9', 'Boeing', 38471, 215, '2024-08-05', TRUE, 'United States', 'Japan', 'GEnx-1B64'),
('Boeing 787-9', 'Boeing', 38489, 215, '2024-08-04', TRUE, 'United States', 'Japan', 'GEnx-1B64'),
('Boeing 777-300ER', 'Boeing', 41712, 264, '2024-08-03', TRUE, 'United States', 'Japan', 'GE90-115B'),
('Boeing 777-300ER', 'Boeing', 41723, 264, '2024-08-02', TRUE, 'United States', 'Japan', 'GE90-115B'),
('Airbus A380-800', 'Airbus', 247, 516, '2024-08-01', TRUE, 'France', 'France', 'Trent 970B-84'),
('Airbus A380-800', 'Airbus', 258, 516, '2024-07-31', TRUE, 'France', 'France', 'Trent 970B-84'),
('Airbus A380-800', 'Airbus', 269, 516, '2024-07-29', TRUE, 'France', 'France', 'Trent 970B-84'),
('Airbus A350-900', 'Airbus', 182, 324, '2024-08-10', TRUE, 'France', 'France', 'Trent XWB-84'),
('Airbus A350-900', 'Airbus', 191, 324, '2024-08-09', TRUE, 'France', 'France', 'Trent XWB-84'),
('Boeing 787-9', 'Boeing', 38394, 280, '2024-08-08', TRUE, 'United States', 'France', 'GEnx-1B74/75'),
('Boeing 787-9', 'Boeing', 38415, 280, '2024-08-07', TRUE, 'United States', 'France', 'GEnx-1B74/75'),
('Airbus A320-200', 'Airbus', 7633, 174, '2024-08-06', TRUE, 'France', 'France', 'CFM56-5B4/3'),
('Airbus A320-200', 'Airbus', 7651, 174, '2024-08-05', TRUE, 'France', 'France', 'CFM56-5B4/3'),
('Airbus A320-200', 'Airbus', 7682, 174, '2024-08-04', TRUE, 'France', 'France', 'CFM56-5B4/3'),
('Airbus A320-200', 'Airbus', 7713, 174, '2024-08-03', TRUE, 'France', 'France', 'CFM56-5B4/3'),
('Airbus A320-200', 'Airbus', 7744, 174, '2024-08-02', TRUE, 'France', 'France', 'CFM56-5B4/3');
"""

# estblishing connection with the mysql server
mydb = mysql.connector.connect(
    host = "localhost", user = "root",
    password = ""
)

# creating the database
mycursor = mydb.cursor()

mycursor.execute("create DATABASE aircraft_database")

mycursor.close()
mydb.close()

print("Database Created")

# Connecting to the Table
mydb = mysql.connector.connect(
    host = "localhost", user = "root",
    password = "", database = "aircraft_database"
)

# creating the database
mycursor = mydb.cursor()

mycursor.execute(create_table_query)

mycursor.close()
mydb.close()
print("Table Created")

# Populating the table
mydb = mysql.connector.connect(
    host = "localhost", user = "root",
    password = "", database = "aircraft_database"
)

mycursor = mydb.cursor()

mycursor.execute(insert_data_query)
mydb.commit()

print("Table has been populated, last ID:", mycursor.lastrowid)
mycursor.close()
mydb.close()