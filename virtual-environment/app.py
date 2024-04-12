from flask import Flask, render_template, url_for, request, redirect, jsonify
from forms import PetForm
from db_utils import format_appointments, get_todays_appointments, get_all_patient_info, add_patient_to_db


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
    name = data.get('name')
    species = data.get('species')
    age = data.get('age')

    result = add_patient_to_db(ownerid, name, species, age)

    # Check if the patient was successfully added to the database
    if result:
        return jsonify({"message": f"{name} successfully added to the database!"}), 200
    else:
        return jsonify({"message": "Failed to add patient to the database."}), 500

    

if __name__ == '__main__':
    app.run(debug=True, port=5000)
