#Main thread will wait for user to type character "q" to stop counting, meanwhile the sub-thread thread1 will be counting
import threading

def program_count():
    global input_str, total_count
    while True:
        total_count += 1
        if input_str == "q":            
            break

if __name__ == '__main__':
    total_count = 0
    input_str = ""
    thread1 = threading.Thread(target=program_count)  #create a thread instance
    thread1.start()  #active thread(program start counting)       
    while True:
        input_str = input('Type "q" to stop count:')  #wait for user to type character "q" to stop counting
        if input_str == "q":
            break
    thread1.join()  #let main thread to wait for thread1 finish thread
    print("Total count: ", total_count)