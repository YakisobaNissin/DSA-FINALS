MAX = 5

class CircularQueue:
    def __init__(self):
        self.queue = [None] * MAX
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % MAX == self.front

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue Overflow: Queue is full.")

        if self.is_empty():
            self.front = 0

        self.rear = (self.rear + 1) % MAX
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue Underflow: Queue is empty.")

        item = self.queue[self.front]

        # If it becomes empty after removing
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % MAX

        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty. No front element.")
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        print("\nQueue contents (front → rear):")
        i = self.front
        while True:
            print(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % MAX
        print()


def menu():
    print("\nCIRCULAR QUEUE MENU")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    return input("\nSelect (1-5): ")


def main():
    q = CircularQueue()

    while True:
        try:
            choice = int(menu())
        except ValueError:
            print("Invalid input. Enter numbers only.")
            continue

        try:
            match choice:
                case 1:
                    value = input("Enter value to enqueue: ")
                    q.enqueue(value)
                    print("Enqueued successfully!")
                case 2:
                    removed = q.dequeue()
                    print(f"Dequeued: {removed}")
                case 3:
                    print("Front element:", q.peek())
                case 4:
                    q.display()
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
