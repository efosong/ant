class Graph(object):
	def __init__(self):
		'''Initialised an empty graph (i.e. no vertices or edges) '''
		self.vertex_list = []
		self.adjacency_list = {}
		self.value_list = {}


	def _is_node(self, v):
		'''Returns true if vertex v is in the graph'''
		if (v in self.vertex_list):
			return True
		else:
			return False
		

	def is_adjacent(self, v, w): 
		'''Returns true if there is an edge connecting nodes x to y in
		   the direction x -> y'''
		if self._is_node(v) and self._is_node(w):
			if (w in self.adjacency_list[v]):
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
			return adjacency_list[v]
		except KeyError:
			print("Invalid vertex index")
			print("Vertex " + str(v) + " does not exist")
			


	def add_vertex(self, v): #TODO add requirement v is int (not important)
		'''Adds a vertex v to the graph if it does not already exist. If
		   it does exist, throws an error'''
		try:
			if self._is_node(v):
				raise IndexError
			else:
				self.adjacency_list[v] = []
				self.vertex_list.append(v)
		except IndexError: 
			print("Invalid vertex number")
			print("Vertex " + str(v) + " exists already")
			print("Vertex was not added")

	
		

