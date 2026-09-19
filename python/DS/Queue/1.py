queue = []

queue.append(10)
queue.append(22)
queue.append(20)
queue.append(40)
 
 
print("Initial queue")
print(queue)



# dequeue  -> remove an element from the queue   -> index 0
queue.pop(0)

print("\nQueue after removing an element")
print(queue)


# front  -> get the first element of the queue   -> index 0
print("\nFront element of the queue")
print(queue[0])


# Rear -> get the last element of the queue   -> index -1
print("\nRear element of the queue")
print(queue[-1])

# add the element at the end of the queue
print("\nAdding an element to the queue")
# input
print("Enter the element to be added to the queue: ")
queue.append(int(input()))
print(queue)