class Array:

    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)

    def pop(self):
        if len(self.data) == 0:
            return None
        return self.data.pop()

    def get(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        return None

    def size(self):
        return len(self.data)

    def print(self):
        print(self.data)


if __name__ == "__main__":
    arr = Array()

    arr.append(10)
    arr.append(20)
    arr.append(30)

    arr.print()
    print(arr.get(1))
    print(arr.pop())
    arr.print()