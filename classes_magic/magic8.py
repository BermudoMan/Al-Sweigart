# creation value tables 
class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0) -> None:
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step
    def __str__(self):
        return f'now: {self.value}'
    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration
    def __iter__(self):
        self.value = self.start - self.stop
        return self
    
class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5) -> None:
        self.fr = FRange(start, stop, step)
        self.rows = rows
    def __iter__(self):
        self.value_row = 0
        return self
    def __next__(self):
        if self.value_row < self.rows:
            self.value_row += 1
            return iter(self.fr)
        else:
            raise StopIteration

fr = FRange2D(0, 5, 0.5, 15)
for row in fr:
    for x in row:
        print(x, end=' ')
    print()