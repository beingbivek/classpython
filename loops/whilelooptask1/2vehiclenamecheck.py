while True:
    vehicle_name = input('Which vehicle are you waiting for?: ').lower()
    if vehicle_name == 'bus':
        print('Finally the wait is over.')
        break
    else:
        print('Wrong vehicle. Waiting for the vehicle.')
