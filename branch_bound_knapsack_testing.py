import numpy as np
from knapsack_LP import *
from branch_bound_knapsack import *


test_list = [(1,3,5),(2,6,1),(3,9,10),(4,7,4),(5,8,3)]
results = branch_and_bound(test_list,15)[0]

#separate values & weights
test_weights = list(map(lambda tup:(tup[0],tup[2]),test_list))
test_values = list(map(lambda tup: (tup[0], tup[1]),test_list))



#compute the total value, weight associated with the selection.
total_value = 0
total_weight = 0
for tup in results:
	total_value = total_value + tup[1]*get_value(test_values,tup[0])

for tup in results:
	total_weight = total_weight + tup[1]*get_value(test_weights,tup[0])

#print results
print("TOTAL VALUE: ", total_value,"\n")
print("TOTAL WEIGHT: ", total_weight,"\n")
for obj_tup in results:
	print("Object Index: ",obj_tup[0],"   Decision Variable Value: ", obj_tup[1])
