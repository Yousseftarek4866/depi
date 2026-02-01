# --- Hospital Management System ---

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def view_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Patient(Person):
    def __init__(self, name, age, medical_record):
        super().__init__(name, age)
        self.medical_record = medical_record

    def view_record(self):
        return f"Patient: {self.name} | Record: {self.medical_record}"

class Staff(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def view_info(self):
        return f"Staff: {self.name} | Position: {self.position} | Age: {self.age}"

class Department:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.staff_members = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_staff(self, staff_member):
        self.staff_members.append(staff_member)

class Hospital:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

# --- Interactive System Interface ---

def main():
    print("--- Welcome to the Hospital Management System ---")
    h_name = input("Enter Hospital Name: ")
    h_loc = input("Enter Hospital Location: ")
    my_hospital = Hospital(h_name, h_loc)

    while True:
        print(f"\n--- {my_hospital.name} Management Menu ---")
        print("1. Add Department")
        print("2. Add Staff to Department")
        print("3. Add Patient to Department")
        print("4. View Hospital Stats")
        print("5. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            dep_name = input("Enter Department Name: ")
            new_dep = Department(dep_name)
            my_hospital.add_department(new_dep)
            print(f"Department '{dep_name}' created!")

        elif choice == '2':
            if not my_hospital.departments:
                print("Error: Create a department first!")
                continue
            print("Select Department:")
            for i, d in enumerate(my_hospital.departments):
                print(f"{i}. {d.name}")
            idx = int(input("Index: "))
            name = input("Staff Name: ")
            age = input("Staff Age: ")
            pos = input("Position (e.g. Doctor/Nurse): ")
            my_hospital.departments[idx].add_staff(Staff(name, age, pos))
            print("Staff added successfully.")

        elif choice == '3':
            if not my_hospital.departments:
                print("Error: Create a department first!")
                continue
            print("Select Department:")
            for i, d in enumerate(my_hospital.departments):
                print(f"{i}. {d.name}")
            idx = int(input("Index: "))
            name = input("Patient Name: ")
            age = input("Patient Age: ")
            record = input("Medical Condition: ")
            my_hospital.departments[idx].add_patient(Patient(name, age, record))
            print("Patient registered.")

        elif choice == '4':
            print(f"\nHospital: {my_hospital.name} | Location: {my_hospital.location}")
            for d in my_hospital.departments:
                print(f"\nDepartment: {d.name}")
                print(f"  Staff count: {len(d.staff_members)}")
                print(f"  Patient count: {len(d.patients)}")
                for s in d.staff_members: print(f"    - {s.view_info()}")
                for p in d.patients: print(f"    - {p.view_record()}")

        elif choice == '5':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()