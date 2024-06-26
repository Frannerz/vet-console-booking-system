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

# Function to get booked appointments for today
def get_todays_appointments():
    today = date.today()
    todays_appointments = []
    query = f'''SELECT a.date, a.time AS 'Time', a.appointment_status AS 'Appointment Status', p.petname AS 'Pets Name', CONCAT(o.firstname, ' ', o.lastname) AS "Owner's name", o.phone AS 'Phone Number'
    FROM Appointments a JOIN pets p ON a.petid = p.petid
    JOIN owners o ON o.ownerid = p.ownerid
    WHERE date = '{today}'
    ORDER BY a.time;'''
    # db_connection = None
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

# Function to get appointments by date
def get_appointments_by_date(chosen_date):
    chosen_date = chosen_date
    todays_appointments = []
    query = f'''SELECT a.date, a.time AS 'Time', a.appointment_status AS 'Appointment Status', p.petname AS 'Pets Name', CONCAT(o.firstname, ' ', o.lastname) AS "Owner's name", o.phone AS 'Phone Number'
    FROM Appointments a LEFT JOIN pets p ON a.petid = p.petid
    LEFT JOIN owners o ON o.ownerid = p.ownerid
    WHERE date = '{chosen_date}'
    ORDER BY a.time;'''
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
def add_patient_to_db(owner_id, pet_name, species, age):
        new_pet_query = f'''INSERT INTO Pets (OwnerID, PetName, Species, Age) VALUES ({owner_id}, '{pet_name}', '{species}', {age})'''
        try:
            db_connection = _connect_to_db()
            cur = db_connection.cubrsor()
            print("Connected to DB")
            cur.execute(new_pet_query)
            db_connection.commit()
            print(f'{pet_name} successfully add to database!')
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
def add_owner_to_db(first_name, last_name, email, phone, address):
        new_owner_query = f'''INSERT INTO owners (firstname, lastname, email, phone, address) VALUES ('{first_name}', '{last_name}', '{email}', '{phone}', '{address}' )'''
        try:
            db_connection = _connect_to_db()
            cur = db_connection.cursor()
            print("Connected to DB")
            cur.execute(new_owner_query)
            db_connection.commit()
            print(f'{first_name} {last_name} successfully add to database!')
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
def add_booking_to_db(pet_id, date, time, notes):
    new_booking_query = f'''UPDATE Appointments
                            SET appointment_status = "Booked", petid = {pet_id}, notes = "{notes}"
                            WHERE date = "{date}" and time = "{time}"'''

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


# Function to cancel appointment
def delete_appointment_from_db(appointment_date, appointment_time, pet_ID):
    try:
        # Connect to the database
        db_connection = _connect_to_db()
        cursor = db_connection.cursor()

        # Construct and execute the UPDATE query to cancel the appointment and make cancelled appointment avalible to book
        appointment_update_query = '''UPDATE appointments 
                                      SET appointment_status = 'Available', 
                                          PetID = NULL, 
                                          notes = NULL 
                                      WHERE date = %s 
                                      AND time = %s
                                      AND appointment_status = 'Booked'
                                      AND PetID = %s'''
        cursor.execute(appointment_update_query, (appointment_date, appointment_time, pet_ID))
        db_connection.commit()

        # Check if any rows were affected
        if cursor.rowcount > 0:
            return True
        else:
            return False
# Exception handling for different kinds of common error
    except ValueError as ve:
        print(f'ValueError occurred: {ve}')
        return False
    except TypeError as te:
        print(f'TypeError occurred: {te}')
        return False
    except Exception as e:
# For all other exception 
        print(f'Error occurred: {e}')
        return False
    finally:
        if cursor:
            cursor.close()
        if db_connection:
            db_connection.close()

# Function to amend bookings
def amend_booking_in_db(appointment_id, new_date, new_time, notes):
    try:
        db_connection = _connect_to_db()
        cursor = db_connection.cursor()

        appointment_update_query = f'''UPDATE Appointments 
                                          SET Date = '{new_date}', Time = '{new_time}', Notes = '{notes}' 
                                          WHERE AppointmentID = {appointment_id}'''
        
        cursor.execute(appointment_update_query)
        db_connection.commit()
        
        cursor.close()
        print('Appointment updated')
    except Exception as e:  
        print(f"Error during amendment: {e}")
        return False
    finally:  
        if db_connection:
            db_connection.close()
