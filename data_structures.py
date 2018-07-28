#I IMPLEMENT A BASIC QUEUE & GRAPH DATA STRUCTURES HERE.

import numpy as np

#a simple queue data structure implementation
class Queue:

  #Constructor creates a list
  def __init__(self):
      self.queue = list()

  #check if DATA is already in queue
  def contains(self,data):
  	if data in self.queue:
  		return True
  	return False

  #check if queue is empty
  def empty(self):
  	if len(self.queue) == 0:
  		return True
  	else:
  		return False



  #Adding elements to queue
  def enqueue(self,data):
      #Checking to avoid duplicate entry (not mandatory)
      if data not in self.queue:
          self.queue.insert(0,data)
          return True
      return False

  #Removing the first element from the queue
  def dequeue(self):
      if len(self.queue)>0:
          return self.queue.pop()
      return ("Queue Empty!")

  #Getting the size of the queue
  def size(self):
      return len(self.queue)

  #printing the elements of the queue
  def printQueue(self):
      return self.queue

#create a simple graph class that supports finding parents, children of a vertex
class Graph:
	#constructor
	def __init__(self, n, arr):
		self.num_vertices = n
		self.adj_mat = arr
		return
	#returns the size of the queue
	def size(self):
		return self.num_vertices

	#returns the edge weight associated with start vertex and end vertex in this graph.
	def get_edge_weight(self, start_vertex, end_vertex):
		if (start_vertex >= self.num_vertices or start_vertex < 0) or(end_vertex >= self.num_vertices or end_vertex < 0):
			#raise some error
			raise ValueError("Invalid vertex provided as argument.")
		else:
			return self.adj_mat[start_vertex][end_vertex]

	#changes the edge weight associated with edge between START_VERTEX & END_VERTEX to NEW_WEIGHT
	def change_edge_weight(self, start_vertex, end_vertex, new_weight):
		if (start_vertex >= self.num_vertices or start_vertex < 0) or(end_vertex >= self.num_vertices or end_vertex < 0):
			#raise some error
			raise ValueError("Invalid vertex provided as argument.")
		if (new_weight < 0):
			raise ValueError("Invalid (Negative) edge weight provided as argument.")
		else:
			self.adj_mat[start_vertex][end_vertex] = new_weight

	#adds an edge with WEIGHT to GRAPH between START_VERTEX & END_VERTEX
	def add_edge(self, start_vertex, end_vertex, weight):
		self.change_edge_weight(start_vertex, end_vertex, weight)

	
	#returns the children of VERTEX in GRAPH
	def children(self,vertex):
		ret_list = []
		if (vertex >= self.num_vertices or vertex < 0):
			#raise some error
			raise ValueError("Invalid vertex provided as argument.")
		else: 
			for ind in range(self.num_vertices):
				if (self.adj_mat[vertex][ind] != 0):
					ret_list.append(ind)
		return ret_list
	
	#returns the parents of VERTEX in GRAPH. 
	def parents(self, vertex):
		ret_list = []
		if (vertex >= self.num_vertices or vertex < 0):
			#raise some error
			raise ValueError("Invalid vertex provided as argument.")
		
		else: 
			for ind in range(self.num_vertices):
				if (self.adj_mat[ind][vertex] != 0):
					ret_list.append(ind)
			return ret_list

	#adds a child with CH_VERTEX_NUM to the vertex PARENT in graph with edge weight EDGE_WEIGHT
	def add_child(self, parent, ch_vertex_num, edge_weight):
		if (parent >= self.num_vertices or parent < 0) or (ch_vertex_num >= self.num_vertices or ch_vertex_num < 0):
			raise ValueError("Invalid vertex provided as argument.")
		else:
			self.adj_mat[parent][ch_vertex_num] = edge_weight
			return
	
	#prints graph in adjaceny matrix format
	def print_graph(self):
		print (self.adj_mat)
