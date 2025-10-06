class ListNode:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    def __str__(self):
        return str(self.data)

A=ListNode(10)
B=ListNode(15)
C=ListNode(20)
Head=A
A.next=B
B.next=C
'''print(Head)
print(Head.next)
print(Head.next.next)
#insert at start
new=ListNode(1)
new.next=A
Head=new
#delete first

Head=Head.next
#insert at last
val1=ListNode(30)
def insertEnd(head,val):
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=val
    print(ListNode(head))

insertEnd(Head,val1)
'''
#delete last
def deleteLast(head):
    curr=Head
    while curr.next.next!=None:
        curr=curr.next
    curr.next=None
deleteLast(Head)


def traverse(head):
    curr=head
    Element=[]
    while curr!=None:
        Element.append(str(curr.data))
        curr=curr.next
    print (" -> ".join(Element))
traverse(Head)

'''def Search(head,target):
    curr=head
    while curr!=None:
        if curr.data==target:
            return True
        else:
            curr=curr.next
    return False
Search(Head,10)'''







'''"Doubly Linked list"

class DoublyNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    def __str__(self):
        return str(self.data)

a=DoublyNode(5)
b=DoublyNode(7)
c=DoublyNode(9)

a=head
a.next=b
b.prev=None
b.next=c
c.prev=b'''

