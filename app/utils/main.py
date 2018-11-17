from datetime import datetime, timezone
import re

def unixTimestamp(t):

    response = {}

    # Regex to check if is only numbers, max 12
    isNumberCheck = re.compile(r'^\d{1,12}$')

    # Regex to validate date format YYYY-MM-DD
    dateCheck = re.compile(r'^\d{1,4}-\d{2}-\d{2}')

    if isNumberCheck.match(t):

        daTime = datetime.fromtimestamp(int(t))

        response['unix'] = t
        response['utc'] = daTime.strftime('%c')
    elif dateCheck.match(t):

        daTime = datetime.strptime(t, '%Y-%m-%d')

        response['unix'] = int(daTime.timestamp())
        response['utc'] = daTime
    else:
        response['error'] = 'Please use a Unix timestamp or a valid date YYYY-MM-DD'

    return response


def currentDateTime():
    daTe = datetime.now(timezone.utc)
    response = {
        'unix': int(daTe.timestamp()),
        'utc': daTe
    }

    return response
