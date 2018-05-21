import string
def digital_root(n):
    # ...
    sum = 0
    length = len(str(n))
    print("length=",length)
    temp = n
    temp0 = 0
    for i in range(0,length):
        num = temp//pow(10,length-i-1)
        temp0 = temp0 + num*pow(10,length - i -1)
        temp = n - temp0
        print("num=",num)
        sum = sum + num
    return sum
def get_middle(s):
    #your code here
    length = len(s)
    if length%2 == 1:
        s0 = s[length//2]
    else:
        s0 = s[length//2-1]+s[length//2]
    return s0
def add_binary(a,b):
    #your code here
    sum = a + b
    sum_binary = bin(sum)
    s = str(sum_binary)
    return s
def  change(n):
    result = '0'
    if n == 0:    # 输入为0的情况
        return result
    else:
        result = change(n // 2)         # 调用自身
        return result + str(n % 2)
def create_phone_number(n):
    #your code here
    data = n
    s = str(data)
    s1 = ""
    s2 = ""
    #nums = string.digits
    for x in s:
        #if x in nums:
        if x.isdigit():
            s1 = s1 +x
    s2 = '(' + s1[0] + s1[1] +s1[2] + ')' + ' ' + s1[3] + s1[4] + s1[5] + '-' + s1[6] + s1[7] + s1[8] + s1[9]
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
    return s2


def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    root = sq**0.5
    if root.is_integer():
        return int((root+1)**2)
    return -1
def friend(x):
    #Code
    s = x
    lis = []
    i = 0
    for x in s:
        if len(x) == 4:
            lis.append(x)
    return lis
def friend2(x):
  return [i for i in x if len(i) == 4]
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")
#print(digital_root(10246))
#print("s0=",get_middle("abcdoe"))
#print("s=",add_binary(127,1))
#print("s=",change(128))
print("s=",create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
#print("s=",find_next_square(121))
#print("s=",friend( ["Ryan", "Kieran", "Jason", "Yous"]))
#print("s=",friend2( ["Ryan", "Kieran", "Jason", "Yous"]))
print("s=",disemvowel("hello, i LOVE YOU"))