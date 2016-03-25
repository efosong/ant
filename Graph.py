#TODO (maybe) : add ability for nodes to have values, and member functions to
#get/set these

class Graph(object):
	def __init__(self):
		'''Initialised an empty graph (i.e. no vertices or edges) '''
		self.vertex_list = []
		self.adjacency_list = {}



	def _is_node(self, v):
		'''Returns true if vertex v is in the graph'''
		if (v in self.vertex_list):
			return True
		else:
			return False

		

	def is_adjacent(self, v, w): 
		'''Returns true if there is an edge connecting vertex x to y in
		   the direction x -> y. Note that a vertex is not adjacent to
		   itself unless there is a loop at that vertex.'''
		if self._is_node(v) and self._is_node(w):
			if not self.adjacency_list[v]:
				return False
			if (w in list(zip(*self.adjacency_list[v]))[0]):
				return True
			else:
				return False
		else:   #Error statements
			print("Invalid vertex index")
			if self._is_node(v):
				pass
			else:
				print("Vertex " + str(v) + " does not exist")
			if self._is_node(w):
				pass
			else:
				print("Vertex " + str(w) + " does not exist")


	
	def get_neighbors(self, v):
		'''Returns a list of all vertices w such that there is an edge
		   v -> w'''
		try:
			return list(zip(*adjacency_list[v]))[0]
		except KeyError:
			print("Invalid vertex index")
			print("Vertex " + str(v) + " does not exist")



	def add_vertex(self, v): #TODO add requirement v is int (not important)
		'''Adds a vertex v to the graph if it does not already exist. If
		   it does exist, throws an error.
		   If v is a list, add each vertex within the list to the graph'''
		if type(v) is list:
			for vertex in v:
				self.add_vertex(vertex)
		else:
			try:
				if self._is_node(v):
					raise IndexError("Vertex " + str(v) + " exists already")
				elif v <= 0 or not (type(v) is int):
					raise IndexError("Index must be a positive integer")
				else:
					self.adjacency_list[v] = []
					self.vertex_list.append(v)
			except IndexError as msg: 
				print("Invalid vertex index")
				print(msg)
				print("Vertex was not added")



	def remove_vertex(self, v):
		'''Removes a vertex v and all the associated edges from the
		   graph, if the vertex v exists.'''
		if self._is_node(v):
			for vertex in self.vertex_list:
				if self.is_adjacent(vertex, v):
					self.remove_edge(vertex, v) 
			del self.adjacency_list[v]
			self.vertex_list.remove(v)
		else:
			print("Node " + str(v) + "does not exist")


	
	def add_edge(self, v, w, weight=1, directed=True):
		'''Adds an edge from v to w if both v and w exist. If
		   directed=False, the edge also goes from w to v. The default
		   weight is 1, but can be specified'''
		if self._is_node(v) and self._is_node(w) \
		     and not self.is_adjacent(v, w):
			self.adjacency_list[v].append((w, weight))
			if not directed:
				_weight = weight
				self.add_edge(w, v, _weight, True)
		else:
			if not self._is_node(v):
				print("Node " + str(v) + " does not exist")
			if not self._is_node(w):
				print("Node " + str(w) + " does not exist")
			if self._is_node(v) and self._is_node(w):
				print("Edge from " + str(v) + " to " + str(w)
				      + " already exists")

		

	def remove_edge(self, v, w, directed=True):
		'''Removes the edge from v to w if it exists. If directed=False,
		   the edge from w to v is also removed if it exists, or nothing
		   is removed if not'''
		if self.is_adjacent(v, w) and (directed or self.is_adjacent(w,v)):
			self.adjacency_list[v] = [i for i in self.adjacency_list[v] if i[0]!=w]
			if not directed:
				self.adjacency_list[w] = [i for i in self.adjacency_list[w] if i[0]!=v]
		else:
			print("Invalid edge")
			if not self.is_adjacent(v, w):
				print("Edge from " + str(v) + " to " + str(w) + " does not exist")
			if not directed and not self.is_adjacent(w,v):
				print("Edge from " + str(w) + " to " + str(v) + " does not exist")

	

	def get_edge_value(self, v, w):
		'''Gets the value associated with the edge from v to w'''
		if self.is_adjacent(v,w):
			return  [i for i in self.adjacency_list[v]].pop()[1]
		else:
			print("Invalid edge")
			print("Edge from " + str(v) + " to " + str(w) + " does not exist")



	def set_edge_value(self, v, w, val):
		'''Sets the value associated with the edge from v to w, if the
		   edge already exists'''
		if self.is_adjacent(v,w):
			self.remove_edge(v,w)
			self.add_edge(v, w, val)
		else:
			print("Invalid edge")
			print("Edge from " + str(v) + " to " + str(w) + " does not exist")
