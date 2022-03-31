import random
import math

#快速幂模算法，减小计算量
def quickMod(a,b,c):
    #计算a^b%c，使用该算法减少运算量
    a = a % c
    #res用来返回结果
    res = 1
    while b!=0:
        if(b%2!=0):
            res = (res*a)%c
        b = b // 2
        a = (a%c) * (a%c)
    return res


#MillerRabin检测是否为素数
def MillerRabin(n,num):
    #n为待检测的数，num为检测的次数
    if n==1:
        return False
    if n == 2:
        return True
    if n/2 == 0:
        return False
    #k用来记录运用了几次 二次探测定理
    k = 0
    #n位正素数,q必为偶数，并且q可以表示为2^m * q
    q = n-1
    #计算q和k
    #当q是偶数时
    while not (q&1):
        q =  q//2
        k = k + 1
    
    for i in range(num):
        #flag用来标志该数是否为素数
        flag = True
        #随机生成2到n-2的整数
        a = random.randint(2,n-1)
        #使用快速幂摸算法算出结果，根据二次探测定理判断最后形式的值
        res = quickMod(a,q,n)
        #判断是否符合二次探测定理
        if(res == 1 or res == n-1):
            flag = False
        #判断是否符合a^(q*2j)modn是否满足二次探测定理
        else:
            for j in range(k):
                res = (res*res)%n
                if res == n-1 or res == 1:
                    flag = False
                    break
        if flag:
            return False
    return True

#扩展欧几里得算法
def excd(a,b,list):
    #x和y分别为解
   #list中包含两个元素，list[0]代表x，list[1]代表y,list[2]代表gcd
    if b == 0:
       list[0] = 1
       list[1] = 0
       list[2] = a
    else:
        excd(b,a%b,list)
        temp = list[0]
        list[0] = list[1]
        list[1] = temp- a//b*list[1]

#由扩展欧几里得算法求模反元素
def inverseMod(a,b):
    list = [0,0,0]
    if a<b:
        a,b = b,a
    excd(a,b,list)
    if list[1]<0:
        list[1] = a + list[1]
    return list[1]

#判断n是否为素数
def judgePrime(n):
    temp = int(math.sqrt(n))
    for i in range(2,temp+1):
        if n%i==0:
            return False
    return True

#遍历返回(begin,end)只见那的素数
def primeList(begin,end):
    p = []
    for i in range(begin,end):
        if judgePrime(i):
            p.append(i)
    return p
#多重判断该数是否为素数        
def addJudge(n,array):
    for a in array:
        if n%a==0:
            return False

    return True

#用来生成两个大素数
def generatePrime(num):
    L = primeList(2,100000)
    prime = []
    while len(prime)<num:
        n = random.randint(pow(10,100),pow(10,101))
        if n%2 == 1:
            #双重条件判断是否为素数
            if addJudge(n,L) and MillerRabin(n,8):
                if n not in prime:
                    prime.append(n)
    return prime

#生成密钥
def generateKey():
    prime = generatePrime(2)
    p = prime[0]
    q = prime[1]
    #要求p和q不能相等
    while p == q:
        prime = generatePrime(2)
        p = prime[0]
        q = prime[1]
    n = p * q
    s = (p-1)*(q-1)
    #取e为65535
    e = 65537
    #扩展欧几里得求模反元素
    d = inverseMod(e,s)
    print ("p = ", p, ",q = ", q)
    print ("n = ", n)
    print ("e = ", e, ",d = ", d)   
    #公钥
    pk = [n,e]
    #私钥
    sk = [n,d]
    rsaKey = {}
    rsaKey['pk'] = pk
    rsaKey['sk'] = sk
    return rsaKey


if __name__ == '__main__':
    #生成秘钥
    rsaKey = generateKey()
    #公钥
    pk =rsaKey ['pk']
    #私钥
    sk = rsaKey['sk']                             
    #密文
    message = int(input("请输入要加密的数:"))
    #加密
    encryptionMsg = quickMod(message,pk[1],pk[0])
    print("密文为",encryptionMsg)
    #解密
    msg = quickMod(encryptionMsg,sk[1],sk[0])
    print('解密后的明文为:',msg)
    



    
