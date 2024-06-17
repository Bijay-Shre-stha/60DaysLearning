import multiprocessing 
import os
import time

def square(num):
    print("Worker Process ID for {0}: {1}".format(num, os.getpid()))
    print("Square: {}".format(num * num))

def cube(num):
    print("Worker Process ID for {0}: {1}".format(num, os.getpid()))
    print("Cube: {}".format(num * num * num))

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=square, args=(9,))
    p2 = multiprocessing.Process(target=cube, args=(9,))

    p1.start()
    print("Process 1 started")
    p2.start()
    print("Process 2 started")

    print("Process 1 is alive: {}".format(p1.is_alive()))
    print("Process 2 is alive: {}".format(p2.is_alive()))

    p1.join()
    p2.join()

    print("Process 1 is alive: {}".format(p1.is_alive()))
    print("Process 2 is alive: {}".format(p2.is_alive()))

    #print time to complete
    print("Time to complete: {}".format(time.process_time()))

    print("Done!")
