from flask import Flask, url_for, request, redirect, abort, jsonify
from aircraft_DAO import aircraftDAO
import initalize_database

#print("0")
initalize_database.check_and_drop_db()
initalize_database.create_db()
initalize_database.create_table()
initalize_database.populate_table()
#print("4")

app = Flask(__name__, static_url_path='', static_folder='staticpages')

# at the root page of the server
@app.route('/')
# this index function will be run
def index():
    # This text is displated in the HTML browser
    return "hello"

# Retrieve all aircraft
@app.route('/aircraft')
def getAllAircraft():
    aircraft_list = aircraftDAO.getAll()

    # Assuming aircraft_list is a list of tuples, convert it to a list of dictionaries
    aircraft_data = []
    for aircraft in aircraft_list:
        aircraft_dict = {
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
        aircraft_data.append(aircraft_dict)

    return jsonify(aircraft_data)

# Retrieve aircraft by id
@app.route('/aircraft/<int:id>')
def findAircraftById(id):
    aircraft = aircraftDAO.findByID(id)
    if aircraft is None:
        return jsonify({}), 204
    return jsonify(aircraft)


# Create a aircraft
### curl -X "POST" -H "content-type:application/json" -d "{\"Title\":\"test\", \"Author\":\"some guy\", \"Price\":123}" http://127.0.0.1:5000/books
@app.route('/aircraft', methods=['POST'])
def createAircraft():
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

# Update existing aircraft
# curl -X "PUT" -d "{\"Title\":\"New Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/books/1
@app.route('/aircraft/<int:id>', methods=['PUT'])
def updateAircraft(id):
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

# Delete aircraft
@app.route('/aircraft/<int:id>', methods=['DELETE'])
def deleteAircraft(id):
    aircraft = aircraftDAO.findByID(id)
    if aircraft is None:
        return jsonify({}), 404
    
    aircraftDAO.delete(id)
    return jsonify({"result": True})

if __name__ == "__main__":
    app.run(debug=True)