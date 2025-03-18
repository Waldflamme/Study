ip = input('Enter IP address in decimal or binary: ')

ip_in_lst = ip.split(sep = '.')
ip_res = []

if len(ip_in_lst[0]) <= 3:
    ip_in_lst[0] = int(ip_in_lst[0])
    ip_res.append(ip_in_lst[0])
elif len(ip_in_lst[0]) > 3:
    pre_octet = []
    for l in ip_in_lst[0]:
        pre_octet.append(int(l))
    octet = 0
    for i in range(0, 8):
        octet += pre_octet[i] * (pow(2, 7 - i))
    ip_res.append(octet)
    octet = 0

if ip_res[0]<=127:
    print('Class: A \nStarting address: 0.0.0.0 \n'
          'Ending address: 127.255.255.255 \n'
          'Mask: 255.0.0.0 \n')
elif 127<ip_res[0]<=191:
    print('Class: B \nStarting address: 128.0.0.0 \n'
          'Ending address: 191.255.255.255 \n'
          'Mask: 255.255.0.0 \n')
elif 191<ip_res[0]<=223:
    print('Class: C \nStarting address: 192.0.0.0 \n'
          'Ending address: 239.255.255.255 \n'
          'Mask: 255.255.255.0 \n')
elif 223<ip_res[0]<=239:
    print('Class: D (reserved) \nStarting address: 224.0.0.0 \n'
          'Ending address: 239.255.255.255 \n'
          'Mask: None \n')
elif 239<ip_res[0]<=255:
    print('Class: D (reserved) \nStarting address: 240.0.0.0 \n'
          'Ending address: 255.255.255.255 \n'
          'Mask: None \n')