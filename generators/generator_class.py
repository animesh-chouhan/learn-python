class Gen:
    def __init__(self, n):
        self.n = n
        self.last = 0

    def __next__(self):
        if self.last >= self.n:
            raise StopIteration()

        ret = self.last ** 2
        self.last += 1
        return ret


gen = Gen(1000)

while True:
    try:
        print(next(gen))
    except StopIteration:
        break
