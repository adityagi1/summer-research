#import necessary libraries
import numpy as np
from data_structures import *



#write a breadth first search algorithm that returns a MST
#returns a minimum spanning tree for the graph G
def bfs(g, start_vertex):
	q = Queue()
	mst = Graph(g.size(), np.zeros((g.size(),g.size())))
	q.enqueue(start_vertex)
	visit_list = []
	#repeat until queue is empty
	while not(q.empty()):
		#get top vertex from queue
		current_vertex = q.dequeue()

		#visit this vertex (add its children to queue if they are not already in queue and have not already been visited)
		ch_list = g.children(current_vertex)
		for ch in ch_list:
			if ch not in visit_list and not(q.contains(ch)):
				q.enqueue(ch)
				mst.add_child(current_vertex, ch, 1)
		#mark vertex as visited by adding to visited_list
		visit_list.append(current_vertex)

	return mst


#edmunds-karp algorithm to find the max. flow of the graph using bfs.
def edm_karps(g, start_vertex, end_vertex):
	#repeat until there are no more augmenting paths
	while (has_aug_path(g, end_vertex)):
		#obtain the MST using the bfs function
		mst = bfs(g, start_vertex)
		#obtain shortest s-t path from the mst returned by the BFS
		sp = get_sp(mst, end_vertex)
		#identify min_capacity on SP path
		flow = get_bottleneck_cap(g,sp)
		#send flow along the path equal to bottleneck capacity
		g = send_flow(g,sp, flow)
	
	#return total flow (sum of reverse edges going into source)
	max_flow = get_total_flow(g, start_vertex)
	return max_flow

#SEVERAL HELPER FUNCTIONS USED ABOVE ARE DEFINED BELOW THAT WERE USED IN THE ABOVE 
#EDMUNDS-KARP IMPLEMENTATION


#true if there is an augmenting path in the residual graph G.
def has_aug_path(g, sink_vertex):
	#run a bfs on g
	res_mst = bfs(g, 0)
	#there is an augmenting path if there are no edges going outwards or coming into the sink in the mst
	if (res_mst.children(sink_vertex) == [0]*len(res_mst.children(sink_vertex)) and 
		res_mst.parents(sink_vertex) == [0]*len(res_mst.parents(sink_vertex))):
		return False
	#otherwise there must be an augmenting path
	else: 
		return True 


#takes an MST TREE and returns the shortest path to SINK_VERTEX as a list of vertices on path.
def get_sp(tree, sink_vertex):
	sp_list = []
	curr_vertex = sink_vertex
	#repeat until you get the source (source in MST is characterized as having no parents)
	while tree.parents(curr_vertex) != []:
		#add curr_vertex to shortest path at beginning of path/list
		sp_list.insert(0,curr_vertex)
		#get parent vertex for curr_vertex in the MST. will be a single-element list.
		curr_vertex = tree.parents(curr_vertex)[0]
	#insert the source vertex into path
	sp_list.insert(0,0)
	return sp_list


#gets the bottleneck capacity on path rep. by SP_LIST for GRAPH
def get_bottleneck_cap(graph, sp_list):
	edge_weights = []
	#iterate over all vertices in sp_list except last
	for index in range(len(sp_list) - 1):
		 start_vertex = sp_list[index]
		 end_vertex = sp_list[index + 1]
		 edge_weights.append(graph.get_edge_weight(start_vertex, end_vertex))

	return min(edge_weights)

#sends flow F along PATH in GRAPH by reducing appropriate edge capacities 
# and adding reverse edges along path. returns updated residual graph. 
def send_flow(graph, path, f):
	ret_graph = graph
	#iterate over all vertices in path except last
	for index in range(len(path) - 1):
		start_vertex = path[index]
		end_vertex = path[index + 1]
		curr_fw_edge_weight = ret_graph.get_edge_weight(start_vertex, end_vertex)
		ret_graph.change_edge_weight(start_vertex, end_vertex, curr_fw_edge_weight - f)
		curr_rev_edge_weight = ret_graph.get_edge_weight(end_vertex, start_vertex)
		ret_graph.add_edge(end_vertex, start_vertex, curr_rev_edge_weight + f)

	return ret_graph


#returns the total outgoing flow from source by adding the total capacity of edges
#incident on source

def get_total_flow(graph, source_vertex):
	#get parents of source vertex
	parent_list = graph.parents(source_vertex)
	#get edge capacities of all edges incident on source vertex & sum to obtain total flow
	return sum([graph.get_edge_weight(parent_vertex, source_vertex) for parent_vertex in parent_list])
	






