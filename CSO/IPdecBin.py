ip = input('Enter IP address in decimal or binary: ')

ip_in_lst = ip.split(sep = '.')
ip_res = []

''' Преобразование в соответсвующую систему исчисления'''
for i in ip_in_lst:
    if len(i) <= 3:
        i = int(i)
        octet = []
        for l in range(0,8):
            octet.append(i%2)
            i = i//2
        ip_res.append(octet[-1:-9:-1])
    elif len(i)>3:
        pre_octet = []
        for l in i:
            pre_octet.append(int(l))
        octet = 0
        for i in range(0,8):
            octet += pre_octet[i]*(pow(2,7-i))
        ip_res.append(octet)
        octet = 0

''' Преобразование в строку'''
if type(ip_res[0]) is int:
    for i in range(0,len(ip_res)):
        ip_res[i] = str(ip_res[i])
    ip_res_out = '.'.join(ip_res)
    print(f'In decimal: {ip_res_out}')
elif type(ip_res[0]) is list:
    for i in range(0,len(ip_res)):
        for j in range(0,len(ip_res[i])):
            ip_res[i][j] = str(ip_res[i][j])
    for i in range(0,len(ip_res)):
        ip_res[i] = ''.join(ip_res[i])
    ip_res_out = '.'.join(ip_res)
    print(f'In binary: {ip_res_out}')

