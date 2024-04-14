from flask import Flask, request, jsonify
from db_utils import get_todays_appointments, get_all_patient_info, add_patient_to_db, add_owner_to_db, get_owner_info


app = Flask(__name__)
app.config['SECRET_KEY']= 'mysecret'

@app.route('/', methods=['GET', 'POST'])
def index():
    res = get_todays_appointments()
    return jsonify(res)


@app.route('/search')
def search():
    pass


@app.route('/booking')
def booking():
    pass


@app.route('/alter')
def alter():
    pass


@app.route('/cancel')
def cancel():
    pass


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
    firstName = data.get('firstName')
    lastName = data.get('lastName')
    email = data.get('email')
    phone = data.get('phone')
    address = data.get('address')

    # run the function using the request data
    result = add_owner_to_db(firstName, lastName, email, phone, address)

    # Check if the patient was successfully added to the database
    if result:
        return jsonify({"message": f"{firstName} {lastName} successfully added to the database!"}), 200
    else:
        return jsonify({"message": "Failed to add patient to the database."}), 500

@app.route('/owners')
def owners():
    email = request.args.get('email')
    owner = get_owner_info(email)
    return jsonify(owner)

if __name__ == "__main__":
    app.run(port=3000, debug=True)