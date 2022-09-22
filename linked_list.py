# Linked list - linear data structure 
# Each element in the list is contained in a separate object called a Node 
# Node - contains individual item of the data and reference to the next node in the list  
# Head - first node in list 
# Tail - Last node in list 

# Nodes - are self referential objects - every node contains link to another node

# Singly Linked list - contains reference to next node in list 
# Doubly Linked List - contains reference to both the node previous and next node in the list 

# List traversal - moving from one node to another 


# Singly linked list 
class Node:
    """
    An object for storing a single node of a linked list 
    Models two attributes - data and the link to the next node in the list 
    """
    data = None
    next_node = None

    def __init__(self,data):
        self.data = data 

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    """
    Singly linked list 
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list 
        """
        current = self.head
        count = 0

        while current:
            count+=1
            current = current.next_node

        return count