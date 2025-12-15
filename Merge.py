import os

class Node:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next = None

class ADTList:
    def __init__(self):
        self.head = None       # List 1 Head
        self.head2 = None      # List 2 Head (The "Second List")
        self.filename = "dos.txt"
        self.retrieve()

    # --- Standard Operations for List 1 ---
    def locate(self, name):
        p = self.head
        while p:
            if p.name == name:
                return p
            p = p.next
        return None

    def addSort(self, name, age):
        # Adds to self.head
        newNode = Node(name, age)
        if self.head is None or age > self.head.age:
            newNode.next = self.head
            self.head = newNode
            return
        p = self.head
        while p.next and age < p.next.age:
            p = p.next
        newNode.next = p.next
        p.next = newNode

    # --- NEW: Operations for List 2 ---
    def addSort2(self, name, age):
        # Adds to self.head2 (The Second List)
        newNode = Node(name, age)
        
        # 1. If List 2 is empty or new node is older than List 2 head
        if self.head2 is None or age > self.head2.age:
            newNode.next = self.head2
            self.head2 = newNode
            return
        
        # 2. Traverse List 2
        p = self.head2
        while p.next and age < p.next.age:
            p = p.next
            
        newNode.next = p.next
        p.next = newNode

    # --- MERGE Internal Lists ---
    def merge_lists(self):
        p1 = self.head
        p2 = self.head2

        if p2 is None:
            print("List 2 is empty. Nothing to merge.")
            return
        if p1 is None:
            self.head = p2
            self.head2 = None
            print("Merged List 2 into Empty List 1.")
            return

        # 1. Determine the new Global Head (Start of chain)
        if p1.age >= p2.age:
            self.head = p1
            p1 = p1.next
        else:
            self.head = p2
            p2 = p2.next

        # 2. 'current' tracks the end of the chain
        current = self.head

        # 3. Loop while both internal lists have nodes
        while p1 is not None and p2 is not None:
            if p1.age >= p2.age:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next

        # 4. Attach remainder
        if p1 is not None:
            current.next = p1
        elif p2 is not None:
            current.next = p2

        # 5. Important: Clear head2 so it doesn't exist separately anymore
        self.head2 = None
        print("Lists merged successfully!")

    # --- Utilities ---
    def deleteRec(self, name):
        if self.head is None:
            return
        if self.head.name == name:
            self.head = self.head.next
            return
        p = self.head
        while p.next and p.next.name != name:
            p = p.next
        if p.next:
            p.next = p.next.next

    def display(self):
        print("\n" + "="*45)
        print(f"{'Name':<15} {'Age':<10} {'List Source':<10}")
        print("-" * 45)
        
        # Display List 1
        p = self.head
        while p:
            print(f"{p.name:<15} {p.age:<10} {'Main List'}")
            p = p.next
            
        # Display List 2 (If it has items)
        if self.head2 is not None:
            print("-" * 45)
            q = self.head2
            while q:
                print(f"{q.name:<15} {q.age:<10} {'List 2 (Pending Merge)'}")
                q = q.next
        print("="*45 + "\n")

    def save(self):
        # Only saves the Main List (head)
        with open(self.filename, "w") as file:
            p = self.head
            while p:
                file.write(f"{p.name},{p.age}\n")
                p = p.next
    
    def retrieve(self):
        if not os.path.exists(self.filename): return
        with open(self.filename, "r") as file:
            self.head = None
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    self.addSort(parts[0], int(parts[1]))

# --- MAIN ---
def menu():
    print("1. Add to Main List")
    print("2. Add to SECOND List")
    print("3. Merge Second List into Main List")
    print("4. Display All")
    print("5. Delete from Main List")
    print("6. Save & Exit")
    return int(input("Choice: "))

def main():
    ll = ADTList()
    while True:
        try:
            match menu():
                case 1:
                    name = input("Enter name for MAIN: ")
                    age = int(input("Enter age: "))
                    ll.addSort(name, age)
                case 2:
                    name = input("Enter name for LIST 2: ")
                    age = int(input("Enter age: "))
                    ll.addSort2(name, age)
                case 3:
                    ll.merge_lists()
                case 4:
                    ll.display()
                case 5:
                    name = input("Enter name to delete: ")
                    ll.deleteRec(name)
                case 6:
                    ll.save()
                    break
                case _:
                    print("Invalid.")
        except ValueError:
            print("Enter a number.")

if __name__ == "__main__":
    main()