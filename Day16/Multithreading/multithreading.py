import threading
import time

def print_cube(num):
    time.sleep(2)
    print("Cube: {}".format(num * num * num))

def print_square(num):

    time.sleep(2)
    print("Square: {}".format(num * num))

if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    # starting thread 1
    t1.start()
    print("Thread 1 started")
    # starting thread 2
    t2.start()
    print("Thread 2 started")

    # wait until thread 1 is completely executed
    print("Thread 1 is alive: {}".format(t1.is_alive()))
    # wait until thread 2 is completely executed
    print("Thread 2 is alive: {}".format(t2.is_alive()))


    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    print("Thread 1 is alive: {}".format(t1.is_alive()))
    print("Thread 2 is alive: {}".format(t2.is_alive()))


    # both threads completely executed
    print("Done!")