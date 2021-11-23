class MinHeap:
    def __init__(self):
        self.data = [None]

    def insert(self, num):
        self.data.append(num)
        i = len(self.data) - 1

        while i > 1:
            if self.data[i] < self.data[i // 2]:
                self.data[i], self.data[i // 2] = self.data[i // 2], self.data[i]
                i = i // 2
            else:
                break

    def remove(self):
        min_value = self.data[1]
        self.data[1] = self.data[-1]
        del self.data[-1]
        i = 1

        while i * 2 + 1 < len(self.data):
            if self.data[i * 2] < self.data[i * 2 + 1]:
                child_i = i * 2
            else:
                child_i = i * 2 + 1

            if self.data[i] > self.data[child_i]:
                self.data[i], self.data[child_i] = self.data[child_i], self.data[i]
            else:
                break

        return min_value

N, K = [int(n) for n in input().split(" ")]
arr = [int(n) for n in input().split(" ")]

min_heap = MinHeap()
for i in arr:
    min_heap.insert(i)

for _ in range(K - 1):
    min_heap.remove()

print(min_heap.remove())