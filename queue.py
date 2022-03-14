class Node:
            def __init__(self, value, link=None):
                self.value = value 
                self.link = link 

            def get_value(self):
                return self.value 

            def get_link(self):
                return self.link 

            def set_link(self, new_link):
                self.link = new_link 

class Queue:
    def __init__(self, limit=None):
        self.limit = limit 
        self.size = 0
        self.head_node = None 
        self.tail_node = None 

    def is_empty(self):
        if self.size == 0:
            return True 

    def has_space(self):
        if self.limit == None:
            return True 
        else:
            if self.limit > self.size:
                return True 

    def peek(self):
        if not self.is_empty():
            return self.head_node.get_value()
        else:
            print("The Queue Is Empty")
    
    def enqueue(self, new_value):
        if self.has_space():
            new_node = Node(new_value)
            if self.size == 0:
                self.head_node = new_node 
                self.tail_node = new_node 
            else:
                self.tail_node.set_link(new_node)
                self.tail_node = new_node 
            self.size += 1
        else:
            print("The Queue Is Full")

    def dequeue(self):
        if not self.is_empty():
            item_to_remove = self.head_node
            if self.size == 1:
                self.head_node = None 
                self.tail_node = None 
            else:
                self.head_node = item_to_remove.get_link()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("The Queue Is Empty")
