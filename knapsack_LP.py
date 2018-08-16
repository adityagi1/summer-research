import numpy as np
#ASSUMES THAT A TRIVIAL SOLUTION IS NOT POSSIBLE (i.e. capacity is so large, that all objects may be included.)

#given a list VW containing tuples of the form (object_index, value, weight), 
#a weight_capacity C, return the fractional values of the decision variables in a list
#containing tuples of the form (object_index, decision_variable_value).
def knapsack_LP(VW, C):
	ratio_list = []
	#compute a new list containing containing tuples of the form (object_index, value-to-weight ratio)
	for tup in VW:
		ratio_list.append((tup[0],tup[1]/tup[2]))
	weights = list(map(lambda tup:(tup[0],tup[2]),VW))
	values = list(map(lambda tup: (tup[0], tup[1]),VW))
	#determine k+1 objects where the first k objects may be included in entirety and the k+1th object
	#overshoots the weight limit	
	object_list = add_objects(weights, ratio_list,C)
	
	#for the k+1 object, determine d (the difference between the existing sum of weights and the capacity),
	# and let x_k+1 = d/w_k+1
	sum_of_weights = sum([get_value(weights,key) for key in object_list[0:len(object_list) - 1]])
	d = C - sum_of_weights
	#create a ret_list containing tuples of the required form 
	ret_list = []
	for obj_tup in VW:
		#if the object is to be added to the knapsack
		if (obj_tup[0] in object_list):
			#if the object is to be added only partially to the knapsack (i.e. the last object in object_list)
			if(obj_tup[0] == object_list[-1]):
				ret_list.append((obj_tup[0],min(1,d/get_value(weights, obj_tup[0]))))
			#otherwise the object is being added to the knapsack in its entirety
			else:
				ret_list.append((obj_tup[0],1))

		#if the object is not to be added to the knapsack
		else:
			ret_list.append((obj_tup[0],0))
	#return the required results
	return ret_list

#returns a list of objects_indices that are to be added to the knapsack, with the last index being of the object 
#whose addition to the knapsack would result in the total weight overshooting the total capacity 
#RATIO_LIST contains tuples of the form (object_index,value-to-weight ratio)  
def add_objects(W, ratio_list, cap):
	obj_list = []
	#sort the ratio_list
	sorted_ratio_list = sorted(ratio_list,key = lambda tup: tup[1], reverse = True)
	current_total_weight = 0  
	object_index = 0
	while current_total_weight < cap:
		#if no more objects are left in the sorted_ratio_list, then break loop. 
		if (len(sorted_ratio_list) == 0):
			break;
		object_index = sorted_ratio_list.pop(0)[0]
		current_total_weight = current_total_weight + get_value(W, object_index)
		obj_list.append(object_index)

	return obj_list

#searches the LIST of TUPLES in (key, value) form and returns the value with KEY=SEARCH_KEY
#returns a NONE if the tuple with required SEARCH_KEY is not present in LST.
def get_value(lst, search_key):
	lst_index = 0
	while (lst_index < len(lst)):
		if (lst[lst_index][0] == search_key):
			return lst[lst_index][1]
		lst_index = lst_index + 1
	return None 

