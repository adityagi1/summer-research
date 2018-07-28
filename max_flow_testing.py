from ford_fulk import *
import numpy as np
from data_structures import *
#testing the bfs function & overall data structure functionality

#define the first test graph [PASSING TEST CASE] 
test_arr1 = np.array([[0,3,3,0,0,0],[0,0,2,3,0,0],[0,0,0,0,2,0],[0,0,0,0,4,2],[0,0,0,0,0,3],[0,0,0,0,0,0]])
test_graph1 = Graph(6,test_arr1)
print("Max flow for Graph 1 is:",edm_karps(test_graph1,0,5),"; Expected Output is: 5")
#max. flow should be 5 units and program should output 5.
#LINK TO GRAPH REPRESENTATION FOR TEST_GRAPH1:
#https://en.wikipedia.org/wiki/Maximum_flow_problem#/media/File:Max_flow.svg

#define the second test graph [FAILING TEST CASE]
test_arr2 = np.array([[0,3,0,3,0,0,0],[0,0,4,0,0,0,0],[3,0,0,1,2,0,0],[0,0,0,0,2,6,0],[0,1,0,0,0,0,1],[0,0,0,0,0,0,9],
	[0,0,0,0,0,0,0]])
test_graph2 = Graph(7,test_arr2)
print("Max flow for Graph 2 is:", edm_karps(test_graph2,0,6), "; Expected Output is: 5")
#max flow should be 5 units, but for some reason program is outputting 8!. 
#LINK TO GRAPH REPRESENTATION FOR TEST_GRAPH2:
#https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm#/media/File:Edmonds-Karp_flow_example_0.svg