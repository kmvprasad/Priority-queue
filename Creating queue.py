from queue import Queue



# Create a Queue object

q = Queue()



# Add an element to the queue

q.put("This is the first element")



# Print the size of the queue

print(f"Queue size: {q.qsize()}")



# Pop an element from the queue

first_element = q.get()



# Print the popped element

print(f"Popped element: {first_element}")



# Print the size of the queue

print(f"Queue size after popping: {q.qsize()}")



# Check if the queue is empty

if q.empty():

  print("The queue is empty")

else:

  print("The queue is not empty")