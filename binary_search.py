def binary_search(lst, item):
    """
    It is Binary Search Algorithm
    The time complexity is O(log n)
    Binary search is an efficient algorithm for finding an item from a sorted list of items
    """
    low = 0
    high = len(lst)-1
    while low <= high:
        mid = (low+high)//2
        guess = lst[mid]
        if guess == item:
            return f'index of {item} is {mid}'
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

mylist=[1,3,5,7,9]

# print(binary_search(mylist,3))

class BinaryTreeNode:
    def __init__(self, value, parent=None):
        self.left = None
        self.right = None
        self.parent = parent
        self.value = value
        
    def find_node(self,value):
        node = self
        while node:
            if value == node.value:
                return node
            if value < node.value:
                node = node.left
            if value > node.value:
                node = node.right
        return None
    
    
    def insert_node(self, value):
        return self._insert_node(value, self)
    
    def _insert_node(self, value, parent_node):
        if value < parent_node.value:
            if parent_node.left is None:
                parent_node.left = BinaryTreeNode(value, parent_node)
            else:
                self._insert_node(value, parent_node.left)
        elif value > parent_node.value:
            if parent_node.right is None:
                parent_node.right = BinaryTreeNode(value, parent_node)
            else:
                self._insert_node(value, parent_node.right)
                
    
    def remove_node(self, value):
        return self._remove_node(value, self)
    
    def _remove_node(self, value, node):
        if node is None:
            return None
        
        if value < node.value:
            node.left = self._remove_node(value, node.left)
            return node
        elif value > node.value:
            node.right = self._remove_node(value, node.right)
            return node
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                original = node
                node = node.right
                while node.left:
                    node = node.left
                node.right = self._remove_node(node.value, original.right)
                node.left = original.left
                return node    
            
    
def traverse_recursive(node):
    if node is not None:
        print(f"node = {node.value}")
        traverse_recursive(node.left)
        traverse_recursive(node.right)

def traverse_with_stack(root):
    stack = []
    stack.append(root)
    while len(stack) > 0:
        current_node = stack.pop()
        print(f"node = {current_node.value}")
        if current_node.right is not None:
            stack.append(current_node.right)
        if current_node.left is not None:
            stack.append(current_node.left)

def traverse_with_queue(root):
    queue = []
    queue.append(root)
    while len(queue) > 0:
        current_node = queue.pop(0)
        print(f"node = {current_node.value}")
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
                    


# Step 1: Create the binary tree with a root node
root = BinaryTreeNode(10)

# Step 2: Insert nodes into the binary tree
root.insert_node(5)
root.insert_node(15)
root.insert_node(3)
root.insert_node(7)
root.insert_node(13)
root.insert_node(17)

# Step 3: Find a node
node = root.find_node(7)
if node:
    print(f"Node with value {node.value} found.")
else:
    print("Node not found.")

# Step 4: Remove a node
root.remove_node(5)
print(f'Node with value 5 removed.')

# Step 5: Traverse the tree using different methods
print("\nRecursive traversal:")
traverse_recursive(root)

print("\nTraversal with stack:")
traverse_with_stack(root)

print("\nTraversal with queue:")
traverse_with_queue(root)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    