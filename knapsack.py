def knapsack(W, wt, val, n): 
	gain = 0
	
	ratio = [0 for i in range(n)] 
	for i in range(n): 
		ratio[i] = val[i]/wt[i] 
	
	for i in range(n): 
		for j in range(i+1, n): 
			if ratio[i] < ratio[j]: 
				ratio[i], ratio[j] = ratio[j], ratio[i] 
				val[i], val[j] = val[j], val[i] 
				wt[i], wt[j] = wt[j], wt[i] 
	
	for i in range(n): 
		if wt[i] <= W: 
			gain += val[i] 
			W -= wt[i] 
		
	
	return gain

profit=[10,5,7,9,3,4]
weight=[2,3,5,3,4,1]
W = 5

n = 6
print(knapsack(W, weight, profit, n))