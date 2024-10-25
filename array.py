import array as arr
array_num = arr.array('i', [1,3,5,2,3,7])
print("Original array: " +str(array_num))
print("Number of the occurances of the numebr 3 in the said array:"+str(array_num.count(3)))
array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))