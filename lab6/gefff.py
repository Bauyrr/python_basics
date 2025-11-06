def bubble_up(heap, i):
    """Move element at index i up to restore max-heap property."""
    while i > 0:
        parent = (i - 1) // 2
        if heap[i] > heap[parent]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break
    return i + 1  


n, q = map(int, input().split())
heap = list(map(int, input().split()))

for _ in range(q):
    i, r = map(int, input().split())
    i -= 1  
    heap[i] += r
    new_pos = bubble_up(heap, i)
    print(new_pos)

print(*heap)