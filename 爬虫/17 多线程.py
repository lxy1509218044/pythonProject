# 进程和线程
# 进程是资源单位，每一个进程至少要有一个线程
# 线程是执行单位

# # 单线程
# 先执行fun()函数里的循环,再执行外部for循环
# def fun():
#     for i in range(1000):
#         print("func",i)
#
# if __name__=='_name_':
#     fun()
#     for i in range(1000):
#         print('main',i)

# # 多线程 1 使用函数
# from threading import Thread # 导入一个 线程类
# import time
# def func():
#     for i in range(10):
#         print("func",i)
#
# if __name__ == '__main__':
#     t = Thread(target=func) #使用线程库创建一个多线程任务
#     t.start() #告诉程序可以开始执行该线程,多线程状态为可以开始工作,具体执行时间由cpu决定
#     for i in range(10): # 与此同时,外部for循环也在同步执行
#         print("main",i)
#     time.sleep(2)

# 多线程 2 使用类
# from threading import Thread # 导入一个 线程类
# class mythread(Thread):
#     def run(self):  # 固定的 -> 当线程被执行的时候,被执行的就是run()
#         for i in range(10):
#             print('子线程',i)
# if __name__== '__main__':
#     t= mythread()
#     # t.run() # 这是方法的调用,不是调用线程
#     t.start() # 开启线程
#     for i in range(10):
#         print('主线程', i)


# 多线程 2 使用类
from threading import Thread
def func(name):  # 向函数传递参数
    for i in range(1000):
        print(name, i)

if __name__ == '__main__':
    t1 = Thread(target=func, args=("周杰伦",))  # 传递参数必须是元组
    t1.start()
    t2 = Thread(target=func, args=("王力宏",))
    t2.start()
