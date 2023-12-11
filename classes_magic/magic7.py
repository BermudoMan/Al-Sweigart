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

fr = FRange(0, 5, 0.5)
i = iter(fr)
print(next(i))
print(i)
print(next(i))
print(i)
print(next(i))
print(i)

for it in iter(fr):
    print(it)