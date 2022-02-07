import threading

def main():
    # 看看有几个线程
    print(threading.active_count())
    # 打印出线程
    print(threading.enumerate())
    # 下面这个是主线程
    # [<_MainThread(MainThread, started 2612)>]

if __name__ == '__main__':
    main()