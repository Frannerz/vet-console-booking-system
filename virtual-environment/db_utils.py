from datetime import timedelta, datetime
import mysql.connector
from config import mysql_settings as mss
from datetime import date


def _connect_to_db():
    try:
        cnx = mysql.connector.connect(
        host=mss['host'],
        user=mss['user'],
        password=mss['password'],
        auth_plugin='mysql_native_password',
        database=mss['db']
        )
        print('DB connection successful')
        return cnx
    except mysql.Error as e:
        raise Exception(f"Failed to connect to the database: {e}")


def format_appointments(results):
    todays_appointments = []
    for row in results:
        # Format the date to format '%Y-%m-%d'
        formatted_date = row[0].strftime('%Y-%m-%d')
        # Format time to format '%H:%M'
        formatted_time = (datetime.min + row[1]).strftime('%H:%M')
        # Creating new tuple for the row with the formatted time:
        new_row = (formatted_date, formatted_time) + row[2:]
        # append to list
        todays_appointments.append(new_row)
    return todays_appointments


def query_db(query):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB")
        cur.execute(query)
        result = cur.fetchall()
        
        return result
    except Exception as e:
        print(f"Failed to execute query: {e}")
        return None
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def get_todays_appointments():
    today = date.today()
    todays_appointments = []
    query = f'''SELECT a.date, a.time AS 'Time', a.appointment_status AS 'Appointment Status', p.petname AS 'Pets Name', CONCAT(o.firstname, ' ', o.lastname) AS "Owner's name", o.phone AS 'Phone Number'
    FROM Appointments a JOIN pets p ON a.petid = p.petid
    JOIN owners o ON o.ownerid = p.ownerid
    WHERE date = '{today}'
    ORDER BY a.time;'''
    try:
        result = query_db(query)
        if result:
            todays_appointments = format_appointments(result)
    except Exception as e:
        print(f"Failed to get today's appointments: {e}")

    return todays_appointments


def get_all_patient_info():
    pet_query = '''SELECT p.petid, p.petname, p.species, p.age,CONCAT(o.firstname, ' ', o.lastname) AS "Owner's name", MAX(a.notes) AS notes
                    FROM pets p
                    JOIN owners o ON p.ownerid = o.ownerid
                    LEFT JOIN appointments a ON p.petid = a.petid
                    GROUP BY p.petid
                    ORDER BY petid;'''
    # interact with database to get existing pets list
    try:
        pets = query_db(pet_query)
        return pets
    except Exception as e:
        print(f"Failed to get patient info: {e}")
        return []
    


def add_patient_to_db(OwnerId, petName, species, age):
        new_pet_query = f'''INSERT INTO Pets (OwnerID, PetName, Species, Age) VALUES ({OwnerId}, {petName}, {species}, {age})'''
        # Get new pets list from database (need to edit this further)
        try:
            query_db(new_pet_query)
            print(f'{petName} successfully add to database!')
            return True
        except Exception as e:
            print(f"Failed to add patient info: {e}")
            return False
       
   