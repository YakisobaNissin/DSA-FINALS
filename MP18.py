import json


class Node:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next = None
        self.prev = None


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.filename = "Records.json"
        self.retrieve()

    def addFront(self, name, age):
        newNode = Node(name, age)
        if self.head is None:
            self.head = self.tail = newNode
            return
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def addEnd(self, name, age):
        newNode = Node(name, age)
        if self.head is None:
            self.head = self.tail = newNode
            return
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode

    def addSort(self, name, age):
        newNode = Node(name, age)
        if self.head is None or name < self.head.name:
            self.addFront(name, age)
            return
        temp = self.head
        while temp.next and temp.next.name < name:
            temp = temp.next
        if temp == self.tail:
            self.addEnd(name, age)
            return
        newNode.next = temp.next
        newNode.prev = temp
        temp.next.prev = newNode
        temp.next = newNode

    def locate(self, name):
        p = self.head
        if not p:
            print("List is Empty")
            return None
        while p:
            if p.name == name:
                print("Name Found")
                return p
            p = p.next
        print("Name not Found")
        return None

    def delete(self, name):
        if not self.head:
            print("List Empty")
            return False
        if self.head.name == name:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            print("Name Deleted")
            return True
        temp = self.head
        while temp:
            if temp.name == name:
                if temp == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                print("Name Deleted")
                return True
            temp = temp.next
        print("Name not found")
        return False

    def display(self):
        if self.head is None:
            print("Empty List")
            return
        print("{:<10} {:<10} {:<10}".format("Name", "Age", "Remarks"))
        temp = self.head
        while temp:
            print("{:<10} {:<10} {:<10}".format(
                temp.name, temp.age, "Adult" if temp.age >= 18 else "Minor"
            ))
            temp = temp.next
        print("--------------------------\n")

    def save(self):
        temp = self.head
        records = []
        while temp:
            records.append({"name": temp.name, "age": temp.age})
            temp = temp.next
        with open(self.filename, "w") as file:
            json.dump(records, file, indent=2)
        print("saved")

    def retrieve(self):
        try:
            with open(self.filename, "r") as file:
                records = json.load(file)
                for rec in records:
                    self.addEnd(rec["name"], rec["age"])
        except FileNotFoundError:
            print("No Record Found")


def menu():
    print("1. Insert Front")
    print("2. Insert End")
    print("3. Insert Sorted")
    print("4. Search By Name")
    print("5. Delete By Name")
    print("6. Display Records")
    print("7. Exit")
    return int(input("Choice(1-7): "))


def main():
    ll = List()
    while True:
        match menu():
            case 1:
                ll.addFront(input("Enter Name: "), int(input("Enter Age: ")))
                ll.save()
            case 2:
                ll.addEnd(input("Enter Name: "), int(input("Enter Age: ")))
                ll.save()
            case 3:
                ll.addSort(input("Enter Name: "), int(input("Enter Age: ")))
                ll.save()
            case 4:
                ll.locate(input("Enter Name: "))
            case 5:
                ll.delete(input("Enter Name: "))
                ll.save()
            case 6:
                ll.display()
            case 7:
                ll.save()
                break
            case _:
                print("Enter 1–7 only")


if __name__ == "__main__":
    main()
