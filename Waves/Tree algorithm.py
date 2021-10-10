class Node:
  father = None
  neigh = list
  visited = []
  
  
  def notify(sender: Node):
    if sender = faher:
      return
    else:
      visited.append(sender)
      visit()
      
    
  def visit():
    while neigh.size() - visited.size() > 1:
      receive()
    
    if neigh.size() - visited.size() == 1:
      for node in neigh:
        if node not in visited:
          father = node
          node.notify(self)
          break
          
