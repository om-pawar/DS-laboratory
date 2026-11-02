# Experiment D3: Binary Search Tree (BST) Operations
# Problem: Implement insertion, deletion, search, and inorder display on a BST.

class Node:
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None

def insert(root, key):
    if not root:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if not root or root.key == key:
        return root is not None
    return search(root.left, key) if key < root.key else search(root.right, key)

def delete(root, key):
    if not root:
        return None
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        temp = root.right
        while temp.left:
            temp = temp.left
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root

def display(root):
    if root:
        display(root.left)
        print(root.key, end=" ")
        display(root.right)

if __name__ == "__main__":
    root = None
    for k in [50, 30, 70, 20, 40]:
        root = insert(root, k)

    print("BST Elements:", end=" ")
    display(root)
    print("\nSearch 30:", search(root, 30))
    root = delete(root, 30)
    print("After Deleting 30:", end=" ")
    display(root)
    print()
