# ----------------------------
# TREE NODE (for Huffman tree)
# ----------------------------
class TreeNode:
    def __init__(self, ch, freq):
        self.ch = ch          # character stored in leaf node
        self.freq = freq      # frequency of this character
        self.left = None      # left child
        self.right = None     # right child


# ----------------------------
# LINKED LIST NODE (for priority queue)
# ----------------------------
class Node:
    def __init__(self, tree):
        self.tree = tree      # TreeNode stored in this linked list node
        self.next = None      # pointer to next node in queue


# ----------------------------
# HUFFMAN CLASS
# ----------------------------
class Huffman:
    def __init__(self):
        self.head = None      # head of linked list priority queue
        self.freq = [0] * 128 # frequency table for ASCII characters
        self.codes = {}       # dictionary to store final Huffman codes

    # ------------------------
    # RETRIEVE FILE + COUNT FREQUENCIES
    # ------------------------
    def retrieve(self, filename):
        try:
            with open(filename, "r") as f:
                text = f.read()
        except FileNotFoundError:
            print("File not found!")
            return

        # Count frequencies
        for ch in text:
            self.freq[ord(ch)] += 1

        # Create TreeNodes and enqueue into priority queue
        for i in range(128):
            if self.freq[i] > 0:
                tree_node = TreeNode(chr(i), self.freq[i])
                self.enqueue(Node(tree_node))

    # ------------------------
    # ENQUEUE (sorted insert)
    # ------------------------
    def enqueue(self, newNode):
        # CASE 1: emptynode/ insert at front (smaller than current head)
        if self.head is None or newNode.tree.freq < self.head.tree.freq:
            newNode.next = self.head
            self.head = newNode
            return

        # CASE 2: insert in middle or end
        p = self.head
        while p.next and p.next.tree.freq <= newNode.tree.freq:
            p = p.next
        newNode.next = p.next
        p.next = newNode

    # ------------------------
    # DEQUEUE (remove smallest frequency node)
    # ------------------------
    def dequeue(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        return temp.tree  # return TreeNode

    # ------------------------
    # BUILD HUFFMAN TREE
    # ------------------------
    def buildTree(self):
        # Keep combining until one node remains
        while self.head is not None and self.head.next is not None:
            left = self.dequeue()
            right = self.dequeue()

            # create new parent node
            parent = TreeNode('*', left.freq + right.freq)
            parent.left = left
            parent.right = right

            # enqueue parent back into priority queue
            self.enqueue(Node(parent))

        # The final node is the root
        return self.dequeue()

    # ------------------------
    # BUILD CODES (DFS traversal)
    # ------------------------
    def buildCodes(self, root, code=""):
        if root is None:
            return

        # Leaf node → store code
        if root.left is None and root.right is None:
            self.codes[root.ch] = code
            return

        # Go left → append '0'
        self.buildCodes(root.left, code + "0")
        # Go right → append '1'
        self.buildCodes(root.right, code + "1")

    # ------------------------
    # DISPLAY CODES
    # ------------------------
    def showCodes(self):
        print("\nCHAR\tCODE")
        for ch, code in self.codes.items():
            if ch == " ":
                print("SPACE\t", code)
            elif ch == "\n":
                print("\\n\t", code)
            else:
                print(f"{ch}\t{code}")


# ----------------------------
# MAIN
# ----------------------------
if __name__ == "__main__":
    h = Huffman()
    h.retrieve("input.txt")     # read file and build priority queue
    root = h.buildTree()        # construct Huffman tree
    h.buildCodes(root)          # generate codes for each character
    h.showCodes()               # display Huffman codes

