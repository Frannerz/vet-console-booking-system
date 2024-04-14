import requests
import json

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

def add_new_patient(ownerid, name, species, age):
    patient_data = {
        "name": name,
        "ownerid": ownerid,
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

def add_new_owner(firstname, lastname, email, phone, address):
    owner_data = {
        "firstName": firstname,
        "lastName": lastname,
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

# basic display for now, need to improve this!
def display_info(data):
    for item in data:
        print(item, '\n')




def add_new_booking():
    pass

def delete_booking():
    pass

def alter_booking():
    pass



def get_action():
    return input('''What action would you like to take? 
            \n-To book a new appointment, enter 'book'
            \n-To add a new patient, enter 'add' 
            \n-To view existing patients, enter 'view'
            \n-To exit, enter 'exit' \n ''')


def run():
    print('*******************************************************')
    print('Hello, welcome to the vetinary practice booking system!')
    print('*******************************************************')
    print()
    print("**************** Today's Appointments ****************")
    display_info(generate_todays_appointments())
    action = get_action()
    
    while action:
        if action == 'add':
            check_if_owner = input("Is the owner in our database? Type 'y' or 'n': ")
            if check_if_owner == 'y':
                # get owners id using their email
                email = input("Enter the customer's email address: ")
                ownerid = view_owner(email)[0][0]
                # add new pet to system
                new_pet = get_pet_info(ownerid)
                add_new_patient(new_pet[0], new_pet[1], new_pet[2], new_pet[3])
                print(f'{new_pet[1]} has been added to the database!')
            elif check_if_owner == 'n':
                # get new owner info
                new_owner = get_owner_info()
                # add new owner to db
                add_new_owner(new_owner[0],new_owner[1],new_owner[2],new_owner[3],new_owner[4])
                print(f'{new_owner[0]} {new_owner[1]} has been added to the system\n')
                new_owner_id = view_owner(new_owner[2])[0][0]
                # get info for the new pet
                new_pet = get_pet_info(new_owner_id)
                # add new pet to db
                add_new_patient(new_owner_id, new_pet[1], new_pet[2], new_pet[3])
                print(f'{new_pet[1]} has been added to the database!')
    
                
        elif action == 'view':
            display_info(view_pet_info())

            
        elif action == 'book':
            # Add code for booking appointments
            pass
        
        elif action == 'exit':
            print('Goodbye')
            break

        else:
            print("Invalid action. Please try again.")

        action = get_action()
        


    # add what to do if something else chosen

if __name__ == '__main__':
    run()