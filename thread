# 스레드(thread)는 프로그램 내에서 동시에 실행될 수 있는 가장 작은 작업 단위를 뜻합니다. 하나의 프로그램(프로세스)은 여러 개의 스레드를 만들어 동시에 여러 작업을 수행할 수 있습니다.
import time
import threading


def task1():
    while True:
        print("Task 1 is running")
        time.sleep(1)


def task2():
    while True:
        print("Task 2 is running")
        time.sleep(1)


# 스레드를 사용하지 않는 경우
# task1()
# task2()
# Task 1 is running

# 스레드를 사용하는 경우
# 두 작업을 각각 스레드로 실행
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()
# Task 1 is running
# Task 2 is running
