import subprocess
from time import sleep

class Node:
    def __init__ (self, x):
        self.x = x
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.head = None
        self.last = self.head
        self.lenght = 0
    
    def enqueue(self,x):
        if(self.head == None):
            self.head = Node(x)
            self.last = self.head
        else:
            node = Node(x)
            self.last.next = node
            node.prev = self.last
            self.last = node
        self.lenght += 1

    def dequeue(self):
        if(self.head == None):
            print("There's no element to dequeue")
        else:
            self.head = self.head.next
            print("Dequeued.")
            self.lenght -= 1

    def printQueue(self):
        pointer = self.last
        for i in range(self.lenght):
            print("-{p}".format(p=pointer.x), end ="")
            pointer = pointer.prev


def clearScreen():
    try:
        subprocess.run(['clear'], check = True, shell=True) #linux
    except:
        subprocess.run('cls', shell=True)

queue = Queue()

while True:

    clearScreen()

    try:
        selection = int(input("Select a function to do. \n1-Enqueue\n2-Dequeue\n3-PrintQueue\n4-Exit\n"))
        clearScreen()

        if(selection==1):
            x = int(input("Enter a value to enqueue.\n"))
            queue.enqueue(x)
            queue.printQueue()        

        elif (selection==2):
            queue.dequeue()
            queue.printQueue()  
            
        elif(selection==3):
            queue.printQueue()

        elif(selection==4):
            break

        else:
            print("Invalid input.")
        print("")
        sleep(2)

    except:
        print("Invalid input.")
        sleep(2)
        