from datetime import datetime
import mysql.connector
from config import mysql_settings as mss
from datetime import date

# Function to create the connection with the db
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
    except Exception as e:
        raise Exception(f"Failed to connect to the database: {e}")

# Function to format the date and time for display in appointments
def format_appointments(results):
    todays_appointments = []
    for row in results:
        formatted_date = row[0].strftime('%Y-%m-%d')
        formatted_time = (datetime.min + row[1]).strftime('%H:%M')
        new_row = (formatted_date, formatted_time) + row[2:]
        todays_appointments.append(new_row)
    return todays_appointments

# Function to query the db- not working properly atm!!!
# def query_db(query, fetch = True):
#     result = []
#     try:
#         db_connection = _connect_to_db()
#         cur = db_connection.cursor()
#         print("Connected to DB")
#         cur.execute(query)
#         db_connection.commit()
#         if fetch:
#             cur.fetchall()
#     except Exception as e:
#         print(f"Failed to execute query: {e}")
#         return None
#     finally:
#         if db_connection:
#             db_connection.close()
#             print("DB connection is closed")
#     return result

# Function to query db and get appointments for today ('/')
def get_todays_appointments():
    today = date.today()
    todays_appointments = []
    query = f'''SELECT a.date, a.time AS 'Time', a.appointment_status AS 'Appointment Status', p.petname AS 'Pets Name', CONCAT(o.firstname, ' ', o.lastname) AS "Owner's name", o.phone AS 'Phone Number'
    FROM Appointments a JOIN pets p ON a.petid = p.petid
    JOIN owners o ON o.ownerid = p.ownerid
    WHERE date = '{today}'
    ORDER BY a.time;'''
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB")
        cur.execute(query)
        result = cur.fetchall()
        todays_appointments = format_appointments(result)
        cur.close()
    except Exception as e:
        print(f"Failed to get today's appointments: {e}")

    finally:
        if db_connection:
            db_connection.close()
            print('DB connection closed')
    return todays_appointments

# Function for viewing existing pets ('/patients')
def get_all_patient_info():
    pet_query = '''SELECT p.petid, p.petname, p.species, p.age,CONCAT(o.firstname, ' ', o.lastname) AS "Owner's name", MAX(a.notes) AS notes
                    FROM pets p
                    JOIN owners o ON p.ownerid = o.ownerid
                    LEFT JOIN appointments a ON p.petid = a.petid
                    GROUP BY p.petid
                    ORDER BY petid;'''
    # interact with database to get existing pets list
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB")
        cur.execute(pet_query)
        results = cur.fetchall()
        cur.close()
        return results
        # pets = query_db(pet_query)
        # return pets
    except Exception as e:
        print(f"Failed to get patient info: {e}")
        return []
    finally:
        if db_connection:
            db_connection.close()
            print('DB connection closed')


# Function to add new pet to database (/patients/add)
def add_patient_to_db(OwnerId, petName, species, age):
        new_pet_query = f'''INSERT INTO Pets (OwnerID, PetName, Species, Age) VALUES ({OwnerId}, '{petName}', '{species}', {age})'''
        try:
            db_connection = _connect_to_db()
            cur = db_connection.cubrsor()
            print("Connected to DB")
            cur.execute(new_pet_query)
            db_connection.commit()
            print(f'{petName} successfully add to database!')
            cur.close()
            # query_db(new_pet_query, fetch=False)

            return True
        except Exception as e:
            print(f"Failed to add patient info: {e}")
            return False
        finally:
            if db_connection:
                db_connection.close()
                print('DB connection closed')
       
# Function to add owner info to db
def add_owner_to_db(firstName, lastName, email, phone, address):
        new_owner_query = f'''INSERT INTO owners (firstname, lastname, email, phone, address) VALUES ('{firstName}', '{lastName}', '{email}', '{phone}', '{address}' )'''
        try:
            db_connection = _connect_to_db()
            cur = db_connection.cursor()
            print("Connected to DB")
            cur.execute(new_owner_query)
            db_connection.commit()
            print(f'{firstName} {lastName} successfully add to database!')
            cur.close()
            # query_db(new_pet_query, fetch=False)
            
            return True
        except Exception as e:
            print(f"Failed to add owner info: {e}")
            return False
        finally:
            if db_connection:
                db_connection.close()
                print('DB connection closed')

# Function to get ownerid
def get_owner_info(email):
    id_query = f"""SELECT * FROM owners
                WHERE email = '{email}';"""  
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB")
        cur.execute(id_query)
        info = cur.fetchall()
        cur.close()
        return info
    except Exception as e:
        print(f"Failed to get owner info: {e}")
        return []
    finally:
        if db_connection:
            db_connection.close()
            print('DB connection closed')


    # Function to add new booking to database
def add_booking_to_db(pet_id, date, time, status):
    new_booking_query = f'''INSERT INTO Appointments (Date, Time, PetID, Appointment_status) 
                        VALUES ('{date}', '{time}', {pet_id}, '{status}')'''
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB")
        cur.execute(new_booking_query)
        db_connection.commit()
        print('Sucessfully added to database!')
        cur.close()
        return True
    except Exception as e:
        print(f"Failed to add booking: {e}")
        return False
    finally:
        if db_connection:
            db_connection.close()
            print('DB connection closed')
