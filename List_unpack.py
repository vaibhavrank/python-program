from itertools import chain
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_list = list(chain(*list_of_lists))

print(flat_list)
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_list = [item for sublist in list_of_lists for item in sublist]

print(flat_list)
from itertools import chain
listoflist=[[1,2,3],[4,5,6],[7,8,9]]
flatlist=list(chain(*listoflist))
print(flatlist)
listoflist=[[1,2,3],[4,5,6],[7,8,9]]
flatlist= [item for sublist in listoflist for item in sublist]
print(flatlist)