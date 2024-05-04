import sys

def inventory():
    cars = []

    def add_new_vehicle():
        while True:
            make = input('Enter vehicle make:\n')
            model = input('Enter vehicle model:\n')
            year = int(input('Enter vehicle year:\n'))
            mileage = int(input('Enter vehicle mileage:\n'))
        
            if confirm('new vehicle information'):
                cars.append(Vehicle(make, model, year, mileage))
                break

    def edit_inventory():
        pass
    
    def edit_vehicle():
        pass
    

def confirm(input):
    confirm = input(f'Confirm {input}: Y/n\n')
    return confirm

class Vehicle:
    def __init__(this, make, model, year, mileage):
        this.make = make
        this.model = model
        this.year = year
        this.mileage = mileage

def main_menu():
    while True:
        print('1. Do something')
        print('2. View Inventory')
        print('3. Add Vehicle')
        print('4. Update Vehicle Information')
        print('5. Remove Vehicle')
        print('0. Exit Program')
        input = int(input('Select an option: \n'))

        match input:
            case 1:
                print('Did something')
            case 2:
                print('View Inventory')
            case 3:
                print('Add Vehicle')
            case 4:
                print('Update Vehicle Information')
            case 5:
                print('Remove Vehicle')            
            case 0:
                break
            case _:
                print('Invalid input. Enter numerical value.')
    else:
        print('Exiting...')
        sys.exit()

