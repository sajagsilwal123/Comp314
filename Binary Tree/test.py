import networkx as nx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import matplotlib.pyplot as plt
G = nx.DiGraph()
for i in range(5):
    G.add_node('Child_%i' % i)
    G.add_edge('Root','Child_%i' %i)

write_dot(G, 'text.dot')
plt.title('Draw')
pos = graphviz_layout(G, prog='dot')
nx.draw(G, pos)


# class BinaryTree:
#     def __init__(self):
#         self.value = None
#         self.left = None
#         self.right =  None

#     def build(self, inOrder:list, PostOrder:list):
#         length = len(PostOrder)
#         root = PostOrder[length-1]
#         left = 0
#         right = 0
#         leftArray = []
#         rightArray = []
#         self.value = root
#         for i in range(inOrder):
#             if (root==inOrder[i]):
#                 left = i-1
#                 right = i+1
#                 leftArray = inOrder[0:left]
#                 rightArray = inOrder[right:length-1]
                



# test = BinaryTree()
# inOrder = [4,8,2,5,1,6,3,7]
# postOrder = [8,4,5,2,6,7,3,1]
# test.build(inOrder, postOrder)