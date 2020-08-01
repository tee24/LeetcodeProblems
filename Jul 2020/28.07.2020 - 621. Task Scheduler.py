class Solution:
    def leastInterval(self, tasks, n):
    	count = {}
    	for i in tasks:
    		if i in count:
    			count[i]+=1
    		else:
    			count[i]=1

    	items = sorted(list(count.keys()), key=lambda x: -count[x])

    	max_freq = count[items[0]]

    	frequency = 0

    	for x in items:
    		if count[x]==max_freq:
    			frequency+=1

    	return max((max_freq-1)*(n+1)+frequency, len(tasks))

#Consider AAABBBCC,2 -> AXX|AXX|AXX -> ABC|ABC|ABX -> 8 & AAB, 2 -> ABX|A -> 4
from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        frequency = Counter(tasks)
        max_freq = frequency.most_common(1)[0][1]
        number_max_frequency = sum([frequency[key] == max_freq for key in frequency])
        return max((max_freq-1)*(n+1)+number_max_frequency, len(tasks))

#Space, Time = O(1), O(n)


