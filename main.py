employees = []

while True:

    print("\n========== Employee Management System ==========")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Employee
    if choice == "1":

        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        age = input("Enter Employee Age: ")
        department = input("Enter Department: ")
        designation = input("Enter Designation: ")
        salary = input("Enter Salary: ")

        employee = {
            "id": emp_id,
            "name": name,
            "age": age,
            "department": department,
            "designation": designation,
            "salary": salary
        }

        employees.append(employee)

        print("\n✅ Employee added successfully!")

    # View Employees
    elif choice == "2":

        if len(employees) == 0:
            print("\nNo employee records found.")

        else:
            print("\n========== Employee List ==========")

            for emp in employees:
                print("--------------------------------")
                print("Employee ID :", emp["id"])
                print("Name        :", emp["name"])
                print("Age         :", emp["age"])
                print("Department  :", emp["department"])
                print("Designation :", emp["designation"])
                print("Salary      :", emp["salary"])

    # Search Employee
    elif choice == "3":

        search = input("Enter Employee ID to search: ")

        found = False

        for emp in employees:

            if emp["id"] == search:

                print("\nEmployee Found")
                print("--------------------------------")
                print("Employee ID :", emp["id"])
                print("Name        :", emp["name"])
                print("Age         :", emp["age"])
                print("Department  :", emp["department"])
                print("Designation :", emp["designation"])
                print("Salary      :", emp["salary"])

                found = True
                break

        if not found:
            print("\nEmployee not found.")

    # Update Employee
    elif choice == "4":

        update_id = input("Enter Employee ID to update: ")

        found = False

        for emp in employees:

            if emp["id"] == update_id:

                emp["name"] = input("Enter New Name: ")
                emp["age"] = input("Enter New Age: ")
                emp["department"] = input("Enter New Department: ")
                emp["designation"] = input("Enter New Designation: ")
                emp["salary"] = input("Enter New Salary: ")

                print("\nEmployee updated successfully!")

                found = True
                break

        if not found:
            print("\nEmployee not found.")

    # Delete Employee
    elif choice == "5":

        delete_id = input("Enter Employee ID to delete: ")

        found = False

        for emp in employees:

            if emp["id"] == delete_id:

                employees.remove(emp)

                print("\nEmployee deleted successfully!")

                found = True
                break

        if not found:
            print("\nEmployee not found.")

    # Exit
    elif choice == "6":

        print("\nThank you for using Employee Management System.")
        break

    else:

        print("\nInvalid choice. Please try again.")