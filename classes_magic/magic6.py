# iterations

# a = iter(range(5))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

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

fr = FRange(0, 4, 0.5)
print(fr)
print(fr.__next__())
print(fr.__next__())
print(next(fr))
print(fr)
print(next(fr))
print(next(fr))
print(next(fr))
print(fr)

# In this case code "for x in fr: .... " - will not work. Iter does not exist for FRange class 