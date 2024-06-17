## **Multiprocessing**

- Multiprocessing refers to yje ability of a system to support more than one processor at the same time.
- Applications in a multiprocessing system are broken to smaller routines that run independently.
- The operating system allocates these threads to the processors improving performance of the system.
- Multiprocessing can be done through:
    - **Processes**: Creating new process
    - **Threads**: Creating new threads
- A multiprocessing system can have:
  - multiprocessor, i.e. a computer with more than one central processor.
  - multi-core processor, i.e. a single computing component with two or more independent actual processing units (called “cores”).

## **Shared Memory Multiprocessing**

- In multiprocessing, several processes share a common portion of memory.
- This is more efficient than passing several copies of data back and forth between processes.
- In this module provides **Array** and **Value** classes to share memory between processes.
  - **Array**: A ctypes array allocated from shared memory.
    - **Value**: A ctypes object allocated from shared memory.

## **Server Process Multiprocessing**

- In multiprocessing, a server process is created that manages shared objects.
- A serve process can hold Python objects and allows other processes to manipulate them using **proxies**.
- A **proxy** is an object which refers to a server object.

## **Summary**

- **Multiprocessing** refers to the ability of a system to support more than one processor at the same time.
- **Shared Memory Multiprocessing** allows multiple processes to share a common portion of memory.
- **Server Process Multiprocessing** creates a server process that manages shared objects.
- **Proxy** is an object which refers to a server object.
