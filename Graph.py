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
				#print(str(vertex) + " is list")
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

	
	def add_edge(self, v, w, weight=1, directed=True):
		'''Adds an edge from v to w if both v and w exist. If
		   directed=False, the edge also goes from w to v. The default
		   weight is 1, but can be specified'''
		if self._is_node(v) and self._is_node(w):
			self.adjacency_list[v].append((w, weight))
			if not directed:
				_weight = weight
				self.add_edge(w, v, _weight, True)
		else:
			if not self.__is_node(v):
				print("Node " + str(v) + " does not exist")
			if not self.__is_node(w):
				print("Node " + str(w) + " does not exist")

		

