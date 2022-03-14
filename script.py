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
            
            if index >= 4:
                index = 0

            if self.cache.size == 4:
                new_node = Node(value)
                new_node.set_link(self.cache.head_node)
                self.cache.head_node = new_node
                self.cache.size += 1
                current_cache_vals[index] = value
                
                
            if value in current_cache_vals:
                print(colored('HIT', 'cyan'))
                print('-'*24)
            else:
                print(colored('MISS', 'red'))
                print('-'*24)
            self.cache.enqueue(value)
            current_cache_vals.append(value)
            index += 1

        return self.history_queues, self.history_vals
            
            
test = FIFO()
print(test())