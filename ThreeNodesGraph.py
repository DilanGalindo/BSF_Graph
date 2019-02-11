# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import deque
class QNode:
	def __init__(self,val, level, visited):
		self.val = val
		self.dist = level
		self.visited = visited
"""
insert three buttons in the graph.
First button will multiply the number by 2
Second button will multiply the number by 3
Third button would subtract 1 from the number
"""
def three_buttons(display: int, dest: int) -> int:
	"""
	Basically I am doing a BFS to solve the shortest path to the second number
	"""
	q = deque()
	q.append(QNode(display, 0, True))
	x = set()

	while len(q):
		cur = q.popleft()
		x.add(cur.val)
		if cur.val == dest:
			return cur.dist
		if ((not((cur.val * 2) in x)) and cur.val< dest*2):
			q.append(QNode(cur.val * 2, cur.dist + 1, False))
		if not((cur.val *3) in x) and cur.val < dest*3:
			q.append(QNode(cur.val * 3, cur.dist + 1, False))
		if not((cur.val -1) in x) and cur.val-1>0:
			q.append(QNode(cur.val - 1, cur.dist + 1, False))
			
def main():

	FirstInput = input()
	FirstInput=[int(s) for s in FirstInput.split(' ')]


	Element = FirstInput[0]
	SecondEle = FirstInput[1]
	result=0
	print(three_buttons(Element, SecondEle))

main()