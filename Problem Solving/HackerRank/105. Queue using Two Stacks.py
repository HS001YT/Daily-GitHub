import sys

s1 = []  # stack for enqueue
s2 = []  # stack for dequeue / front

q = int(sys.stdin.readline())

for _ in range(q):
    query = sys.stdin.readline().split()
    t = int(query[0])

    # Enqueue
    if t == 1:
        x = int(query[1])
        s1.append(x)

    else:
        # Transfer only if needed
        if not s2:
            while s1:
                s2.append(s1.pop())

        # Dequeue
        if t == 2:
            if s2:
                s2.pop()

        # Print front
        elif t == 3:
            if s2:
                print(s2[-1])
