# 进程是执行中的程序
# 拥有独立的地址空间 内存 数据栈
# 操作系统管理
# 派生 新进程
# 进程键通信IPC 方式共享信息
   #进程是并行  10个进程同时运行

# 什么是线程
# 同进程下执行 并共享上下文
# 多线程 并发执行
# 需要同步原语
  #*******并发是不是同时运行 轮询运行

# Python 与线程
# 解释器主循环
# 解释器中只有一个控制线程在执行
# 使用全局解释器所 GIL
# GIL　保证一个线程


#两种线程管理
# _thread module


# threading module
import _thread
from time import sleep, ctime
import logging

logging.basicConfig(level=logging.INFO)
loops = [2, 4]
def loop(nloop, nsec, lock):
    logging.info("start loop "+str(nloop)+str(ctime()))
    sleep(nsec)
    logging.info("end loop "+ str(nloop)+ str(ctime()))
    lock.release()



# 当主线程结束的时候 所有的子线程都被kill掉
def main():
    logging.info("start all at " + ctime())
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire() #加锁操作
        locks.append(lock) #把所有的锁加进来

    for i in nloops:
        _thread.start_new_thread(loop,(i,loops[i],locks[i]))

    for i in nloops:
        while locks[i].locked():pass
rt5e
    logging.info("end all at " + ctime())


if __name__ == '__main__':
    main()