import mysql.connector
import dbconfig as cfg

class AircraftDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''

    def __init__(self): 
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']
    
    def getCursor(self): 
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
    
    def create(self, values):
        cursor = self.getCursor()
        sql = """
        INSERT INTO aircraft (
            model_name, manufacturer, aircraft_serial_number, configuration, 
            last_flight, certificate_of_airworthiness, country_of_origin, 
            country_of_registration, engine_type
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, values)
        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid

    def getAll(self):
        cursor = self.getCursor()
        sql = "SELECT * FROM aircraft"
        cursor.execute(sql)
        result = cursor.fetchall()
        self.closeAll()
        return result

    def findByID(self, id):
        cursor = self.getCursor()
        sql = "SELECT * FROM aircraft WHERE aircraft_id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        return result

    def update(self, values):
        cursor = self.getCursor()
        sql = """
        UPDATE aircraft 
        SET model_name = %s, manufacturer = %s, aircraft_serial_number = %s, 
            configuration = %s, last_flight = %s, 
            certificate_of_airworthiness = %s, country_of_origin = %s, 
            country_of_registration = %s, engine_type = %s 
        WHERE aircraft_id = %s
        """
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def delete(self, id):
        cursor = self.getCursor()
        sql = "DELETE FROM aircraft WHERE aircraft_id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

# Example usage
aircraftDAO = AircraftDAO()
