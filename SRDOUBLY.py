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
        self.filename = "Records.txt"
        self.retrieve()

    def addSorted(self, name, age):
        if self.locate(name):
            print("Duplicate found. Not added.")
            return

        newNode = Node(name, age)

        # Insert at head
        if self.head is None or name < self.head.name:
            newNode.next = self.head
            newNode.prev = None
            if self.head is None:
                self.head = self.tail = newNode
            else:
                self.head.prev = newNode
                self.head = newNode
            print("Added successfully.")
            return

        # Insert in middle or end
        p = self.head
        while p.next and name > p.next.name:
            p = p.next

        if p is self.tail:
            newNode.prev = self.tail
            newNode.next = None
            self.tail.next = newNode
            self.tail = newNode
        else:
            newNode.next = p.next
            newNode.prev = p
            p.next.prev = newNode
            p.next = newNode
        print("Added successfully.")

    def locate(self, name):
        p = self.head
        while p:
            if p.name == name:
                return p
            p = p.next
        return None

    def delete(self, name):
        node = self.locate(name)
        if not node:
            print("Name not found.")
            return False

        # Deleting head
        if node is self.head:
            self.head = self.head.next
            if self.head is None:  # List became empty
                self.tail = None
            else:
                self.head.prev = None

        # Deleting tail
        elif node is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

        # Deleting middle node
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        print("Deleted successfully.")
        return True

    def display(self):
        if self.head is None:
            print("Empty List")
            return
        print("{:<10} {:<10} {:<10}".format("Name", "Age", "Remarks"))
        p = self.head
        while p:
            print("{:<10} {:<10} {:<10}".format(
                p.name, p.age, "Adult" if p.age >= 18 else "Minor"
            ))
            p = p.next

    def save(self):
        with open(self.filename, "w") as file:
            p = self.head
            while p:
                file.write(f"{p.name},{p.age}\n")
                p = p.next

    def retrieve(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        name, age = line.split(",")
                        self.addSorted(name, int(age))
        except FileNotFoundError:
            pass


def menu():
    print("\n1. Add")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")
    return int(input("Choice (1-4): "))


def main():
    ll = List()
    while True:
        choice = menu()
        match choice:
            case 1:
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                ll.addSorted(name, age)
                ll.save()
            case 2:
                name = input("Enter Name to Delete: ")
                ll.delete(name)
                ll.save()
            case 3:
                ll.display()
            case 4:
                ll.save()
                break
            case _:
                print("Enter 1–4 only.")


if __name__ == "__main__":
    main()
