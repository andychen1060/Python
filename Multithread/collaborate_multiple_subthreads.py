#Collaborate multiple subthreads. 
import threading
import time

def task(name):
    global total_task_count, tasks, current_task, lock  #ready to use global variable later    
    while True:     
        lock.acquire()  #restrict threads not to process the task repeatedly
        if current_task == len(tasks):
            lock.release()
            break      
        task = tasks[current_task]  #get next task
        print("{} is processing by {}".format(task, name)) 
        time.sleep(1)  #simulate that every thread need to spend a second to tag the task which it had taken         
        current_task += 1
        total_task_count += 1
        lock.release()
        time.sleep(2)  #simulate that every task need to take two seconds to be finished
        print("{} is finished by {}".format(task, name))

if __name__ == '__main__':
    tasks = ["task1", "task2", "task3", "task4", "task5", "task6", "task7", "task8", "task9", "task10"]  #suppose there are ten tasks which need to be finished 
    lock = threading.Lock()  
    thread1 = threading.Thread(target=task, args=("Thread1",))  #create a thread instance
    thread2 = threading.Thread(target=task, args=("Thread2",))   
    thread3 = threading.Thread(target=task, args=("Thread3",))
    thread4 = threading.Thread(target=task, args=("Thread4",))   
    current_task = 0
    total_task_count = 0
    thread1.start()  #active thread
    thread2.start()  
    thread3.start()  
    thread4.start()    
    thread1.join()  #wait for thread1 to finish
    thread2.join()
    thread3.join()  
    thread4.join()
    print("Finished! Completed {} tasks in total".format(total_task_count))    