import requests
import json
from db_utils import delete_appointment_from_db

def generate_todays_appointments():
    try:
        result = requests.get('http://127.0.0.1:3000')
        result.raise_for_status()  # Raise an exception for bad status codes
        return result.json()  # Decode JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching appointments: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def search_by_date():
    pass

def add_new_patient(owner_id, name, species, age):
    patient_data = {
        "name": name,
        "owner_id": owner_id,
        "species": species,
        "age": age
    }

    result = requests.post(
        'http://127.0.0.1:3000/patients/add',
        headers={'content-type': 'application/json'},
        data=json.dumps(patient_data)
    )

    return result.json()

# Form for getting info about pets to add onto db
def get_pet_info(ownerid):
    name = input("Enter the animal's name: ")
    species = input("Enter the species of animal: ")
    age = input("Enter the animal's age: ")
    return [ownerid, name, species, age]

def view_pet_info():
    try:
        response = requests.get('http://127.0.0.1:3000/patients')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching appointments: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def add_new_owner(first_name, last_name, email, phone, address):
    owner_data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
        "address": address
        }

    result = requests.post(
        'http://127.0.0.1:3000/owners/add',
        headers={'content-type': 'application/json'},
        data=json.dumps(owner_data)
    )
    return result.json()

# Form for getting info about pets to add onto db
def get_owner_info():
    first_name = (input("Enter the owner's first name: "))
    last_name = input("Enter the owner's last name: ")
    email = input("Enter the owner's email: ")
    phone = input("Enter the owner's phone number: ")
    address = input("Enter the owner's address: ")
    return [first_name, last_name, email, phone, address]

def view_owner(email):
    try:
        result = requests.get('http://127.0.0.1:3000/owners', params={'email': email})
        result.raise_for_status()  
        return result.json()  
    except requests.exceptions.RequestException as e:
        print(f"Error fetching owner: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None




# Form for getting info about booking to add onto db
def get_booking_info():
    pet_id = int(input("Enter the pet ID: "))
    date = input("Enter the date for the appointment (YYYY-MM-DD): ")
    time = input("Enter the time for the appointment (HH:MM:SS): ")
    return pet_id, date, time



def add_new_booking():
    pet_id, date, time = get_booking_info()

    booking_data = {
        "pet_id": pet_id,
        "date": date,
        "time": time,
        "appointment_status": "Booked"  # Assuming default status is "Booked" when creating a new booking
    }
    # attempts post request, if it can't it returns an error
    try:
        response = requests.post(
            'http://127.0.0.1:3000/booking',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(booking_data)
        )
        response.raise_for_status()  # Check for HTTP request errors
        print("Booking added successfully!")
        return response.json()  # Return the JSON response from the server
    except requests.exceptions.RequestException as e:
        print(f"Error adding booking: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def delete_booking_request(pet_ID, appointment_date, appointment_time):
    # Prepare the data to be sent in the request
    data = {
        'pet_ID': pet_ID,
        'appointment_date': appointment_date,
        'appointment_time': appointment_time
    }

    try:
        # Make a POST request to the server
        result = requests.post(
            'http://127.0.0.1:3000/delete',
            headers={'content-type': 'application/json'},
            data=json.dumps(data)
        )
        # Return the JSON response from the server
        return result.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return None



def delete_booking():
    pass

def alter_booking():
    appointment_id = input("Enter the booking id number: ")
    new_date = input("Enter the new date you want to book using this format (YYYY-MM-DD): ")
    new_time = input("Enter the date using this format (HH:MM:SS): ")
    notes = input("Reason for appointment: ")
    new_booking_data = {
        "appointment_id": appointment_id,
        "date": new_date,
        "time": new_time,
        "appointment_status": "Booked",
        "notes": notes
    }
    try:
        response = requests.put(
            'http://127.0.0:3000/booking/<int:appointment_id>',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(new_booking_data)
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error amending booking: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# basic display for now, need to improve this!
def display_info(data):
    for line in data:
        for item in line:
            print(f"{item:<15}", end='')
        print('\n')


def get_action():
    return input('''\n**** What action would you like to take? ****
            \n-To book a new appointment, enter 'book'
            \n-To add a new patient, enter 'add' 
            \n-To view existing patients, enter 'view'
            \n-To exit, enter 'exit' 
            \n To cancel an appointment, enter 'cancel'
            \n To amend an existent appointment, enter 'amend' 
            \n > ''')

appointment_headers = ['Date', 'Time', 'Status', 'Pet Name', 'Owner', 'Contact']

def print_headers(headers):
    for title in headers:
        print(f"{title:<15}", end='')
    print('\n')

# Function to create welcome message, includes calculations for length of stars
def welcome_message():
    star='*'
    total_length = 100

    # create welcome message
    text_length = len(" Hello, welcome to the veterinary practice booking system! ")
    padding_length = (total_length - text_length) // 2
    print(f'''\n{star*total_length}\n{' '*padding_length}{'Hello, welcome to the veterinary practice booking system!'}{' '*padding_length}\n{star*total_length}\n''')
    
    # create title for today's appointments
    text_length = len("Today's Appointments")
    stars_length = (total_length - text_length) // 2
    print(f"{star*stars_length} Today's Appointments {star*stars_length}\n")


def run():
    # Print welcome messages and today's appointments
    welcome_message()
    print_headers(appointment_headers)
    display_info(generate_todays_appointments())
    
    action = get_action()
    
    while action:
        if action == 'add':
            check_if_owner = input("""Is the owner in our database? Type 'y' or 'n'\n > """)
            if check_if_owner == 'y':
                # get owners id using their email
                email = input("Enter the customer's email address: ")
                owner_id = view_owner(email)[0][0]

                # add new pet to system
                new_pet = get_pet_info(owner_id)
                add_new_patient(new_pet[0], new_pet[1], new_pet[2], new_pet[3])
                print(f'{new_pet[1]} has been added to the database!')
            
            elif check_if_owner == 'n':
                # get new owner info
                new_owner = get_owner_info()

                # add new owner to db
                add_new_owner(new_owner[0],new_owner[1],new_owner[2],new_owner[3],new_owner[4])
                print(f'{new_owner[0]} {new_owner[1]} has been added to the system\n')
                
                # get info for the new pet
                new_owner_id = view_owner(new_owner[2])[0][0]
                new_pet = get_pet_info(new_owner_id)
                
                # add new pet to db
                add_new_patient(new_owner_id, new_pet[1], new_pet[2], new_pet[3])
                print(f'{new_pet[1]} has been added to the database!')
    
                
        elif action == 'view':
            display_info(view_pet_info())

            
        elif action == 'book':
            add_new_booking()
        
        elif action == 'cancel':
            # Get information for appointment to cancel
            pet_ID = input('Enter PetID: ')
            appointment_date = input('Enter appointment date (YYYY-MM-DD): ')
            appointment_time = input('Enter appointment time (HH:MM): ')
            # Call the delete_booking_request function to delete the appointment
            cancel_result = delete_appointment_from_db(appointment_date, appointment_time, pet_ID)
            if cancel_result:
                print('Booking deleted')
            else:
                print('Failed to delete booking. Please try again.')

        elif action == 'amend':
            alter_booking()
        
        elif action == 'exit':
            print('Goodbye')
            break

        else:
            print("Invalid action. Please try again.")

        # Once the user have finished, print the initial question again 
        action = get_action()
        


if __name__ == '__main__':
    run()

    