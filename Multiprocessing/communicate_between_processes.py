"""
Communication between processes.
In this sample code, the subprocess will pass each non-duplicate random number to main process through Queue.
At the end of the subprocess, the result will all be stored in a list and pass to main process via Pipe.
Main process will recieve and print the result on screen.
"""
from multiprocessing import Process, Pipe, Queue, current_process
from random import randint
from time import sleep

def get_random_numbers(random_number_count, conn, queue):
    """Get specific number of non-duplicate random numbers."""
    result = list()
    count = 1
    while count <= random_number_count:  #get random numbers
        random_number = randint(1, 40)   #randomly draw a number
        if not(random_number in result):  #check if a number has been drawn
            result.append(random_number)  #append the random number to the list
            queue.put(random_number)  #Once a number is drawn, the number is passed to main process
            count += 1
            sleep(1)
    result.sort()
    conn.send(result)  #pass result list to main process

if __name__ == '__main__':  
    parent_conn, child_conn = Pipe()  #communicate between processes through Pipe
    queue = Queue()  #communicate between processes through Queue
    random_number_count = 5  #specify the number of non-duplicate number which need to be drawn
    p1 = Process(target=get_random_numbers, args=(random_number_count, child_conn, queue))
    p1.start()  #active process
    count = 1
    print("====== Draw Numbers ======")
    while count <= random_number_count:
        print("Number {}: {}".format(count, queue.get()))  #get random number which was drawn by subprocess
        count += 1
    print("Result: {}".format(parent_conn.recv()))  #get result list
    p1.join()