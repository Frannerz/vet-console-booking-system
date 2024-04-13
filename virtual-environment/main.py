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

def add_new_patient(owner_id, name, species, age):
    patient_data = {
        "name": name,
        "ownerid": owner_id,
        "species": species,
        "age": age
    }

    result = requests.post(
        'http://127.0.0.1:3000/patients/add',
        headers={'content-type': 'application/json'},
        data=json.dumps(patient_data)
    )

    return result.json()

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

# basic display for now, need to improve this!
def display_info(data):
    for item in data:
        print(item, '\n')

# Form for getting info about pets to add onto db
def get_pet_info():
    owner = int(input("Enter the owner id (1-10): "))
    name = input("Enter the animal's name: ")
    species = input("Enter the species of animal: ")
    age = input("Enter the animal's age: ")
    return [owner, name, species, age]


def add_new_booking():
    pass

def delete_booking():
    pass

def alter_booking():
    pass

def get_owner_info():
    pass

def get_action():
    return input('''What action would you like to take? 
            \n-To book a new appointment, enter 'book'
            \n-To add a new patient, enter 'add' 
            \n-To view existing patients, enter 'view' ''')


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
            new_pet = get_pet_info()
            add_new_patient(new_pet[0], new_pet[1], new_pet[2], new_pet[3])
            print(f'{new_pet[1]} has been added to the database!')
            
        elif action == 'view':
            display_info(view_pet_info())
        
        elif action == 'book':
            # Add code for booking appointments
            pass
        
        else:
            print("Invalid action. Please try again.")

        action = get_action()
        


    # add what to do if something else chosen

if __name__ == '__main__':
    run()