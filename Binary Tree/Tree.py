from prettytable import PrettyTable

class Node:
     
    def __init__(self, x):
         
        self.data = x
        self.left = None
        self.right = None


def build(inn, post, start, end):
    global dc, index, lst, lstIndex
    # print(dc) 
 
    if (start > end):
        return None

    curr = post[index]
    node = Node(curr)
    lst[lstIndex] = curr
    lstIndex += 1
    index -= 1
 
    #If node doesn't have any children
    if (start == end):
        return node
 

    iIndex = dc[curr]
 

    node.right = build(inn, post,
                           iIndex + 1, end)
    node.left = build(inn, post, start,
                          iIndex - 1)
 
    return node
 

def constructTree(inn, post, lenn):
     
    global index
    global lst, lstIndex
    for i in range(lenn):
        dc[inn[i]] = i
         
    # Index in postorder
    index = lenn - 1
    return build(inn, post, 0, lenn - 1)
 
#preorder Traversal
def preOrder(node):
     
    if (node == None):
        return
         
    print(node.data, end = " ")
    preOrder(node.left)
    preOrder(node.right)

#postorder Traversal
def postOrder(node):

    if(node==None):
        return 

    postOrder(node.left)
    postOrder(node.right)
    print(node.data, end=" ")

#Inorder Traversal
def inOrder(node):

    if(node==None):
        return 

    inOrder(node.left)
    print(node.data, end=" ")
    inOrder(node.right)
 
# Driver Code
if __name__ == '__main__':
     
    inn = [ 4, 8, 2, 5, 1, 6, 3, 7 ]
    post = [ 8, 4, 5, 2, 6, 7, 3, 1 ]
    n = len(inn)
    dc, index, lst, lstIndex = {}, 0, {}, 0
    root = constructTree(inn, post, n)

    # Prettytable
    print("\n The index of the node and its correspondig value are: ")
    tb = PrettyTable()
    tb.field_names = ["index", "value of node"] 
    for i in lst:
        tb.add_row([i, lst[i]])
    print(tb)
 
    print("\nThe array in pre order traversal is :")
    preOrder(root)

    print("\n\nThe array in post order traversal is :")
    postOrder(root)

    print("\n\nThe array in in order traversal is :")
    inOrder(root)
    print("\n")