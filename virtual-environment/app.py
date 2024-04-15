from flask import Flask, request, jsonify
from db_utils import get_todays_appointments, get_all_patient_info, add_patient_to_db, add_owner_to_db, get_owner_info, add_booking_to_db, delete_appointment_from_db, amend_booking_in_db


app = Flask(__name__)
app.config['SECRET_KEY']= 'mysecret'

@app.route('/', methods=['GET', 'POST'])
def index():
    res = get_todays_appointments()
    return jsonify(res)


@app.route('/search')
def search():
    pass


@app.route('/booking', methods=['POST'])
def booking():
    data = request.json
    pet_id = data.get('pet_id')
    date = data.get('date')
    time = data.get('time')
    status = data.get('appointment_status', 'Booked')

    # Assuming a function exists to add the booking to the database
    result = add_booking_to_db(pet_id, date, time, status)

    if result:
        return jsonify({"message": "Booking successfully created!"}), 200
    else:
        return jsonify({"message": "Failed to create booking."}), 500


@app.route('/alter')
def alter():
    pass

@app.route('/booking/<int:appointment_id>', methods=['PUT'] )
def amend_booking(appointment_id):
    data = request.json
    new_date = data.get('new_date')
    new_time = data.get('new_time')
    notes = data.get('notes')
    # status = data.get('appointment_status', 'Booked')
    # appointment_id = data.get('appointment_id')

    result = amend_booking_in_db(appointment_id, new_date, new_time, notes)

    # Check if the appointment was successfully amended in the database

    if result:
        return jsonify({"message": f"Appointment {appointment_id} successfully amended!"}), 200
    else:
        return jsonify({"message": "Failed to amend appointment."}), 500

@app.route('/delete', methods=['POST'])
def delete_appointment():
    data = request.json
    appointment_date = data.get('appointment_date')
    appointment_time = data.get('appointment_time')
    pet_ID = data.get('pet_ID')

    result = delete_appointment_from_db(appointment_date, appointment_time, pet_ID)
# If function works then showcase what has been deleted
    if result:
        return jsonify({"message": f"Appointment cancelled",
                        "appointment_date": appointment_date,
                        "appointment_time": appointment_time,
                        "pet_ID": pet_ID}), 200
    else:
        return jsonify({"message": "Failed to cancel appointment. Appointment not found or already cancelled."}), 404



@app.route('/patients', methods=['GET', 'POST'])
def patients():
    pets= get_all_patient_info()
    return jsonify(pets)

@app.route('/patients/add/', methods=['POST'])
def add_patients():
    data = request.json
    # Extract relevant fields from the JSON data
    ownerid = data.get('ownerid')
    petname = data.get('name')
    species = data.get('species')
    age = data.get('age')

    # run the function using the request data
    result = add_patient_to_db(ownerid, petname, species, age)

    # Check if the patient was successfully added to the database
    if result:
        return jsonify({"message": f"{petname} successfully added to the database!"}), 200
    else:
        return jsonify({"message": "Failed to add patient to the database."}), 500

@app.route('/owners/add', methods=['GET', 'POST'])   
def add_owners():
    data = request.json
    # Extract relevant fields from the JSON data
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    phone = data.get('phone')
    address = data.get('address')

    # run the function using the request data
    result = add_owner_to_db(first_name, last_name, email, phone, address)

    # Check if the patient was successfully added to the database
    if result:
        return jsonify({"message": f"{first_name} {last_name} successfully added to the database!"}), 200
    else:
        return jsonify({"message": "Failed to add patient to the database."}), 500

@app.route('/owners')
def owners():
    email = request.args.get('email')
    owner = get_owner_info(email)
    return jsonify(owner)

if __name__ == "__main__":
    app.run(port=3000, debug=True)


