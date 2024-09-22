import threading
import os


def task1():
    print("\nTask 1 assigned to Thread: {}".format(threading.current_thread().name))
    print("\nID of process running Task 1: {}".format(os.getpid()))

def task2():
    print("\nTask 2 assigned to Thread: {}".format(threading.current_thread().name))
    print("\nID of process running Task 2: {}".format(os.getpid()))

if __name__=="__main__":
    print("\nID of process running main program: {}".format(os.getpid()))
    print("\nMain thread name: {}".format(threading.current_thread().name))


    t1=threading.Thread(target=task1, name="t1")
    t2=threading.Thread(target=task2, name="t2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
