# import numpy as np
# A = np.random.randn(4,3)
# B = np.sum(A, axis = 1, keepdims = True)
# print (B)

# def answer(s):
#     best = None
#     # lets try from len(subarray) n to 1
#     for i in range(len(s)):


#         length = len(s) / (i + 1)
#         print("length", len(s))
#         print (i)
#         print ("length", length)
#         succ = True
#         # print ("hello", length)
#         for j in range(len(s)):
#         	# print (j, j% length)

#             if s[int(j)] != s[int(j % length)]:
#             	print(s[int(j)], s[int(j % length)])
#             	succ = False
#             	break

   
                

#         if succ:
#             best = i + 1
#             print("best", best)

#     return best

# s = "abcabcc"
# print(answer(s))

a = 20
c = 10
b = c<a
print(b)