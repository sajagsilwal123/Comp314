# class BinarySearchTree:
#     def __init__(self):
#         self.left = None
#         self.right = None
#         self.value  = None


#     def insertNode(self, key, value , root=None):
        
#         if root is None:
#             root.value = key
#             return BinarySearchTree(key)
#         else:
#             if root.value==key:
#                 return root
#             elif root.value<key:
#                 root.right = self.insertNode(root.right, key)
#             elif root.value>key:
#                 root.left = self.insertNode(root.left, key)
#         return root

#     def Search(self, root, key):
#         if root:
#             if (key==root.value):
#                 return 1
#             elif(key<root.value):
#                 self.Search(root.left, key)
#             elif(key>root.value):
#                 self.Search(root.right, key)
#             else:
#                 return -1

#     def Smallest(self, root):
#         if root.left:
#             small = self.Smallest(root.left)   
#             return small  
#         else:
#             return root.value 
            
#     def Largest(self, root):
#         if root.right:
#             small = self.Largest(root.right)  
#             return small  
#         else:
#             return root.value


#     def preOrder(self, root):
#         if root:
#             print(root.value)
#             self.preOrder(root.left)
#             self.preOrder(root.right)
            
#     def postOrder(self,root):
#         if root:
#             self.postOrder(root.left)
#             self.postOrder(root.right)
#             print(root.value)

#     def inOrder(self, root):
#         if root:
#             self.inOrder(root.left)
#             print(root.value)
#             self.inOrder(root.right)


#     def count(self, root): 
#         if root is None:
#             return 0
#         return 1 + self.count(root.left)+ self.count(root.right) 

# # test = BinarySearchTree(50)
# # test = insertNode(test,10)
# # test = insertNode(test,60)
# # test = insertNode(test,5)
# # test = insertNode(test, 2)
# # test = inOrder(test)
# # print (Search(test, 8))
# # print(Smallest(test))
# # print(count(test))