table = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
         'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b',
         'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
         'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3',
         '4', '5', '6', '7', '8', '9', '+', '/']
#table = '@,.1fgvw#`/2ehux$~"3dity%_;4cjsz^+{5bkrA&=}6alqB*-[70mpC()]89noD'

#table=list(table)
def encode(s):  # 将字符串转化成二进制
    tmp = []
    for c in s:
        if 57 >= ord(c) >= 48:
            tmp.append('0')
            tmp.append(bin(ord(c)).replace('b', ''))
        else:
            tmp.append(bin(ord(c)).replace('b', ''))
    str_bin = ''.join(tmp)
    return str_bin


def decode(s):  # 将二进制转化为字符串
    bin_str = ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])
    return bin_str


def zh(rr):  # 将二进制转化为10进制
    ma = 0
    for a in range(0, 6):
        if rr[a] == '1':
            ma += pow(2, 5 - a)
    return ma


def zh2(rr):  # 将十进制转化为二进制
    tmp = []
    for i in range(0, 6):
        tmp.insert(0, '{}'.format(rr % 2))
        rr = int(rr / 2)
    str_bin = ''.join(tmp)
    return str_bin


def dz(zz) -> object:  # 依照base64的表将10进制转化为字符
    return table[zz]


def dz2(zz):  # 依照base64的表将字符转化为10进制
    for i in range(0, 64):
        if zz == table[i]:
            return i


def main1():  # 加密函数
    global xx
    a = input('请输入要加密的文本\n')
    r = list(a)
    x = encode(r)
    if len(x) % 6 == 0:
        bss = len(x) / 6
        bs = int(bss)
        for i in range(1, bs + 1):
            hh = x[0 + (i - 1) * 6: 6 + (i - 1) * 6:1]
            print(dz(zh(hh)), end="")
        return
    else:
        tt = len(x) % 6
        for i in range(1, 7 - tt):
            if i == 1:
                xx = '{}{}'.format(x, '0')
            else:
                xx = '{}{}'.format(xx, '0')
        bss = len(xx) / 6
        bs = int(bss)
        for i in range(1, bs + 1):
            hh = xx[0 + (i - 1) * 6: 6 + (i - 1) * 6:1]
            print(dz(zh(hh)), end="")
        if len(xx) % 8 == 4:
            print("==", end="")
        else:
            print("=", end="")
        print("\n")
        return


def main2():  # 解密函数
    a = input('请输入要解密的文本\n')
    a = a.replace('=', '')
    r = list(a)
    less = len(r)
    t = []
    for i in range(0, less):
        t.append(zh2(dz2(r[i])))
    tt = ''.join(t)
    less2 = len(tt)
    bs = int(less2 / 8)
    for i in range(1, bs + 1):
        hh = tt[0 + (i - 1) * 8: 8 + (i - 1) * 8:1]
        print(decode(hh), end="")
    print("\n")
    return


def main():
    while(1):
        s = eval(input("请选择要使用的功能，1代表加密，2代表解密,0代表退出\n"))
        if s == 1:
            main1()
            continue
        elif s == 2:
            main2()
            continue
        elif s == 0:
            return
        else:
            print('ERROR!\n')



main()
# base64加密原理：将字符串转化为二进制（依照ascll编码），一般一个字符在计算机中的储存是8个比特位，取6个比特位转化为10进制，按照base64表转化为字符就得到了密文，不足6位的补0并且在最后加等于号（具体视情况而定）
