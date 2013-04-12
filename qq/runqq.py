#coding=utf-8
from login_qq import webqq
import thread
import threading
import Queue

msg_queue = Queue.Queue()

def poll2_daemon(qq):
    while 1:
        qq.poll2()

class process_msg_daemon(threading.Thread):
    def __init__(self, msg_queue):
        threading.Thread.__init__(self)
        self.msg_queue = msg_queue

    def run(self):
        while 1:
            msg = self.msg_queue.get()
            print msg()
            self.msg_queue.task_done()

class senf_msg_daemon(threading.Thread):
    def __init__(self, send_queue):
        threading.Thread.__init__()
        self.send_queue = send_queue

    def run(self):
        while 1:
            send = self.send_queue.get()
            print send
            self.send_queue.task_done()

def run():
    #user = raw_input('QQ:')
    #pwd = getpass.getpass('password: ')
    import os
    user = os.environ['QQ']
    pwd = os.environ['QQ_PASSWD']
    qq = webqq(user, pwd)
    qq.getSafeCode()
    qq.loginGet()
    qq.loginPost()
    qq.getGroupList()
    qq.getFriend()

    import thread
    thread.start_new_thread(poll2_daemon, (qq))
    for i in range(100):
        print 'to', qq.friend['info'][0]['uin']
        print 'to', qq.group['gnamelist'][10]
        #qq.sendMsg(str(qq.friend['result']['info'][0]['uin']), 'clientjsfzhiyong')
        ms = ''
        for _ in xrange(i):
            ms += '。'
        qq.sendQunMsg(str(qq.group['gnamelist'][10]['gid']), ms)
        #qq.sendMsg('2236071402', 'geisf')

if __name__ == "__main__":
    thread.start_new_thread(th, (0, 5))
    import time
    time.sleep(5)