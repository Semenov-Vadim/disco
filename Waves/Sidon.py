class Node:
	neigh = list
	used = []
	father = None
	last = None
	
	# initializing the algorithm
	def init():
		father = self
		
		for node in neigh:
      node.notify(self)
		used.append(neigh[0])
		last = neigh[0]
		neigh[0].visit_next(self)
		
		
  # first enterence of this node
  def notify(sender: Node):
    if sender not in used:
      used.append(sender)
	
	
	def visit_next(sender: Node):
		if last != None and last != sender:
			if sender not in used:
				used.append(sender)
		
		elif father == None:
			father = sender
			for node in neigh:
				if node != father:
					node.notify(self)
					
		# checking the end of the program
      elif father == self:
        for node in neigh:
          if node not in used:
            break
        else:
          return
				
			else:
        for node in neigh:
          if node not in used and node != father:
            used.append(node)
            node.visit_next(self)
        else:
          father.visit_next(self)
					
					
      
if __name__ == __main__:
  # some algorithm of creating Nodes
  nodes= list
  
  # randomly choose init node 
  init = rand(nodes)
  init.init()
