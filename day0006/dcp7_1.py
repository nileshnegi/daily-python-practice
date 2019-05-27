#Daily Coding Problem #7 [Medium]
#Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#You can assume that the messages are decodable. For example, '001' is not allowed.
def num_decode(msg):
    count = 1
    if(len(msg) > 1):
        for i in range(len(msg)-1):
            if(int(msg[i]+msg[i+1]) < 27):
                count = count + num_decode(msg[i+2:])
    
    return count
                          
print(num_decode('12321'))
print(num_decode(''))
