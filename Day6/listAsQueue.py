from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print("Queue: ", queue)
print("Pop the value from queue: ", queue.popleft())    # The first to arrive now leaves
print("Queue: ", queue)
queue.append("Terry")           # Terry arrives
print("New arrival: ", queue)
print("Queue: ", queue)
print("Pop the value from queue: ", queue.popleft())    # The second to arrive now leaves
print("Queue: ", queue)
