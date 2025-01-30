class node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Linked_List:
  def __init__(self, Node):
    self.head = None

  def add(self, Node):
    if self.head == None:
       self.head = Node
    New_node = Node
    self.head.next = New_node
    while self.head.next == None:
      self.head.next = New_node
    self.head.next = New_node.next  
