# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        nodes=[]
        nodesMax=[]
        nodes.append(root)
        nodesMax.append(root.val)
        ans=1
        while(len(nodes)!=0):
            currentNode=nodes[0]
            nodes.remove(nodes[0])
            currentMax=nodesMax[0]
            nodesMax.remove(nodesMax[0])
            if(currentNode.left!=None):
                if(currentNode.left.val>=currentMax):
                    ans+=1
                nodes.append(currentNode.left)
                nodesMax.append(max(currentMax,currentNode.left.val))
            if(currentNode.right!=None):
                if(currentNode.right.val>=currentMax):
                    ans+=1
                nodes.append(currentNode.right)
                nodesMax.append(max(currentMax,currentNode.right.val))
        return ans




        