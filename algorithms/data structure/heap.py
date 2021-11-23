# max heap
# 1. 구현을 쉽게 하기 위해 배열의 첫 번째 인덱스 0은 사용 X
# 2. 부모 노드와 자식 노드의 관계
#     - 왼쪽 자식의 인덱스 = 부모 인덱스 * 2
#     - 오른쪽 자식의 인덱스 = 부모 인덱스 * 2 + 1
#     - 부모의 인덱스 = 자식의 인덱스 / 2

class MaxHeap:
    def __init__(self):
        self.data = [None]

    def __str__(self):
        return "".join(map(str, self.data[1:]))

    def insert(self, data):
        self.data.append(data)
        i = len(self.data) - 1

        while i > 1:
            if self.data[i] > self.data[i // 2]:
                self.data[i], self.data[i // 2] = self.data[i // 2], self.data[i]
                i = i // 2
            else:
                break

    def remove(self):
        max_value = self.data[1]
        self.data[1] = self.data[-1]
        del self.data[-1]

        i = 1

        while i * 2 + 1 < len(self.data):
            if self.data[i * 2] < self.data[i * 2 + 1]:
                child_index = i * 2 + 1
            else:
                child_index = i * 2

            if self.data[i] < self.data[child_index]:
                self.data[i], self.data[child_index] = self.data[child_index], self.data[i]
                i = child_index
            else:
                break

        return max_value

class MinHeap:
    def __init__(self):
        self.data = [None]

    def __str__(self):
        return "".join(map(str, self.data[1:]))

    def insert(self, data):
        self.data.append(data)
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
            if self.data[i * 2] > self.data[i * 2 + 1]:
                child_index = i * 2 + 1
            else:
                child_index = i * 2

            if self.data[i] > self.data[child_index]:
                self.data[i], self.data[child_index] = self.data[child_index], self.data[i]
                i = child_index
            else:
                break

        return min_value

arr = [7, 9, 4, 8, 6, 3]

max_heap = MaxHeap()
min_heap = MinHeap()

for num in arr:
    max_heap.insert(num)
    min_heap.insert(num)

print(max_heap)
print(min_heap)

print("Max Value : ", max_heap.remove())
print("Min Value : ", min_heap.remove())

print(max_heap)
print(min_heap)