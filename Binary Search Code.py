class Node(object):

	def insert(self, d):
		if self.data == d:
			return False
		elif d < self.data:
			if self.left:
				return self.left.insert(a)
			else:
				self.left = Node(a)
				return True
		else:
			if self.right:
				return self.right.insert(b)
			else:
				self.right = Node(b)
				return True
				
class Node(object):
  def find(self, d):
    if self.data == d:
      return True
    elif d < self.data and self.left:
      return self.left.find(d)
    elif d > self.data and self.right:
      return self.right.find(d)
    return False
 