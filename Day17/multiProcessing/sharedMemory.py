import multiprocessing
import time

def square_list(my_list, result, square_sum):
    print("Worker Process ID: {}".format(multiprocessing.current_process().pid))
    for index, num in enumerate(my_list):
        result[index] = num * num
    print("Result (in process): {}".format(result[:]))

    square_sum.value = sum(result)
    print("Sum of squares (in process): {}".format(square_sum.value))

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6]
    result = multiprocessing.Array('i', len(my_list))
    square_sum = multiprocessing.Value('i', 0)

    p1 = multiprocessing.Process(target=square_list, args=(my_list, result, square_sum))

    start_time = time.time()
    p1.start()
    p1.join()
    end_time = time.time()

    print("Time to execute: {:.4f} seconds".format(end_time - start_time))

    print("Result (in main): {}".format(result[:]))
    print("Sum of squares (in main): {}".format(square_sum.value))
    print("Total execution time: {:.4f} seconds".format(time.process_time()))
