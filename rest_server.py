from flask import Flask, request, redirect, url_for, render_template, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from aircraft_DAO import aircraftDAO
import initalize_database

# Initalising Database
initalize_database.check_and_drop_db()
initalize_database.create_db()
initalize_database.create_table()
initalize_database.populate_table()


#########################################################################################
app = Flask(__name__)
app.secret_key = 'verySecure' 

#########################################################################################
#Passwords here
#Passwords here
#Passwords here
# A simple in-memory user store
users = {
    "admin": generate_password_hash("password123"),  # User 1
    "andrew": generate_password_hash("streachYourLegs"), # User 2
    "david": generate_password_hash("myMumHasLitACandle") # User 3
}

#########################################################################################
# at the root page of the server
@app.route('/')
def serveLogin():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('aircraft.html')

#########################################################################################
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username exists and the password matches
        if username in users and check_password_hash(users[username], password):
            # Correct credentials, set session and redirect
            session['username'] = username
            flash('You were successfully logged in', 'success')
            return redirect(url_for('aircraftPage'))
        else:
            # Incorrect credentials, redirect back to login with a message
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))
    
    # If method is GET, simply render the login page
    return render_template('login.html')

#########################################################################################
@app.route('/logout')
def logout():
    # Clear the session data
    session.pop('username', None)
    flash('You were successfully logged out', 'success')
    return redirect(url_for('login'))

@app.route('/aircraft')
def aircraftPage():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('aircraft.html')

@app.route('/aircraftdata', methods=['GET'])
def get_aircraft_data():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    aircraftList = aircraftDAO.getAll()

    # Assuming aircraft_list is a list of tuples, convert it to a list of dictionaries
    aircraftData = []
    for aircraft in aircraftList:
        aircraftDict = {
            "aircraft_id": aircraft[0],
            "model_name": aircraft[1],
            "manufacturer": aircraft[2],
            "aircraft_serial_number": aircraft[3],
            "configuration": aircraft[4],
            "last_flight": aircraft[5],
            "certificate_of_airworthiness": aircraft[6],
            "country_of_origin": aircraft[7],
            "country_of_registration": aircraft[8],
            "engine_type": aircraft[9]
        }
        aircraftData.append(aircraftDict)


    return jsonify(aircraftData)


#########################################################################################
#########################################################################################
#########################################################################################

# Retrieve all aircraft
@app.route('/aircraft', methods=['POST'])
def createAircraft():
    if 'username' not in session:
        return redirect(url_for('login'))

    if not request.json:
        abort(400)
    aircraft = {
        "model_name": request.json.get("model_name"),
        "manufacturer": request.json.get("manufacturer"),
        "aircraft_serial_number": request.json.get("aircraft_serial_number"),
        "configuration": request.json.get("configuration"),
        "last_flight": request.json.get("last_flight"),
        "certificate_of_airworthiness": request.json.get("certificate_of_airworthiness"),
        "country_of_origin": request.json.get("country_of_origin"),
        "country_of_registration": request.json.get("country_of_registration"),
        "engine_type": request.json.get("engine_type"),
    }
    aircraft_id = aircraftDAO.create(tuple(aircraft.values()))
    aircraft["aircraft_id"] = aircraft_id
    
    return jsonify(aircraft), 201


#########################################################################################
# Retrieve aircraft by id
@app.route('/aircraft/<int:id>')
def findAircraftById(id):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    aircraft = aircraftDAO.findByID(id)
    if aircraft is None:
        return jsonify({}), 204
    return jsonify(aircraft)  

#########################################################################################
# Update existing aircraft
# curl -X "PUT" -d "{\"Title\":\"New Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/books/1
@app.route('/aircraft/<int:id>', methods=['PUT'])
def updateAircraft(id):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    aircraft = aircraftDAO.findByID(id)
    if aircraft is None:
        return jsonify({}), 404
    
    if not request.json:
        abort(400)
    
    # Convert the tuple returned by findByID to a dictionary
    foundAircraft = {
        "model_name": aircraft[1],
        "manufacturer": aircraft[2],
        "aircraft_serial_number": aircraft[3],
        "configuration": aircraft[4],
        "last_flight": aircraft[5],
        "certificate_of_airworthiness": aircraft[6],
        "country_of_origin": aircraft[7],
        "country_of_registration": aircraft[8],
        "engine_type": aircraft[9],
        "aircraft_id": aircraft[0]
    }

    reqJson = request.json

    # Update the dictionary with the new values from the request
    foundAircraft['model_name'] = reqJson.get('model_name', foundAircraft['model_name'])
    foundAircraft['manufacturer'] = reqJson.get('manufacturer', foundAircraft['manufacturer'])
    foundAircraft['aircraft_serial_number'] = reqJson.get('aircraft_serial_number', foundAircraft['aircraft_serial_number'])
    foundAircraft['configuration'] = reqJson.get('configuration', foundAircraft['configuration'])
    foundAircraft['last_flight'] = reqJson.get('last_flight', foundAircraft['last_flight'])
    foundAircraft['certificate_of_airworthiness'] = reqJson.get('certificate_of_airworthiness', foundAircraft['certificate_of_airworthiness'])
    foundAircraft['country_of_origin'] = reqJson.get('country_of_origin', foundAircraft['country_of_origin'])
    foundAircraft['country_of_registration'] = reqJson.get('country_of_registration', foundAircraft['country_of_registration'])
    foundAircraft['engine_type'] = reqJson.get('engine_type', foundAircraft['engine_type'])

    updated_aircraft = tuple(foundAircraft.values())

    # Pass the tuple to the update method
    print(updated_aircraft)
    aircraftDAO.update(updated_aircraft)
    
    return jsonify(foundAircraft)

#########################################################################################
# Delete aircraft
@app.route('/aircraft/<int:id>', methods=['DELETE'])
def deleteAircraft(id):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    aircraft = aircraftDAO.findByID(id)
    if aircraft is None:
        return jsonify({}), 404
    
    aircraftDAO.delete(id)
    return jsonify({"result": True})

#########################################################################################
#########################################################################################
#########################################################################################
if __name__ == "__main__":
    app.run(debug=True)