class Node:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        # Children are stored as a dictionary of directions mapping to another dictionary of angles LOL funny to say outloud
        self.children = {}
    
    def add_child(self, direction, angle, child_node):
        # Ensure the direction exists in the children dictionary
        if direction not in self.children:
            self.children[direction] = {}
        # Add the child node at the specified angle
        self.children[direction][angle] = child_node

    def get_child(self, direction, angle):
        # Safely retrieve the child node by direction and angle
        return self.children.get(direction, {}).get(angle, None)

    def __repr__(self):
        return f"Node({self.name}, value={self.value})"


# Example Usage:
root = Node("Root")

# Adding child nodes
child_1 = Node("Child1", value=10)
child_2 = Node("Child2", value=20)
grandchild_1 = Node("GrandChild1", value=30)

# Add children to root with direction and angle
root.add_child("up", 45, child_1)
root.add_child("down", 90, child_2)

# Add a grandchild to child_1
child_1.add_child("right", 30, grandchild_1)

# Retrieve nodes
retrieved_child = root.get_child("up", 45)
retrieved_grandchild = child_1.get_child("right", 30)

print(f"Retrieved Child: {retrieved_child}")
print(f"Retrieved Grandchild: {retrieved_grandchild}")