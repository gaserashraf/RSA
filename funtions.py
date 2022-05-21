import math

#this function take an string in base 256 and convert it to base 10
def ConvertToInt(message_str):
    numBase10 = 0
    for i in range(len(message_str)):
        numBase10 = numBase10 * 256 + ord(message_str[i])
    return numBase10

#this function take an string in base 256 and max block size and convert it to an array of base 10 number x <= max block size
def ConvertToIntBlocks(message_str,mxBlockSize):
    res = 0
    arr = []
    for i in range(len(message_str)):
        if(res*256+ord(message_str[i])<=mxBlockSize):
            res = res * 256 + ord(message_str[i])
        else:
            arr.append(res)
            res = ord(message_str[i])
    if(res):
        arr.append(res)
    return arr

#this function take an int in base 10 and convert it to string base 256
def ConvertToStr(n):
    str = ""
    while n > 0:
        str += chr(n % 256)
        n //= 256
    return str[::-1]

#sample GCD funtion
def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

#sample ExtendedEuclid funtion
def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return (y, x - k * y)


# this is an R2L recursive implementation that works for large integers
def PowMod(a, n, mod):
    if n == 0:
        return 1 % mod
    elif n == 1:
        return a % mod
    else:
        b = PowMod(a, n // 2, mod)
        b = b * b % mod
        if n % 2 == 0:
            return b
        else:
            return b * a % mod


def InvertModulo(a, n):
    (b, x) = ExtendedEuclid(a, n)
    if b < 0:
        b = (b % n + n) % n 
    return b


# msg must be a string 
def Encrypt(m, n, e):
    # Encryption c = (msg ^ e) % n

    # convert each msg to block <= n-1 
    msgs = ConvertToIntBlocks(m,n-1)
    arrCipher=[]
    for msg in msgs:
        # enctpy each block
        enctpyted = PowMod(msg, e, n)
        c = str(enctpyted)
        arrCipher.append(c)
    return arrCipher


def Decrypt(c, p, q, e):
    # Decryption m = (c ^ d) % n
    # Now calculate Private Key, d :
    # Φ(n) = (p - 1) * (q - 1)
    # d = (k*Φ(n) + 1) / e for some integer k

    #decrpt each block <= n-1
    msg = c
    phi = (p - 1) * (q - 1)
    # d * e == 1 modulo (p-1)(q-1)
    d = InvertModulo(e, phi) # private key
    n = p * q
    dectpyted = PowMod(msg, d, n)
    m = ConvertToStr(dectpyted)
    return m

def writeCipherArrayInFile(arr,fileName):
  with open(fileName, 'a') as f:
      for item in arr:
          f.write("%s " % item)
      f.write("\n")
def writeOutputArrayInFile(arr,fileName):
    with open(fileName, 'a') as f:
        for item in arr:
            f.write("%s" % item)
        f.write("\n")