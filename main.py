# Question: Employee management system
# 1. add employee
# 2. view all employees
# 4.delete employee
# 5. exit


emoloye = set()


def add_employee():
    name = input("Enter employee's name: ")
    emoloye.add(name)
    print("Employee added successfully!")


def view_employees():
    if not emoloye:
        print("No employees added yet \n")
        return
    print("Employee list:")
    for name in emoloye:
        print(name)


def delete_employee():
    name = input("Enter employee's name to delete: ")
    if name in emoloye:
        emoloye.remove(name)
        print("Employee deleted successfully!")
    else:
        print("Employee not found!")
        return


def main():
    while True:
        print("\n1. Add employee")
        print("2. View all employees")
        print("3. Delete employee")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_employee()
        elif choice == 2:
            view_employees()
        elif choice == 3:
            delete_employee()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice!")
            return


main()


