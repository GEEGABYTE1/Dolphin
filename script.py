from queue import Queue
from termcolor import colored




class FIFO:
    def __init__(self):
        data_vals = str(input(': '))
        data_vals = data_vals.split(',')
        self.data = []
        for character in data_vals:
            self.data.append(int(character))

        self.cache = Queue()
        self.history_queues = []
        self.histroy_vals = []

        self.fifo(self.data)

        
    def fifo(self, values):
        current_cache_vals = []
        for value in values:
            if cache.size == 4:
                self.histroy_queues.append(cache)
                self.history_vals.append(current_cache_vals)
                newcache = Queue()
                cache = newcache
                new_cache_vals = []
                current_cache_vals = new_cache_vals
            elif value in current_cache_vals:
                print(colored('HIT', 'cyan'))
                print('-'*24)
            else:
                print(colored('MISS', 'red'))
                print('-'*24)
            cache.enqueue(value)
            current_cache_vals.append(cache)

        return self.history_queues, self.history_vals
            
            
test = FIFO()
print(test())