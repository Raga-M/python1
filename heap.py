import  heapq

g=[112,12,134,14,654,432,11]
print(min(g),max(g))
print (heapq.nlargest(3,g))
print (heapq.nsmallest(7,g))