def find_max_min(list1):
  #checks equality of variables
  if all(i == list1 [0] for i in list1) == True: 
    list2 = []
    list2.append(len(list1))
    #returns length of list
    return list2
  else:
    maximum = max(list1) 
    minimum = min(list1)
    #creates an empty list to hold the maximum and minimum values of list1
    mxmn = []                   
    mxmn.append(minimum) #appends the minimum value for list1 onto the blank list
    mxmn.append(maximum) #appends the maximum value for list1 onto the blank list
    return mxmn