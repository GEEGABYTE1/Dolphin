from cache import Cache, Node
from termcolor import colored





class FIFO:
    def __init__(self):
        data_vals = str(input(': '))
        data_vals = data_vals.split(',')
        self.data = []
        for character in data_vals:
            self.data.append(int(character))

        self.cache = Cache()
        self.history_queues = []
        self.history_vals = []

        result = self.fifo(self.data)
        print(result)

        
    def fifo(self, values):
        current_cache_vals = []
        index = 0
        for value in values:

            if value in current_cache_vals:
                print(colored('HIT', 'cyan'))
                print('-'*24)
            else:
                print(colored('MISS', 'red'))
                print('-'*24)
            
            if index >= 4:
                index = 0
                self.cache_size = 0

            if self.cache.size >= 4:
                if self.cache.size == 4:
                    new_node = Node(value)
                    new_node.set_link(self.cache.head_node)
                    self.cache.head_node = new_node
                else:
                    current_node = self.cache.head_node
                    counter = 0 
                    while counter != index:
                        if current_node.get_value() == value:
                            current_node.value = value 
                            break
                        else:
                            current_node = current_node.get_link()
                            counter += 1
                    self.cache.size += 1
                    current_cache_vals[index] = value   
            else:          
                current_cache_vals.append(value)
                
            
            self.cache.enqueue(value)
            index += 1

        return self.history_queues, self.history_vals
            
            
test = FIFO()
print(test())