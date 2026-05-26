from structure import Employee

class Operations:
    def __init__(self, root=None):
        self.root = root
    
    # Initializer method

    def insert_employee(self, name, position, manager_id=None):
        if self.root is None:
            self.root = Employee(name, position)

            return self.root
        
        # Inserting head employee
        
        manager = self.search_employee(manager_id)

        if manager is None:
            print("Manager not found")
            return
        
        # Checking for manager
        
        employee = Employee(name, position, manager)

        manager.children.append(employee)

        return employee
 
    # Method to insert employee

    def search_employee(self, employee_id):
        if self.root is None:
            return None
        
        if self.root.employee_id == employee_id:
            return self.root
        
        stack = [self.root]

        while stack:
            current = stack.pop()

            for child in current.children:
                if child.employee_id == employee_id:
                    return child

                stack.append(child)

        return None    
    
    # Method to search for employee
    
    def update_employee(self, employee_id, name=None, position=None):
        employee = self.search_employee(employee_id)

        if employee is None:
            print(f"No employee found with ID {employee_id}")
            return
        
        if name is not None:
            employee.name = name

        if position is not None:
            employee.position = position

        print(f"Employee updated successfully (Employee ID {employee_id})")

    # Method to update employee

    def delete_employee(self, employee_id):
        if self.root is None:
            return None
        
        if self.root.employee_id == employee_id:
            print("Cannot delete root emplyoee")
            return False
        
        stack = [self.root]

        while stack:
            current = stack.pop()

            for child in current.children:
                if child.employee_id == employee_id:
                    current.children.remove(child)
                    return True
                
                stack.append(child)

        return False


    # Method to delete employee