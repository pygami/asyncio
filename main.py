import multiprocessing
import time


def task1():
    print("Task 1 started")
    time.sleep(2)  
    print("Task 1 completed")


def task2():
    print("Task 2 started")
    time.sleep(3)  
    print("Task 2 completed")

if __name__ == "__main__":
    
    process1 = multiprocessing.Process(target=task1)
    process2 = multiprocessing.Process(target=task2)
    
    
    process1.start()
    process2.start()
    
    
    process1.join()
    process2.join()
    
    print("All tasks completed")
