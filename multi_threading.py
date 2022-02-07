import threading
import time

def main():
    # 看看有几个线程
    print(threading.active_count())
    # 打印出线程
    print(threading.enumerate())
    # 下面这个是主线程
    # [<_MainThread(MainThread, started 2612)>]
    # 打印当前进程
    print(threading.currentThread())

def thread_job():
    print('This is an added Thread, number is %s' % threading.currentThread())

def main1():
    # 添加一个进程，target是指向这个线程运行的函数
    added_thread = threading.Thread(target=thread_job)
    # 启动这个线程
    added_thread.start()

def thread_job1():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish\n')

def thread_job2():
    print('T2 start')
    print('T2 finish')

def main2():
    # name可以命名线程
    added_thread = threading.Thread(target=thread_job1, name='T1')
    thread2 = threading.Thread(target=thread_job2,name='T2')
    added_thread.start()
    thread2.start()
    # join的意思就是等上面的线程运行完了，再运行下面的语句
    added_thread.join()
    thread2.join()
    print('all done\n')

if __name__ == '__main__':
    # main()
    # main1()
    main2()