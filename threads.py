"""
    @author : RituRaj
    created : 24 Apr,19
"""

from urllib.request import urlopen , Request
import time 
from threading import Thread
import requests

# Single Threaded Program
def singleThreadResponse():
    """
        Summary
            - All the urls are fetched in sequence
            - Unless the processsor got reposnse from a url , it didn't fetch next url.
            - Network operatons are taking time 
            - single threaded program
            - Even in single threaded program , there is one thread of execution call it main thread.
    """
    urls = [
        'http://www.google.com', 
        'http://www.amazon.com', 
        'http://www.ebay.com', 
        'http://www.alibaba.com', 
        'http://www.reddit.com'
    ]
    start = time.time()
    for url in urls:
        print (url)
        headers={'User-Agent' : 'my bot'}
        req = Request(url,headers=headers)
        resp = urlopen(req)
        print (resp.getcode())

    print ("Elapsed time - ",format(time.time() - start))

# Multi Threaded Way 
class GetUrlThread(Thread):
    def __init__(self,url):
        self.url = url 
        super(GetUrlThread,self).__init__()
        
    def run(self):
        headers={'User-Agent' : 'my bot'}
        req = Request(self.url, headers=headers)
        resp = urlopen(req)
        print (resp , resp.getcode())

def multiThreadResponse():
    """
        Summary
            I wrote a multi threaded program to decrease processor’s idle time. 
            - While waiting for response of a particular thread’s url, processor can work on some other thread 
            and fetch the other thread’s url.
            - We wanted one thread to act on one url, 
            so overridden the constructor of thread class to pass it a url.
            - Execution of a thread means execution of a thread’s run().
            - So, whatever we want the thread to do must go in its run().
            - Created one thread for each url and called start() on it. 
            - This tells the processor that it can execute the particular thread i.e the run() of thread.
            - We don’t want the elapsed time to be evaluated 
            - until all the threads have executed, join() comes in picture here.
            - Calling join() on a thread tells the main thread 
            - to wait for this particular thread to finish before the main thread can execute the next instruction.
            - We call join() on all the threads, 
            - so elapsed time will be printed only after all the threads have run.
            
            some more things aboout Thread
                - Processor might not execute run() of a thread immediately after start().
                - You can’t say in which order run() of different threads will be called.
                - For a specific thread, it’s guaranteed that the statements 
                - inside run() will be executed sequentially.
                - It means that first the the url associated with the 
                - thread will be fetched and only then the recieved response will be printed.
    """
    urls = [
        'http://www.google.com', 
        'http://www.amazon.com', 
        'http://www.ebay.com', 
        'http://www.alibaba.com', 
        'http://www.reddit.com'
    ]
    start = time.time()
    threads = []
    for url in urls:
        t = GetUrlThread(url)
        threads.append(t)
        t.start()
    
    print (threads)
    for t in threads:
        t.join()
    
    print ("Elapsed time - ",time.time() - start)

if __name__=="__main__":
    print ("Single Thread Result")
    singleThreadResponse()
    print ("Multi Thread Result")
    print ("\n")
    multiThreadResponse()

    