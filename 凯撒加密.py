#_*_coding:UTF-8_*_
def jiami(mingwen):
    ll = len(mingwen)
    for ii in range(1,27):
        print("移位为{}位:\n".format(ii))
        for zz in range(ll):
            ii %= 26
            xx = ord(mingwen[zz])
            if 65<= xx<= 90:
                if ii <= 90-xx:
                    xx += ii
                elif ii > 90-xx:
                    xx = 65+ii-(90-xx+1)
                ss = chr(xx)
                print(ss, end="")
                continue
            if 97 <= xx <= 122:
                if ii <= 122 - xx:
                    xx += ii
                elif ii > 122 - xx:
                    xx = 97+ii-(122-xx+1)
                ss = chr(xx)
                print(ss, end="")
                continue
        print("\n")
a = input("请输入你要转换的字符串，目前只支持字母\n")
r = list(a)
jiami(r)
