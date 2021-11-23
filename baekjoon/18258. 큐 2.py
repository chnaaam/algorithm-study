import sys
from collections import deque

class Queue():
    def __init__(self):
        self.q = deque()

    def push(self, data):
        self.q.append(data)

    def pop(self):
        if self.q:
            return self.q.popleft()
        else:
            return -1

    def size(self):
        return len(self.q)

    def empty(self):
        if self.q:
            return 0
        else:
            return 1

    def front(self):
        if self.q:
            return self.q[0]
        else:
            return -1

    def back(self):
        if self.q:
            return self.q[-1]
        else:
            return -1


q = Queue()
N = int(sys.stdin.readline())

for _ in range(N):
    command = sys.stdin.readline()

    if command.startswith("push"):
        q.push(int(command.split(" ")[1]))
    elif command.startswith("pop"):
        print(q.pop())
    elif command.startswith("size"):
        print(q.size())
    elif command.startswith("empty"):
        print(q.empty())
    elif command.startswith("front"):
        print(q.front())
    else:
        print(q.back())