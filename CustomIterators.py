class CustomIterator:
    def __init__(self, max, jump):
        self.max = max
        self.jump = jump
        self.count = 0
        #self.curNum = 0

    def __iter__(self):
        #self.curNum = 0  # First value of the iterator needs to be set here and initialize it
        return self

    def __next__(self):
        if self.count >= self.max:
            raise StopIteration
        else:
            self.curNum = self.curNum + self.jump
            self.count += 1

        return self.curNum


myClass = CustomIterator(20, 4)
print(next(myClass))

print("For Loop from here")
for i in myClass:
    print(i)

