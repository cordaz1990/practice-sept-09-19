#List Comprehensions
def capitalize_all(t)
    res = []
    for s in t:
      res.append(s.capitalize())
    
    return res
  
  
def capitalize_all(t):
    return[s.capitalize() for s in t]
  

def only_upper(t):
    res = []
    for s in t:
      if s.isupper():
         res.append(s)
      
      return res
