class Node:
    def __init__(self, name, value=None):
        self.name = name #key
        self.value = value #value pairs
        # Children are stored as a dictionary of directions mapping to another dictionary of angles LOL funny to say outloud
        self.children = {}
                    #{name , its value}
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
root.add_child("up", 45, child_1)  #this already holds the node itself, AKA the name its value, all its doing is giving itself a place in 4D so direction and angle.
root.add_child("down", 90, child_2) # -Y , 90 degrees | child2, 30

# Add a grandchild to child_1
child_1.add_child("right", 22.5, grandchild_1) # here were making a grandchild of the child, saying that from the negative Y direction which is already implicitly known that its 90 degrees from the origin in relation to the axis of the other node brances. add a child and place it to the right of that node pointer. now give it a degrees of, we can divided larger angles to smaller ones which is an implicit child angle of the parent

# Retrieve nodes
retrieved_child = root.get_child("up", 45) 
retrieved_grandchild = child_1.get_child("right", 30) 

print(f"Retrieved Child: {retrieved_child}")
print(f"Retrieved Grandchild: {retrieved_grandchild}")