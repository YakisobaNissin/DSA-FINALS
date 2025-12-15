import os

MAX = 5

# =======================
#   QUICKSORT FUNCTIONS
# =======================

def quicksort_by_name(records):
    if len(records) <= 1:
        return records
    pivot = records[len(records) // 2]["name"]
    left  = [r for r in records if r["name"] < pivot]
    mid   = [r for r in records if r["name"] == pivot]
    right = [r for r in records if r["name"] > pivot]
    return quicksort_by_name(left) + mid + quicksort_by_name(right)

def quicksort_by_age(records):
    if len(records) <= 1:
        return records
    pivot = records[len(records) // 2]["age"]
    left  = [r for r in records if r["age"] < pivot]
    mid   = [r for r in records if r["age"] == pivot]
    right = [r for r in records if r["age"] > pivot]
    return quicksort_by_age(left) + mid + quicksort_by_age(right)


# =======================
#   PERSON RECORD CLASS
# =======================

class PersonR:
    def __init__(self, filename="persons.txt"):
        self.records = []
        self.filename = filename
        self.load_records()

    def find_record(self, name):
        for i, rec in enumerate(self.records):
            if rec["name"] == name:
                return i
        return -1

    def is_full(self):
        return len(self.records) >= MAX

    def append_record(self, name, age):
        if self.is_full():
            print("List full.")
        elif self.find_record(name) != -1:
            print("Duplicate found.")
        else:
            self.records.append({"name": name, "age": int(age)})
            print("Record added.")
            self.save_records()

    def update_record(self, name, age):
        i = self.find_record(name)
        if i == -1:
            print("Record not found.")
        else:
            self.records[i]["age"] = int(age)
            print("Updated!")
            self.save_records()

    def delete_record(self, name):
        i = self.find_record(name)
        if i == -1:
            print("Record not found.")
        else:
            del self.records[i]
            print("Deleted!")
            self.save_records()

    def display_records(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nPerson List:")
        for rec in self.records:
            print(f"{rec['name']} - {rec['age']}")
        input("\nPress Enter to continue...")

    def sort_by_name(self):
        self.records = quicksort_by_name(self.records)
        print("Sorted by Name!")
        self.save_records()

    def sort_by_age(self):
        self.records = quicksort_by_age(self.records)
        print("Sorted by Age!")
        self.save_records()

    def save_records(self):
        with open(self.filename, 'w') as file:
            for rec in self.records:
                file.write(f"{rec['name']},{rec['age']}\n")

    def load_records(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 2:
                        name, age = parts
                        self.records.append({"name": name, "age": int(age)})
        except FileNotFoundError:
            print("No record found.")


# =======================
#   MENU
# =======================

def menu():
    print("\nPerson Record MENU")
    print("1. Add Record")
    print("2. Update Record")
    print("3. Delete Record")
    print("4. Display Records")
    print("5. Sort Records by Name")
    print("6. Sort Records by Age")
    print("7. Exit")
    return input("\nSelect (1-7): ")


# =======================
#   MAIN
# =======================

def main():
    records = PersonR()
    while True:
        try:
            choice = int(menu())
        except ValueError:
            print("Invalid input.")
            continue

        match choice:
            case 1:
                name = input("Enter Person Name: ")
                age = input("Enter Age: ")
                records.append_record(name, age)
                input("Press enter to continue")
            case 2:
                name = input("Enter Person Name to update: ")
                age = input("Enter New Age: ")
                records.update_record(name, age)
                input("Press enter to continue")
            case 3:
                name = input("Enter Person Name to delete: ")
                records.delete_record(name)
                input("Press enter to continue")
            case 4:
                records.display_records()
            case 5:
                records.sort_by_name()
                input("Press enter to continue")
            case 6:
                records.sort_by_age()
                input("Press enter to continue")
            case 7:
                records.save_records()
                break
            case _:
                print("Wrong input")
                input("Press enter to continue")


if __name__ == "__main__":
    main()
