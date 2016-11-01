def words(string):
  #eliminates white spaces from string, caters for both upper ad lower cases
  my22 = string.split() #| string.upper().split
  #initializing an empty dictionary for final value
  my_dict = {}
  wordset = set(my22)
  for word in wordset:
      count = 0
      for item in my22:
        if word == item:
          count = count + 1
          if word.isdigit() == True:
            word = int(word)
      my_dict[word] = count
  return my_dict