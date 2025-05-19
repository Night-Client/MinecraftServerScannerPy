from mcstatus import JavaServer
from random import randint
import threading
import time

MAX_THREADS = 600
filepath = input("Path to text file to save data in: ")
last_scanned = 0
total_scanned = 0

def test():
    global total_scanned
    file = open(filepath, "a+")
    ip = str(92) + "." + str(randint(100, 120)) + "." + str(randint(1, 255)) + "." + str(randint(1, 255)) + ":25565"
    server = JavaServer.lookup(ip)

    try:
        print((server.status().version.__str__() + " Exists"))
        res = ip + " - " + server.status().version.__str__() + " -  Exists"
        file.write(res + "\n")
    except:
        pass

    total_scanned += 1
    file.close()

def status():
    global last_scanned
    global total_scanned
    time.sleep(10)
    print("Scanned " + str(total_scanned) + " Servers (" + str((total_scanned - last_scanned)/10) + "/s)")
    last_scanned = total_scanned
    status()

threading.Thread(target=status).start()

# thread thing

while True:
    time.sleep(1)

    threads = []
    for _ in range(MAX_THREADS):
        thread = threading.Thread(target=test)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
