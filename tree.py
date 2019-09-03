class Node(object):
    def __init__(self,key=None):
        self.data=key
        self.left=None
        self.right=None
        self.hd=0
def hd(root):
    q=[]
    hd=0
    root.hd=hd
    q.append(root)
    l=[]
    #l.append([root.data,root.hd])
    while(len(q)):
        root=q[0]
        hd=root.hd
        #print(root.data)
        l.append([root.data,root.hd])
        if(root.left):
            root.left.hd=hd-1
            q.append(root.left)
        if(root.right):
            root.right.hd=hd+1
            q.append(root.right)
        q.pop(0)
    return l
def lefttree(root):
    q=[]
    hd=-1
    root.left.hd=hd
    q.append(root.left)
    l=[]
    while(len(q)):
        root=q[0]
        hd=root.hd
        l.append([root.data,root.hd])
        if(root.left):
            root.left.hd=hd-1
            q.append(root.left)
        if(root.right):
            root.right.hd=hd-1
            q.append(root.right)
        q.pop(0)
    return l
def righttree(root):
    q=[]
    hd=1
    root.right.hd=hd
    q.append(root.right)
    l=[]
    while(len(q)):
        root=q[0]
        hd=root.hd
        l.append([root.data,root.hd])
        if(root.left):
            root.left.hd=hd+1
            q.append(root.left)
        if(root.right):
            root.right.hd=hd+1
            q.append(root.right)
        q.pop(0)
    return l

   
root=Node(5)
root.left=Node(3)
root.left.left=Node(2)
root.left.right=Node(4)
root.left.left.left=Node(1)
root.right=Node(9)
root.right.left=Node(7)
root.right.left.left=Node(6)
root.right.left.right=Node(8)
root.right.right=Node(11)
root.right.right.left=Node(10)
x=[[root.data,0]]+lefttree(root)+righttree(root)



def find_dis_from(val,dis):
    p=0
    l=[]
    for i in x:
        if(val==i[0]):
            p=i[1]
            break
    for i in x:
        if(dis==abs(i[1]-p)):
            l.append(i[0])
    return l
print(find_dis_from(3,2))
