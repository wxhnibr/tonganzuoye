##函数说明

####1.quicMod(a,b,c)
该函数用来计算a^b%c，进行快速幂计算，快速幂算法将大数的求幂算法转化了小数求幂的乘法。可以利用一个引理：**积的取余等于取余的积的取余。**，来减少a和b规模，然后进行计算。  
例如计算7^16mod3，a=7.b=16,c=3，就等于(7%3)*(7%3).....,这样就减少了a的规模，计算相当于1*1*1....，然后减少b的规模，如果计算(7*7%^3)(7*7%3).....，这样就减少了b的规模，这样就可以快速计算出大数的摸。
####2.MillerRabin(n,num)
该函数来检测一个大数是否为素数,Miller-Rabin素性测试算法由两个定理引出，(1)费马定理：设p是素数，a是整数，且(a,p)=1,a^(p-1)=(1modp)。(2)二次探测定理：如果p是一个素数，且0<x<p,则有$x2=1(modp)$。  经一系列推导可得，**参考链接：https://blog.csdn.net/ECNU_LZJ/article/details/72675595。**
####3.excd(a,b,list)
贝组定理：如果a、b是整数，那么一定存在整数x、y是得ax+by=gcd(a,b)，如果ax+by=m有解，那么gcd(a,b)一定m的倍数，那么如果ax+by=1就有gcd(a,b)=1，可以利用辗转相除法计算这个公因数。当b=0,a=gcd(a,b)时，有a*1+b*0=gcd(a,b)，x=1,y=0，这时的a和b不是最开始的a和b，要求出a和b就要回到递归开始的式子，通过计算可得x=y1,y=x1-a/b*y1这样得到相邻两次递归就可以利用递归求解。**参考链接：https://blog.csdn.net/destiny1507/article/details/81750874**
####4.inverseMod(a,b)
利用扩展欧几里得算法求逆，求(a*x)%b=1，可以利用该函数求RSA的私钥，在已知e和s的情况下，求(e*d)%m=1，求解d，d即为rsa的私钥。
####5.generatePrime(num)
生成num个大素数，首先生成2-100000之间的素数列表L，生成素数在10^100和10^101之间，利用MillerRain判断生成素数是否为素数，然后利用生成的L，做除法判断生成的数是否为素数，返回一个素数列表，其中包含num个素数。
####5.generateKey()
生成RSA的公钥和私钥，首先生成两个大的素数p和q,令n=p*q，s=(p-1)(q-1)，选择一个与s互质的数为e=65537，利用inverseMod计算出d，然后得到公钥(n,e)，得到私钥(n,d)，计算快速幂摸计算m^e=c(modn)，c即为密文，利用私钥计算(c^d)=m(modb)，可得明文m。

  
参考链接:
https://blog.csdn.net/chroje/article/details/79477329?spm=1001.2101.3001.6650.3&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-3.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-3.pc_relevant_default&utm_relevant_index=6