from structure import Employee

class Operations:
    def insertEmployee(self, position):
        newEmployee = Employee(position)

        self.children.append(newEmployee)
        print(f"Employee added successfully. (ID: {Employee.Id})")
 
        return newEmployee
    
    # Method to insert employee

    def searchEmployee(self, employee_Id):
        if self.Id == employee_Id:
            return self
        
        for child in self.children:
            result = child.searchEmployee(employee_Id)

            if result:
                return result
            
        return None
    
    # Method to search for employee
    
    def updateEmployee(self, employee_Id, name=None, position=None):
        employee = self.searchEmployee(employee_Id)

        if employee is None:
            print(f"No employee found with ID {employee_Id}")
            return
        
        if name is not None:
            employee.name = name

        if position is not None:
            employee.position = position

        print(f"Employee added successfully (Employee ID {employee_Id})")

    # Method to update employee

    def delete_Employee(self, employee_Id):
        for child in self.children:
            if child.id == employee_Id:
                self.children.remove(child)

                print(f"Employee delted successfully (Employee ID {employee_Id})")
                return True
            
            deleted = child.deleteEmployee(employee_Id)

            if deleted:
                return True
            
        return False

    # Method to delete employee