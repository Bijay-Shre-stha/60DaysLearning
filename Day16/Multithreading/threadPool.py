import concurrent.futures
import time

# Define a simple function to simulate a time-consuming task
def task(n):
    print(f"Task {n} started")
    time.sleep(2)
    result = n * n
    print(f"Task {n} completed with result {result}\n")
    return result

# Create a ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # List of tasks to execute
    tasks = [1, 2, 3, 4, 5]
    
    # Submit tasks to the thread pool
    future_to_task = {executor.submit(task, n): n for n in tasks}

    # Retrieve and print results as they are completed
    for future in concurrent.futures.as_completed(future_to_task):
        task_number = future_to_task[future]
        try:
            result = future.result()
        except Exception as exc:
            print(f"Task {task_number} generated an exception: {exc}")
        else:
            print(f"Task {task_number} result: {result}")
