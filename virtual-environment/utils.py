from datetime import timedelta, datetime

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