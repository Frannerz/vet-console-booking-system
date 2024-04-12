import requests
import json
from db_utils import get_todays_appointments

# def generate_todays_appointments():
#     try:
#         result = requests.get('http://127.0.0.1:5000')
#         result.raise_for_status()  # Raise an exception for bad status codes
#         return result.json()  # Decode JSON response
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching appointments: {e}")
#         return None
#     except ValueError as e:
#         print(f"Error decoding JSON: {e}")
#         return None

# def search_by_date():
#     pass

def generate_todays_appointments():
    try:
        result = requests.get('http://127.0.0.1:5000')
        result.raise_for_status()  # Raise an exception for bad status codes
        print(f"Response status code: {result.status_code}")
        print(f"Response content: {result.text}")
        return result.json()  # Decode JSON response
    except requests.exceptions.RequestException as e:
        if isinstance(e, requests.exceptions.HTTPError):
            print(f"Error fetching appointments: {e}")
            print(f"Response status code: {e.response.status_code}")
            print(f"Response content: {e.response.text}")
        else:
            print(f"Error fetching appointments: {e}")
        return None
    except ValueError as e:
        print(f"Error decoding JSON: {e}")
        return None

def add_new_patient(name, owner_id, species, age):
    patient_data = {
        "name": name,
        "ownerid": owner_id,
        "species": species,
        "age": age
    }

    result = requests.post(
        'http://127.0.0.1:5000/patients/add',
        headers={'content-type': 'application/json'},
        data=json.dumps(patient_data)
    )

    return result.json()

def add_new_booking():
    pass

def delete_booking():
    pass

def alter_booking():
    pass

def get_owner_info():
    pass

def display_appointments(data):
    print(data)
    for item in data:
        print(item)

def run():
    print('*******************************************************')
    print('Hello, welcome to the vetinary practice booking system!')
    print('*******************************************************')
    print()
    todays_apps = generate_todays_appointments()
    print('todays apps: ', todays_apps)
    print("************ Today's Appointments ************")
    display_appointments(todays_apps)


if __name__ == '__main__':
    run()