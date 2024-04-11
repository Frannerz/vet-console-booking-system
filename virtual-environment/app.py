from flask import Flask, render_template, url_for, request, redirect
from flask_mysqldb import MySQL
from config import mysql_settings as mss
from forms import PetForm
from utils import format_appointments
from datetime import date

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'
app.config['MYSQL_HOST'] = mss['host']
app.config['MYSQL_USER'] = mss['user']
app.config['MYSQL_PASSWORD'] = mss['password']
app.config['MYSQL_DB'] = mss['db']

mysql = MySQL(app)


@app.route('/', methods=['GET','POST'])
def index():
    today = date.today()
    print(today)
    query = '''SELECT a.date, a.time AS 'Time', a.appointment_status AS 'Appointment Status', p.petname AS 'Pets Name', CONCAT(o.firstname, ' ', o.lastname) AS "Owner's name", o.phone AS 'Phone Number' 
    FROM Appointments a JOIN pets p ON a.petid = p.petid
    JOIN owners o ON o.ownerid = p.ownerid
    WHERE date = %s
    ORDER BY a.time;'''
    try:
        # Query the db
        cursor = mysql.connection.cursor()
        cursor.execute(query, (today,))
        appointments = cursor.fetchall()
        cursor.close()
        # use imported utils function to edit the format of appointments
        todays_appointments = format_appointments(appointments)
        return render_template("index.html", todays_appointments=todays_appointments)
    except:
        print("Failed to read data from DB")
        message = 'Sorry, could not retrieve appointments. Please try again later.'
        return render_template("index.html", message=message, todays_appointments=[])
    finally:
        if cursor:
            cursor.close()
            print('The database is now closed')


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

@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    # change this to owner name/email on form?
    # Query for getting pets list:
    pet_query = '''SELECT p.petid, p.petname, p.species, p.age,CONCAT(o.firstname, ' ', o.lastname) AS "Owner's name", MAX(a.notes) AS notes
                    FROM pets p 
                    JOIN owners o ON p.ownerid = o.ownerid
                    LEFT JOIN appointments a ON p.petid = a.petid
                    GROUP BY p.petid
                    ORDER BY petid;'''
    # interact with database to get existing pets list
    cursor = mysql.connection.cursor()
    cursor.execute(pet_query)
    pets = cursor.fetchall()
    cursor.close()
    
    # create instance of pet form
    pet_form = PetForm()

    # if pet form is validated, collect data
    if pet_form.validate_on_submit():
        OwnerId = pet_form.OwnerId.data
        petName = pet_form.petName.data
        species = pet_form.species.data
        age = pet_form.age.data

        #  Add new pet to database
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO Pets (OwnerID, PetName, Species, Age) VALUES (%s,%s,%s,%s)''',(OwnerId,petName, species, age))
        mysql.connection.commit()
        
        # Get new pets list from database (need to edit this further)
        cursor.execute(pet_query)
        updated = cursor.fetchall()
        cursor.close()

        # Success message
        message = 'Patient added successfully!'
        return render_template('add_patient.html', external=True, _scheme='https', pets=updated, pet_form=pet_form, message=message)
   
    return render_template('add_patient.html',external=True, _scheme='https', pet_form = pet_form, pets=pets)

if __name__ == '__main__':
    app.run(debug=True)