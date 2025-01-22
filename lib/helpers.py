from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input("Enter Employee's Name: ")
    if employee := Employee.find_by_name(name):
        print(f"Success: {employee}")
    else:
        print(f"Employee name: {name} can not find!")


def find_employee_by_id():
    id_ = int(input("Enet Employee's Id: "))
    if employee := Employee.find_by_id(id_):
        print(f"Success : {employee}")
    else:
        print(f"id:{id_} not found!!!!")


def create_employee():
    name = input("Enter Employee's Name: ")
    job_title = input("Enter Job Title: ")
    department_id = int(input("Enter Department's Id: "))
    try:
        employee = Employee.create(name,job_title,department_id)
        print(f"Success : {employee}")
    except Exception as exc:
        print(f"Error Creatint Employee!",exc)


def update_employee():
    id_=int(input("Enter Employee;s Id: "))
    if employee := Employee.find_by_id(id_):
        try:
            name = input("Enter New Name: ")
            job_title = input("Enter New Job Title: ")
            department_id = int(input("Enter Department's Id: "))
            employee.name = name
            employee.job_title = job_title
            employee.department_id = department_id
            employee.update()
            print(f"Success: {employee}")
        except Exception as exc:
            print(f"Error Updating: {employee}")
    else:
        print(f"id:{id_} can not find")


def delete_employee():
    id_ = int(input("Enter Employee's Id: "))
    if employee := Employee.find_by_id(id_):
        Employee.delete(employee)
        print(f"Deleted: {employee}")
    else:
        print(f"id:{id_} not Found")


def list_department_employees():
    department_id = int(input("Enter Department's Id: "))
    if department := Department.find_by_id(department_id):
        employees = department.employees()
        for employee in employees:
            print(employee)
    else:
        print(f"can not find id: {department_id}")