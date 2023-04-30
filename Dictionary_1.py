employee_data = {
    'dept1': {
        'employee1': 50000,
        'employee2': 60000,
        'employee3': 4500000,
        'employee4': 55000
    },
    'dept2': {
        'employee1': 70000,
        'employee2': 800000,
        'employee3': 90000,
        'employee4': 100000
    },
    'dept3': {
        'employee1': 40000,
        'employee2': 550000,
        'employee3': 60000,
        'employee4': 45000
    }
}

# employee_data = {dep1,dep2,dep3}
# print(employee_data)

dep_max_salary={}
dep_min_salary={}
for dept,employee in employee_data.items():
    max_salary=min(employee.values())
    min_salary= max(employee.values())


    dep_max_salary[dept] = {max_salary}
    dep_min_salary[dept] = {min_salary}


print(dep_max_salary,dep_min_salary)

# print(employee_data)
# # Initialize dictionaries to store department-wise minimum and maximum salary
# dept_min_salary = {}
# dept_max_salary = {}

# # Iterate through the employee data dictionary
# for dept, employees in employee_data.items():
#     # Find the minimum and maximum salary for the current department
#     min_salary = min(employees.values())
#     max_salary = max(employees.values())
    
#     # Store the minimum and maximum salary in the department-wise dictionaries
#     dept_min_salary[dept] = min_salary
#     dept_max_salary[dept] = max_salary

# # Print the department-wise minimum and maximum salary
# print("Department-wise minimum salary:")
# print(dept_min_salary)
# print("\nDepartment-wise maximum salary:")
# print(dept_max_salary)

