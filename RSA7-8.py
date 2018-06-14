import os, random, base64, time


def powmod(m, e, n):  # 不知道自带的pow也能这样搞,心态大崩
    c = 1
    e = bin(e)[2:]
    k = len(e)
    for i in range(k):
        c = c ** 2 % n
        if e[i] == '1':
            c = c * m % n
    return (c)


def miller(n, a, m, t):
    b = powmod(a, m, n)
    if b == 1 or b == (n - 1):
        return True
    for i in range(t - 1):
        b = powmod(b, 2, n)
        if b == (n - 1):
            return True
    return False


def MR(p, k):
    pAss = False
    block = []
    for i in range(k):
        block.append(random.randint(2, p - 2))
    m = p - 1
    t = 0
    while not m % 2:
        m = m // 2
        t += 1
    for a in block:
        pAss = miller(p, a, m, t)
        if not pAss:
            return False
    return True


def prime():
    while True:
        p = random.randrange(0x80000001, 0xFFFFFFFF, 2)  # 直接生成奇数,提高效率
        if MR(p, 9):
            break
    return p


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)  # g为公因子
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if (g != 1):
        print('modular inverse does not exist')
    else:
        return x % m


def RSAbulid():
    p = prime()
    q = prime()
    n = p * q
    fai = (p - 1) * (q - 1)
    e = 65537
    d = modinv(e, fai)
    print('\n p=', p, '\n q=', q, '\n N=', n, '\nΦ=', fai, '\n e=', e, '\n d=', d)
    return (e, d, n)


def MessageDiv(A, Inv):
    blk = []
    if Inv == '2':
        for i in range(len(A) // 8):
            blk.append(
                (A[0] << 0x38) + (A[1] << 0x30) + (A[2] << 0x28) + (A[3] << 0x20) + (A[4] << 0x18) + (A[5] << 0x10) + (
                A[6] << 0x8) + A[7])
            A = A[8:]
    else:
        if (len(A)) % 7 != 0:
            A = A + bytes(7 - (len(A)) % 7)
        for i in range(len(A) // 7):
            blk.append(
                (A[0] << 0x30) + (A[1] << 0x28) + +(A[2] << 0x20) + (A[3] << 0x18) + (A[4] << 0x10) + (A[5] << 0x8) + A[
                    6])
            A = A[7:]
    return blk


def RSA(message, k, n, Inv):
    block = MessageDiv(message, Inv)
    data = []
    for i in block:
        data.append(powmod(i, k, n))
    text = []
    for i in data:
        A = i
        if Inv != '2':
            text.append((A >> 0x38) % 0x100)
        text.append((A >> 0x30) % 0x100)
        text.append((A >> 0x28) % 0x100)
        text.append((A >> 0x20) % 0x100)
        text.append((A >> 0x18) % 0x100)
        text.append((A >> 0x10) % 0x100)
        text.append((A >> 0x8) % 0x100)
        text.append(A % 0x100)
    text = bytes(text)
    return text


Inv = input('请选择:1.加密 2.解密:')
choose = input('请选择编码:1.utf-8 2.unicode 3.GBK:')
if choose == '2':
    EnCo = 'unicode_internal'
elif choose == '3':
    EnCo = 'GBK'
else:
    EnCo = 'utf-8'

start = time.clock()

if Inv == '2':
    t1 = time.clock()
    k = int(input('\n请输入解密钥:'))
    n = int(input('请输入模数:'))
    Message = bytes(input('\n请输入base64格式的密文:'), encoding='ascii')
    Message = base64.b64decode(Message)
else:
    k, d, n = RSAbulid()
    print('\n请保管好密钥组: < d , N > = <', d, ',', n, '>\n')
    t1 = time.clock()
    Message = bytes(input('请输入明文:'), encoding=EnCo)

t2 = time.clock()
text = RSA(Message, k, n, Inv)

if Inv == '1':
    text = base64.b64encode(text)
    text = str(text, encoding="ascii")
else:
    text = str(text, encoding=EnCo)

ans = ['\n密文(以base64形式输出):\n', '\n明文:']
print(ans[int(Inv) - 1], text)

end = time.clock()
print("\n\n构建耗时 %f秒" % (t1 - start))
print("加解密耗时 %f秒" % (end - t2))
print("运算总耗时 %f秒" % (end - t2 + t1 - start))

os.system("PAUSE")