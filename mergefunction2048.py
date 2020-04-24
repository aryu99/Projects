"""
Merge function for 2048 game.
"""
# line = [2,2,2,2,2]

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    result = []
     
        # print (line)
        
    
    for num in line:
    	if num != 0:
    		result.append(num)

    if len(result) < len(line):
    	while len(result) < len(line):
    		result.append(0)
    # print (result)
    if len(result) <= 2:
        try:
            if result[0] == result[1]:
                result[0] = result[0] + result[1]
                result[1] = 0
                # print (type(result))
                return result
            else:
                return result
        except:
            return result
    print(result)
    i = 0
    while (i + 1) <= (len(line)-1): # if i +
        if result[i] == result[i + 1] and result[i] != 0:
            result.append(0)
            result[i] = result[i] + result[i + 1]
            print("before loop: ", result)
            x = 0
            for n in range((len(line) - 1) - i):             
                result[i + 1 + x] = result[i + 2 + x]
                x += 1
                print ("loop: ",result)
        else:
            pass
        i += 1
   
    while len(result) > len(line):
        result.pop()


            # for n in range(3 - i):
            #     x = 0
            #     result[i + x + 1] = result[i + x + 2] 
            #     x += 1
            #     print (result)
    print ("the result is:" ,result)
    return (result)

# print("answer", merge(line))