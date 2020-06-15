import hashlib
# def get_prefix(string):
#     if len(string) == 0:
#         return ''
    
#     string.sort() 
#     shortest = string[0] 
#     prefix = '' 
  
#     for i in range(len(shortest)): 
#         if string[len(string)-1][i] == shortest[i]: 
#             prefix += string[len(string)-1][i]
#         else:
#             break
      
#     return prefix


# string = ["start", "star" , "stair"]

# print(get_prefix(string))


class MySet:
  def __init__(self, size):
    self.size = size
    self.bucket = [ None for x in range(size) ]

  def values(self):
    set_data =""
    for i in range(self.size):
      if self.bucket[i] != None:
        set_data += self.bucket[i]
        set_data += ", "
    if set_data[-1] == " ":
      data_set = set_data[:-2]
    return data_set

  # 1. hash_value 함수
  def hash_value(self,key):
    hash_value = hashlib.sha1(key.encode())
    # hash_dig = hash_value.hexdigest()
    # hash_value = hash_obj.hexdigest()
    print(hash_value)

    
  
  # 2. add 함수
#   def add(self, key):
#     hash_value = self.hash_value(key)
    # 여기서 부터 구현
pr = MySet(16)

pr.hash_value('wecode')
