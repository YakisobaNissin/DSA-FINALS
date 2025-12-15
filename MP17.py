class Node:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.filename = "List.txt"
        self.retrieve()
    
    def addFront(self,name, age):
        newNode = Node(name, age)
        newNode.next = self.head 
        self.head = newNode
    def addEnd(self,name,age):
        newNode = Node(name, age)
        if self.head == None:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode
    def addSort(self,name,age):
        newNode = Node(name, age)

        if self.head == None or name < self.head.name:
            newNode.next = self.head
            self.head = newNode
            return
        
        temp = self.head
        while temp.next and temp.next.name < name:
            temp = temp.next
        newNode.next = temp.next
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
            self.head = self.head.next
            print("name Deleted")
            return True
        temp = self.head
        while temp.next:
            if temp.next.name == name:
                temp.next = temp.next.next
                print("Name Deleted")
                return True
            temp = temp.next
        print("Name not found")
        return False

    def display(self):
        if self.head is None:
            print("Empty List")
            return
        print("{:<10} {:<10} {:<10}".format("Name","Age","Remarks"))
        temp = self.head
        while temp:
            print("{:<10} {:<10} {:<10}".format(temp.name, temp.age, "Adult" if temp.age >= 18 else "Minor")) 
            temp = temp.next
        print("--------------------------\n")

    def save(self):
        with open(self.filename, "w") as file:
            temp = self.head
            while temp:
                file.write(f"{temp.name},{temp.age}\n")
                temp = temp.next
        print("saved")

    def retrieve(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    name, age = line.strip().split(",")
                    self.addEnd(name.strip(), int(age))
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
    ll =List()

    while True:
        match menu():
            case 1:
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                ll.addFront(name,age)
                ll.save()
            case 2:
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                ll.addEnd(name,age)
                ll.save()
            case 3:
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                ll.addSort(name,age)
                ll.save()
            case 4:
                name = input("Enter Name: ")
                ll.locate(name)
            case 5:
                name = input("Enter Name: ")
                ll.delete(name)
                ll.save()
            case 6:
                ll.display()
            case 7:
                ll.save()
                break
            case _:
                print("Print Enter 1-7 only")

if __name__ == "__main__":
    main()

        




        

