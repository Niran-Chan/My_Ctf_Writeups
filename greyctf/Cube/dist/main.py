from Crypto.Util.number import bytes_to_long, getPrime, isPrime

#FLAG = <REDACTED>
FLAG = b"greyctf{...}"

def gen(n):
    while True:

        #p = getPrime(n - 1) * 2 + 1
        p = 147271787827929374875021125075644322658199797362157810465584602627709052665153637157027284239972360505065250939071494710661089022260751215312981674288246413821920620065721158367282080824823494257083257784305248518512283466952090977840589689160607681176791401729705268519662036067738830529129470059752131312559
        print("Searching for prime number...\t",p)
        if (isPrime(p)):
            print("[+] Found a prime number! : ",p);

            return p

def cube(m, n, p):
    res = m
    for i in range(n):
        temp = res
        res = (res * res * res) % p
        if temp == res:
            print("Index of Breakage : " , i)
            break
        print("Progress:\t ",i/n * 100,"%")
    return res

p = gen(1024)
m = bytes_to_long(FLAG)
c = cube(m, 2 ** 100, p)

print(p)
print(c)

# p = 147271787827929374875021125075644322658199797362157810465584602627709052665153637157027284239972360505065250939071494710661089022260751215312981674288246413821920620065721158367282080824823494257083257784305248518512283466952090977840589689160607681176791401729705268519662036067738830529129470059752131312559
# c = 117161008971867369525278118431420359590253064575766275058434686951139287312472337733007748860692306037011621762414693540474268832444018133392145498303438944989809563579460392165032736630619930502524106312155019251740588974743475569686312108671045987239439227420716606411244839847197214002961245189316124796380