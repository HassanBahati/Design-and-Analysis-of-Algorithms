# Linked list - linear data structure 
# Each element in the list is contained in a separate object called a Node 
# Node - contains individual item of the data and reference to the next node in the list  
# Head - first node in list 
# Tail - Last node in list 

# Nodes - are self referential objects - every node contains link to another node

# Singly Linked list - contains reference to next node in list 
# Doubly Linked List - contains reference to both the node previous and next node in the list 

# List traversal - moving from one node to another 

# Prepend - when data is added to the head of the linked list 
# Append - when data is added to the tail of the list  
# Insert - when data can be added to any point in the list 


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

    def add(self, data):
        """
        Adds a new node containing data at head of the list 
        Takes O(1) time 
        """
        new_node = Node(data)
        new_node.next_node = self.head

        self.head = new_node


    def search(self,key):
        """
        Search for the first node containing data that matches the key
        Return the node or None if not found 
        Takes O(n) time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None



    def insert(self,data,index):
        """
        Insert a new node containg data at index position
        Insertion takes O(1) time but finding the node at the insertion point takes O(n) time
        Overall O(n) time
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)
            
            position = index
            current = self.head
            
            while position > 1:
                current = new.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    

    def remove(self,key):
        current = self.head
        previous = None 
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found=True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                 previous = current
                 current = current.next_node



    def __repr__(self):
        """
        Returns a string representation of the list 
        Takes O(n) time 
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '-> '.join(nodes)




# python3 -i linked_list.py 
# >>> N1=Node(10)
# >>> N1
# >>> N2=Node(20)
# >>> N1.next_node=N2
# >>> N1.next_node
# <Node data: 20>


# python3 -i linked_list.py 
# >>> l = LinkedList()
# >>> N1=Node(10)
# >>> l.head=N1
# >>> l.size()

# >>> l=LinkedList()
# >>> l.add(1)
# >>> l.size()
# 1
# >>> l.add(2)
# >>> l.add(3)
# >>> l.size()
# 3
# >>> 

# >>> l=LinkedList()
# >>> l.add(1)
# >>> l.add(2)
# >>> l.add(3)
# >>> l
# [Head: 3]-> [2]-> [Tail: 1]


# >>> l=LinkedList()
# >>> l.add(19)
# >>> l.add(2)
# >>> l.add(45)
# >>> l.add(15)
# >>> n=l.search(45)
# >>> n
# <Node data: 45>
# >>> l
# [Head: 15]-> [45]-> [2]-> [Tail: 19]