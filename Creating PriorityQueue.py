from queue import PriorityQueue



# Step 1: Create a Priority Queue

my_priority_queue = PriorityQueue()



# Step 2: Add elements to the Priority Queue

for priority, data in [

  (3, "Priority 3"),

  (1, "Priority 1"),

  (2, "Priority 2"),

]:

  my_priority_queue.put((priority, data))



# Step 3: Pop an element from the Priority Queue

popped_element = my_priority_queue.get()



# Step 4: Show the Output

print(f"Popped element from the priority queue: {popped_element}")



# Additional Step: Print the remaining elements in the Priority Queue

remaining_elements = list(my_priority_queue.queue)

print(f"Remaining elements in the priority queue: {remaining_elements}")



Output:

Popped element from the priority queue: (1, 'Priority 1')

Remaining elements in the priority queue: [(2, 'Priority 2'), (3, 'Priority 3')]

