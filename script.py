from threading import currentThread
from cache import Cache, Node
from termcolor import colored
import random





class FIFO:                                         # FIFO 
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
                print(current_cache_vals)
                print('-'*24)
                continue
            elif len(current_cache_vals) != 0:
                print(colored('MISS', 'red'))
                
            
            if index >= 4:
                index = 0
                
                

            if self.cache.size >= 4:
                if self.cache.size == 4:
                    new_node = Node(value)
                    prev_node = self.cache.head_node.get_link()
                    self.cache.head_node = new_node
                    new_node.set_link(prev_node)
                else:
                    current_node = self.cache.head_node
                    counter = 0
                    
                    while current_node.get_value() != None:
                        if counter == index:
                            current_node.value = value 
                            break
                        else:
                            current_node = current_node.get_link()
                            counter += 1
                            
                self.cache.size += 1
                       
            else:          
                current_cache_vals.append(value)
                
                self.cache.enqueue(value)
            
            print(current_cache_vals)
            print('-'*24)
            current_cache_vals[index] = value
            index += 1

        return self.history_queues, self.history_vals


class two_way:                          #FIFO Two-Way
    def __init__(self):
        data_vals = str(input(': '))
        data_vals = data_vals.split(',')
        self.data = []
        for character in data_vals:
            self.data.append(int(character))

        result = self.two_way(self.data)
        print(result)

    def two_way(self, data):        #n-way (2)
        set0 = Cache()
        set1 = Cache()

        set_0_vals = []
        set_1_vals = []
        index0 = 0
        index1 = 0
        
        for value in data:
            if value % 2 == 0:

                if value not in set_0_vals:
                    print(colored('MISS', 'red'))
                    
                    
                    
                else:
                    print(colored('HIT', 'green'))
                    string = str(set_0_vals) + ' ' +  str(set_1_vals)
                    print(string)
                    print('-'*24)
                    
                    continue 

                if index0 >= 2:
                    index0 = 0 
                if set0.size >= 2:
                    counter = 0 
                    current_node = set0.head_node 
                    while current_node:
                        if counter == index0:
                            current_node.value = value 
                            break 
                        else:
                            counter += 1
                    set_0_vals[index0] = value
                else:
                    set_0_vals.append(value)
                    set0.enqueue(value)

                
                index0 += 1
                string = str(set_0_vals) + ' ' +  str(set_1_vals)
                print(string)
                print('-'*24)
            else:
                if value not in set_1_vals:
                    print(colored('MISS', 'red'))
                    
                    
                    
                else:
                    print(colored('HIT', 'green'))
                    string = str(set_0_vals) + ' ' +  str(set_1_vals)
                    print(string)
                    print('-'*24)
                    continue 

                if index1 >= 2:
                    index1 = 0 
                if set1.size >= 2:
                    counter = 0 
                    current_node = set1.head_node
                    while current_node:
                        if counter == index1:
                            current_node.value = value 
                            break 
                        else:
                            counter += 1
                    set_1_vals[index1] = value
                else:
                    set_1_vals.append(value)
                    set1.enqueue(value)
            
                
                index1 += 1
                string = str(set_0_vals) + ' ' +  str(set_1_vals)
                print(string)
                print('-'*24)
        
        return set0, set1

class Random:
    # Full associative with Random Replacement
    def __init__(self):
        data_vals = str(input(': '))
        data_vals = data_vals.split(',')
        self.data = []
        for character in data_vals:
            self.data.append(int(character))

        result = self.random(self.data)
        print(result)
    
    def random(self, data):
        cache = Cache()
        cache_vals = [None for i in range(4)]
        for value in range(4):
            cache.enqueue(None)
        
        for value in data:
            random_idx = random.randint(0, 3)
            current_node = cache.head_node 
            counter = 0
            if value in cache_vals:
                print(colored('HIT', 'cyan'))
                print(cache_vals)
                print('-'*24)
                continue 
            else:
                print(colored('MISS', 'red'))
            current_node = cache.head_node
            counter = 0 
            while current_node:
                if counter == random_idx:
                    current_node.value = value 
                    break
                else:
                    counter += 1
                    current_node = current_node.get_link()
            
            cache_vals[random_idx] = value
            print(cache_vals)
            print('-'*24)
            
        return cache_vals

                
test = Random()
print(test)
        


        
            

                
                
                
            

        


test = two_way()
print(test)