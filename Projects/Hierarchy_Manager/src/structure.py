import random

class Employee:
    used_ids = set()

    def __init__(self, name, position, manager=None, employee_id=None):
        self.name = name
        self.position = position
        self.manager = manager
        self.children = []

        if employee_id is None:
            while True:
                random_id = str(random.randint(0, 9999)).zfill(4)

                if random_id not in Employee.used_ids:
                    Employee.used_ids.add(random_id)
                    self.employee_id = random_id
                    break
        else:
            self.employee_id = employee_id
            Employee.used_ids.add(employee_id)
            
    #Initialiser method