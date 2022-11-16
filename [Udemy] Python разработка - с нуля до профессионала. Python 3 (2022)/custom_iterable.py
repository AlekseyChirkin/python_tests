class TestRange:
    def __init__(self, start, end):
        self.start = start
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            val = self.current
            self.current += 1
            return val
        raise StopIteration


print(list(TestRange(0, 10)))
