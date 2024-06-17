import multiprocessing
import time
def print_records(records):
    for record in records:
        print("Name: {0}\nScore: {1}\n".format(record[0], record[1]))

def insert_record(record, records):
    records.append(record)
    print("New record added!\n")

if __name__ == "__main__":
    with  multiprocessing.Manager() as manager:
        records = manager.list([("Sam", 10), ("Adam", 9), ("Kevin", 8)])
        new_record = ("Jeff", 8)

        p1 = multiprocessing.Process(target=insert_record, args=(new_record, records))
        p2 = multiprocessing.Process(target=print_records, args=(records,))

        p1.start()
        p1.join()
        print("Record after process 1:")
        print("Record 1 execution time: {}".format(time.process_time()))


        p2.start()
        p2.join()
        print("Record after process 2:")
        print("Record 2 execution time: {}".format(time.process_time()))

        print("Record in main:")
        print_records(records)
        print("Total execution time: {}".format(time.process_time()))

        print("Done!")