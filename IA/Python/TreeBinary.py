from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {'This is the Tree binary': 'FastApi'}
class TreeBinary:
    def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

def findPath( root, path, k):
        if root is None:
            return False
        path.append(root.data)
        if root.data == k :
            return True
        if ((root.left != None and findPath(root.left, path, k)) or (root.right!= None and findPath(root.right, path, k))):
            return True
        
        path.pop()
        return False
    
def ancestro(root, n1, n2):
        path1 = []
        path2 = []

        if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
            return -1

        i = 0
        while(i < len(path1) and i < len(path2)):
            if path1[i] != path2[i]:
                break
            i += 1
        return path1[i-1]

root = TreeBinary(70)
root.left = TreeBinary(49)
root.left.left = TreeBinary(37)
root.left.left.left = TreeBinary(22)
root.left.left.right = TreeBinary(40)

root.left.right = TreeBinary(54)
root.left.right.left = TreeBinary(51)

root.right = TreeBinary(84)
root.right.right = TreeBinary(85)
root.right.left = TreeBinary(78)
root.right.left.left = TreeBinary(76)
root.right.left.right = TreeBinary(80)

print ("Ancestros de (40, 78) = %d" %(ancestro(root, 40, 78)))
print ("Ancestros de (51, 37) = %d" %(ancestro(root, 51, 37)))
print ("Ancestros de (76, 85) = %d" %(ancestro(root,76,85)))