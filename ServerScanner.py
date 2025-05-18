from mcstatus import JavaServer
from random import randint
import threading
import time

MAX_THREADS = 600

def test():
    filepath = input("Path to text file to save data in:")
    file = open(filepath, "a+")
    ip = str(randint(1, 255)) + "." + str(randint(1, 255)) + "." + str(randint(1, 255)) + "." + str(randint(1, 255)) + ":25565"
    server = JavaServer.lookup(ip)

    try:
        print((server.status().version.__str__() + " Exists"))
        res = ip + " - " + server.status().version.__str__() + " -  Exists"
        file.write(res + "\n")
    except:
        print("Error")
        res = ip + " - None"
        
    file.close()

# thread thing

while True:
    time.sleep(3)

    threads = []
    for _ in range(MAX_THREADS):
        thread = threading.Thread(target=test)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
