class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Node:
    def __init__(self):
        self.root = None

    def preFix(self, n):
        if n is None:
            return
        print(n.data, end=" ")
        self.preFix(n.left)
        self.preFix(n.right)

    def inFix(self, n):
        if n is None:
            return
        self.inFix(n.left)
        print(n.data, end=" ")
        self.inFix(n.right)

    def postFix(self, n):
        if n is None:
            return
        self.postFix(n.left)
        self.postFix(n.right)
        print(n.data, end=" ")

    def buildTree(self):
        self.root = Tree("*")
        self.root.left = Tree("+")
        self.root.right = Tree("10")
        self.root.left.left = Tree("2")
        self.root.left.right = Tree("5")
        return self.root

    def evaluate(self, n):
        if n.left is None and n.right is None:
            return int(n.data)

        if n.data == "+":
            return self.evaluate(n.left) + self.evaluate(n.right)
        elif n.data == "-":
            return self.evaluate(n.left) - self.evaluate(n.right)
        elif n.data == "*":
            return self.evaluate(n.left) * self.evaluate(n.right)
        elif n.data == "/":
            return self.evaluate(n.left) // self.evaluate(n.right)

        return 0

    def levelOrder(self, n):
        if n is None:
            return

        class Lnode:
            def __init__(self, tnode):
                self.tnode = tnode
                self.next = None

        head = tail = Lnode(n)

        while head:
            d = head.tnode
            head = head.next
            if head is None:
                tail = None

            print(d.data, end=" ")

            if d.left:
                newNode = Lnode(d.left)
                if tail is None:
                    head = tail = newNode
                else:
                    tail.next = newNode
                    tail = newNode

            if d.right:
                newNode = Lnode(d.right)
                if tail is None:
                    head = tail = newNode
                else:
                    tail.next = newNode
                    tail = newNode


def main():
    t = Node()
    r = t.buildTree()

    print("PreFix: ", end="")
    t.preFix(r)

    print("\nInFix: ", end="")
    t.inFix(r)

    print("\nPostFix: ", end="")
    t.postFix(r)

    print("\nLevelOrder: ", end="")
    t.levelOrder(r)

    print("\nEvaluation:", t.evaluate(r))


if __name__ == "__main__":
    main()
