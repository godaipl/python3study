import queue, threading, time, urllib
from urllib import request

base_url = 'https://www.baidu.com/index.php/'
url_queue = queue.Queue()

for i in range(1, 50):
    url = base_url + str(i)
    url_queue.put(url)
    print("添加url url is ", url)


def fetch_url(url_queue):
    while True:
        try:
            # 不阻塞的读取队列数据
            url2 = url_queue.get_nowait()
            j = url_queue.qsize()
        except Exception as  e:
            print("读取url的时候报错")
            break
        print('Current Thread Name %s, Url: %s ' % (threading.currentThread().name, url2))

        try:
            response = urllib.request.urlopen(url2)
            responseCode = response.getcode()
        except Exception as e1:
            continue
        if responseCode == 200:
            # 抓取内容的数据处理可以放到这里
            # 为了突出效果， 设置延时
            time.sleep(1)


if __name__ == '__main__':
    start_time = time.time()
    threads = []
    threadNum = 10
    for i in range(0, threadNum):
        t = threading.Thread(target=fetch_url, args={url_queue})
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    end_ime = time.time()

    print('Done, Time cost: %s ' % (end_ime - start_time))
