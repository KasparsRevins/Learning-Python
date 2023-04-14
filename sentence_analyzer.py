def sentence_analyzer(sentence):
  solution = {}
  for char in sentence:
    if char != ' ':
      if char in solution:
       solution[char] += 1
      else:
       solution[char] = 1
      
  return solution
  
sentence_analyzer("Pythonn")