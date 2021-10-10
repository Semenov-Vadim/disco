Node:
  neigh = list
  received = []
  father = None
  
  
  def init():
    father = self
    for node in neigh:
      node.notify(self)
      
      
  def notify(sender: Node):
    if father == None:
      father = sender
      for node in neigh:
        if node not in received and node != father:
          node.notify(self)
    else:
      received.append(Node)
      if received.size() - neigh.size() == 1:
        father.notify()
    if father == self and if received.size() - neigh.size() == 0:
      return True
      
        

        
  
