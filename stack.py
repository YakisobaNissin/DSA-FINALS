MAX = 5

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) >= MAX

    def push(self, item):
        if self.is_full():
            raise Exception("Stack Overflow: Stack is full.")
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack Underflow: Stack is empty.")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty. No top element.")
        return self.items[-1]

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return

        print("\nStack contents (top → bottom):")
        for item in reversed(self.items):
            print(item)
        print()


def menu():
    print("\nSTACK MENU")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    return input("\nSelect (1-5): ")


def main():
    stack = Stack()

    while True:
        try:
            choice = int(menu())
        except ValueError:
            print("Invalid input. Enter numbers only.")
            continue

        try:
            match choice:
                case 1:
                    value = input("Enter value to push: ")
                    stack.push(value)
                    print("Pushed successfully!")
                case 2:
                    removed = stack.pop()
                    print(f"Popped: {removed}")
                case 3:
                    print("Top element:", stack.peek())
                case 4:
                    stack.display()
                case 5:
                    print("Exiting program...")
                    break
                case _:
                    print("Invalid choice. Try again.")
        except Exception as err:
            print("Error:", err)

        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
