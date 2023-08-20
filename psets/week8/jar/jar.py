class Jar:
    def __init__(self, capacity=12):
        self.cookie = "🍪"
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return f"{self.size*self.cookie}"

    def deposit(self, n):
        if n < 0:
            raise ValueError
        self.size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:  # or capacity > 12:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0 or size > self.capacity:
            raise ValueError
        self._size = size


def main():
    jar = Jar(50)
    print(jar.capacity)
    print(jar)
    jar.deposit(5)
    print(jar)


if __name__ == "__main__":
    main()
