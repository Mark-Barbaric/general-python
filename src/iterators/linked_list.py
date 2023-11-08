class LinkedList:
    def __init__(self, lst):
        self.numbers=lst

    def __iter__(self):
        self.pos=0
        return self

    def __next__(self):
        if(self.pos < len(self.numbers)):
            self.pos += 1
            return self.numbers[self.pos - 1]
        else:
            raise StopIteration