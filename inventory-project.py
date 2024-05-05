import sys

class Vehicle:
    def __init__(this, make, model, year, mileage):
        this.make = make
        this.model = model
        this.year = year
        this.mileage = mileage

    def __str__(this):
        return f'Make: {this.make}, Model: {this.model}, Year: {this.year}, Mileage: {this.mileage}'

class Inventory():
    def __init__(self):
        self.cars = []

    def view(self):
        print(f'Current inventory total: {len(self.cars)} vehicle(s)\n')
        if len(self.cars) > 0:           
            for index, car in enumerate(self.cars):
                print(f'ID: {index + 1}.')
                print(f'Make: {car.make}')
                print(f'Model: {car.model}')
                print(f'Year: {car.year}')
                print(f'Mileage: {car.mileage}\n')

    def add_new_vehicle(self):
        while True:
            make = input('Enter vehicle make:\n')
            model = input('Enter vehicle model:\n')
            year = input_int('Enter vehicle year:\n')
            mileage = input_int('Enter vehicle mileage:\n')
            print(f'Vehicle information:\nMake: {make}\nModel: {model}\nYear: {year}\nMileage: {mileage}\n')
            
            if confirm('new vehicle information'):
                new_car = Vehicle(make, model, year, mileage)
                self.cars.append(new_car)
                print("Successfully added new vehicle.\n")
                break

    def update_vehicle(self):
        self.view()
        if len(self.cars) == 0:
            print('No vehicles in inventory to update.\n')
            return
        while True:
            index = input_int('Select vehicle to update (Enter ID number):\n') - 1

            if self.cars[index] not in self.cars:
                print('Invalid selection; vehicle not in inventory.\n')
                continue

            self.update_parameter(index)
            break

    def update_parameter(self, index):
        key = {1: 'make', 2: 'model', 3: 'year', 4: 'mileage'}
        while True:
            print('Select parameter to update:\n')
            parameter = input_int('1. Make\n2. Model\n3. Year\n4. Mileage\n')
            if parameter not in {1, 2, 3, 4}:
                print('Invalid selection. Enter a whole numerical value between 1-4.\n')
                continue
            
            update = None
            if parameter in {3, 4}:
                update = input_int(f'Update {key[parameter]} information:\n')
            else:
                update = input(f'Update {key[parameter]} information:\n')

            if not confirm(f'updating {key[parameter]} to {update}'):
                continue

            match parameter:
                case 1:
                    self.cars[index].make = update
                case 2:
                    self.cars[index].model = update
                case 3:
                    self.cars[index].year = update
                case 4:
                    self.cars[index].mileage = update
                case _:
                    pass
            print("Succesfully updated vehicle.\n")
            break

    def remove_vehicle(self):
        self.view()
        if len(self.cars) == 0:
            print('No vehicles in inventory to remove.\n')
            return
        while True:
            index = input_int('Select vehicle to remove (Enter ID number):\n') - 1

            if self.cars[index] not in self.cars:
                print('Invalid selection; vehicle not in inventory.\n')
                continue

            if confirm(f'removing {self.cars[index]}'):
                self.cars.pop(index)
                print('Successfully removed vehicle.\n')
            break
                

def confirm(phrase):
    while True:
        confirm = input(f'Confirm {phrase}: y/n\n')
        match confirm:
            case "y":
                return True
            case 'n':
                return False
            case _:
                print('Invalid response.\n')

def input_int(prompt):
    while True:
        value = input(prompt)
        if not value.isdigit():
            print('Invalid input. Enter a whole numerical value.')
            continue
        return int(value)

def main_menu():
    inventory = Inventory()
    while True:
        print('Main Menu')
        print('1. View Inventory')
        print('2. Add Vehicle')
        print('3. Update Vehicle Information')
        print('4. Remove Vehicle')
        print('0. Exit Program')

        user_input = input_int('Select an option: \n')

        match user_input:
            case 1:
                print('Viewing inventory...\n')
                inventory.view()
            case 2:
                print('Adding new vehicle...\n')
                inventory.add_new_vehicle()
            case 3:
                print('Updating vehicle information...\n')
                inventory.update_vehicle()
            case 4:
                print('Removing vehicle...\n')
                inventory.remove_vehicle()   
            case 0:
                print('Exiting...\n')
                sys.exit()
            case _:
                print('Unknown input value.\n')

main_menu()