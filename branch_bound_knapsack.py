from knapsack_LP import *
import queue as Q


#returns the OBJ_INDEX in SOL_SET that has a fractional value.
def find_fractional(sol_set):
	for tup in sol_set:
		if (tup[1] != 0 and tup[1] != 1):
			return tup[0]

	return None; 

#returns TRUE if sol_set represents a leaf node, FALSE otherwise
def is_leaf(sol_set):
	for tup in sol_set:
		if (tup[1] != 0 and tup[1] != 1):
			return False

	return True



#calculates the total value of knapsack 
def calculate_value(sol_set, VW):
	total_value = 0
	values_list = list(map(lambda tup: (tup[0], tup[1]),VW))

	for tup in sol_set:
		total_value = total_value + tup[1]*get_value(values_list,tup[0])
	return total_value



def branch_and_bound(VW,C):
	#set curr_sol to be empty, max_obs_obj_value = 0
	curr_sol = []
	max_obs_obj_value = 0
	#solve LP relaxation at the root node
	lp_result = knapsack_LP(VW,C)
	print(lp_result)
	#compute knapsack value
	lp_result_val = calculate_value(lp_result[0], VW)
	#initialize priority queue
	PQ = Q.PriorityQueue()
	#add root node to the PQ
	PQ.put((-1*lp_result_val,lp_result))
	#loop until the PQ is empty
	while not PQ.empty():
		#pop a node from the PQ
		curr_sol_tup = PQ.get()
		print("Popped Node:",curr_sol_tup)
		print("Max. obs. obj value", max_obs_obj_value)
		#check if LP solution is entirely integral (leaf node) and if its obj_value > curr_sol: 
		#if so, set max_obs_obj_value to be this obj_value, and save the decision variable values.
		if is_leaf(curr_sol_tup[1][0]):
			if(-1*curr_sol_tup[0] > max_obs_obj_value):
				max_obs_obj_value = -1*curr_sol_tup[0]
				curr_sol = curr_sol_tup[1]
			continue;
		#branch on curr_sol_tup if UB is higher than curr_sol and add children to PQ, after solving for their LP_relaxation. 

		
		#find the object index that is fractional (i.e. needs to be branched on)
		frac_index = find_fractional(curr_sol_tup[1][0])
		#a list of object_indices that Must be Included in the solution (value = 1)
		mi = curr_sol_tup[1][1] + [frac_index]
		#a list of object_indices that Must be Not Included in the solution (value = 0)
		mni = curr_sol_tup[1][2] + [frac_index]
		#produce child #1 (that has to contain the fractional object)
		child1 = knapsack_LP(VW,C,mi,[])
		child1_bound = calculate_value(child1[0],VW)
		#add child #1 to the priority queue if its upper bound is greater than the current observed max objective value
		if (child1_bound > max_obs_obj_value):
			PQ.put((-1*child1_bound,child1))
			print((child1_bound, child1))
		#produce child #2 (that does not contain the fractional object)
		child2 = knapsack_LP(VW,C,[],mni)
		child2_bound = calculate_value(child2[0],VW)
		#add child #2 to the priority queue if its upper bound is greater than the current observed max objective value
		if (child2_bound > max_obs_obj_value):
			PQ.put((-1*child2_bound,child2))
			print((child2_bound, child2))
		print()
			
	#when the loop stops executing, simply return the most optimal curr_sol observed so far.
	return curr_sol



