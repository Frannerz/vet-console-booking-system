from flask import Flask, render_template, url_for, request, redirect
from flask_mysqldb import MySQL
from config import mysql_settings as mss
from forms import PetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'
app.config['MYSQL_HOST'] = mss['host']
app.config['MYSQL_USER'] = mss['user']
app.config['MYSQL_PASSWORD'] = mss['password']
app.config['MYSQL_DB'] = mss['db']

mysql = MySQL(app)


@app.route('/', methods=['GET','POST'])
def index():
    return render_template("index.html")

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
    # interact with database to get existing pets list
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT * FROM Pets ''')
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
        cursor.close()

        # Get new pets list from database (need to edit this further)
        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT * FROM Pets ''')
        updated = cursor.fetchall()
        cursor.close()

        # Success message
        message = 'Patient added successfully!'
        return render_template('add_patient.html', external=True, _scheme='https', pets=updated, pet_form=pet_form, message=message)
   
    return render_template('add_patient.html',external=True, _scheme='https', pet_form = pet_form, pets=pets)

if __name__ == '__main__':
    app.run(debug=True)