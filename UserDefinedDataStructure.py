# Linked Lists
class Node:
    def __init__(self, data=None, pointer=None):
        self.data = data
        self.pointer = pointer


class LinkedList:
    def __init__(self):
        self.head = None

    def get_length(self):
        if self.head is None:
            return 0
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.pointer
        return count

    def insert_at_begining(self,data):
        node=Node(data,self.head)
        # above self.head holds the address of previous node object
        self.head=node
        # now this self.head will keep the address of current node object

    def insert_at_end(self,data):
        node=Node(data,None)
        if self.head is None:
            self.head=node
            return

        itr=self.head
        while itr.pointer:
            itr=itr.pointer
        itr.pointer=node

    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.pointer)
                itr.pointer=node
                break

            itr=itr.pointer
            count+=1

    def print(self):
        if self.head is None:
            print("LinkedList is Empty")
            return
        itr=self.head
        print(itr)
        llstr=''

        while itr:
            llstr+=str(itr.data) + "--->"
            itr=itr.pointer
            print(itr)
        print(llstr)

if __name__ =='__main__':
    ll=LinkedList()
    ll.insert_at_begining(89)
    ll.insert_at_begining(99)
    ll.insert_at_end(88)
    ll.print()
    ll.insert_at(1,190)
    ll.print()
    print(ll.get_length())

# from collections import deque
# stack=deque()
# print(dir(stack))