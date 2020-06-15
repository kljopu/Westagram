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


def romanToNum(s):
    result=1
    num_list = ['I','V','X','L','C','D','M','IV','IX','XL','XC','CD','CM']
    for i in  num_list:
        if i = 'I':
            count_i = 0
    
    

s = 'CD'

print(romanToNum(s))

# for i in num_list:
        
#         if i in s:
            
            # I= 1
            # V= 5
            # X= 10
            # L= 50
            # C= 100
            # D= 500
            # M= 1000

            # IV = 4
            # IX =9
            # XL = 4
            # XC =90
            # CD = 400
            # CM = 900
            # print(i)
    # return result