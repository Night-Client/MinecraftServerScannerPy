from mcstatus import JavaServer
from random import randint
import threading
import time

MAX_THREADS = 600
filepath = input("Path to text file to save data in: ")
last_scanned = 0
total_scanned = 0
found = 0

def test():
    global total_scanned
    global found
    file = open(filepath, "a+")
    ip = str(92) + "." + str(randint(100, 120)) + "." + str(randint(1, 255)) + "." + str(randint(1, 255)) + ":25565"
    server = JavaServer.lookup(ip)

    try:
        res = ip + " - " + server.status().version.name.__str__()
        file.write(res + "\n")
        found += 1
    except:
        pass

    total_scanned += 1
    file.close()

def status():
    global last_scanned
    global total_scanned
    global found
    time.sleep(10)
    print("Scanned " + str(total_scanned) + " Servers (" + str((total_scanned - last_scanned)/10) + "/s) And Found " + str(found) + " Servers")
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
