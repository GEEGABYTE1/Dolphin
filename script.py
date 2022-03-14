from queue import Queue


cache = Queue()

class FIFO:
    def __init__(self):
        data_vals = str(input(': '))
        data_vals = data_vals.split(',')
        self.data = []
        for character in data_vals:
            self.data.append(int(character))
        self.fifo(self.data)

        
    def fifo(self, values):
        for value in values:
            
            
