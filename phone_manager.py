# Manage a list of phones
# And a list of employees

# Each employee gets 0 or 1 phones

class Phone():

    def __init__(self, id, make, model):
        self.id = id
        self.make = make
        self.model = model
        self.employee_id = None


    def assign(self, employee_id):
        self.employee_id = employee_id


    def is_assigned(self):
        return self.employee_id is not None


    def __str__(self):
        return 'ID: {} Make: {} Model: {} Assigned to Employee ID: {}'.format(self.id, self.make, self.model, self.employee_id)



class Employee():

    def __init__(self, id, name):
        self.id = id
        self.name = name


    def __str__(self):
        return 'ID: {} Name {}'.format(self.id, self.name)



class PhoneAssignments():

    def __init__(self):
        self.phones = []
        self.employees = []


    def add_employee(self, employee):
        # TODO throw exception if two employees with same ID are added
        isId_inList = False
        for empl in self.employees:
            if empl.id == employee.id:
                isId_inList = True
                raise PhoneError('\n\tThis ID# {} is already in list. Update ID#'.format(employee.id))
                break
        if isId_inList == False:
            self.employees.append(employee)



    def add_phone(self, phone):
        # TODO throw exception if two phones with same ID are added
        isId_inList = False
        for phones in self.phones:
            if phones.id == phone.id: # Checks if the id is in the list of phones.
                isId_inList = True
                raise PhoneError("\n    {} \n    CAN'T REPEAT ID# {}".format(phone, phone.id))
                break
        if isId_inList == False: # the new phone gets added.
            self.phones.append(phone)


    def assign(self, phone_id, employee):
        # Find phone in phones list
        if self.phones.__contains__(phone_id):
            raise PhoneError('No ID')
            
        for phone in self.phones:
            if phone.id == phone_id:
                # TODO if phone is already assigned to an employee, do not change list, throw exception
                if phone.employee_id == employee.id:
                    raise PhoneError('\n\tPhone is already assigned to this employee ID# {}'.format(employee.id))
                    break
                # TODO if employee already has a phone, do not change list, and throw exception
                elif phone.employee_id != None:
                    raise PhoneError('\n\tThis employee already has a phone')
                    break
                # TODO if employee already has this phone, don't make any changes. This should NOT throw an exception.
                phone.assign(employee.id)
                return


    def un_assign(self, phone_id):
        # Find phone in list, set employee_id to None
        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(None)   # Assign to None


    def phone_info(self, employee):
        # find phone for employee in phones list

        # TODO  should return None if the employee does not have a phone
        # TODO  the method should throw an exception if the employee does not exist

        for phone in self.phones:
            if phone.employee_id == employee.id:
                return phone


        return None

# This class just pass, because what we need is just the Exception.
class PhoneError(Exception):
    pass
