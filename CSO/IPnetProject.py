ip = input('Enter IP address in decimal or binary: ')
subnet = int(input('Enter number of subnetworks: '))
hots = int(input('Enter number of hosts: '))

ip_in_lst = ip.split(sep = '.')
ip_res = []

''' Преобразование в десятичную систему исчисления'''
for i in ip_in_lst:
    if len(i) <= 3:
        i = int(i)
        ip_res.append(i)
    elif len(i)>3:
        pre_octet = []
        for l in i:
            pre_octet.append(int(l))
        octet = 0
        for i in range(0,8):
            octet += pre_octet[i]*(pow(2,7-i))
        ip_res.append(octet)
        octet = 0

mask = []

def mask_to_str(lst):
    '''Преобразование маски в десятичную форму'''
    mask_to_str = []
    ls= []
    res_mask = []
    for n in range(0,32):
        ls.append(lst[n])
        if len(ls)==8:
            mask_to_str.append(ls)
            ls = []
    octet = 0
    for i in mask_to_str:
        for j in range(0, 8):
            octet += i[j] * (pow(2, 7 - j))
        res_mask.append(octet)
        octet = 0
    for i in range(0,len(res_mask)):
        res_mask[i] = str(res_mask[i])
    return '.'.join(res_mask)

if ip_res[0]<=127:

    if subnet<=262144: #Просчет маски, условие поставлено с учетом минимального количества хостов 64 шт
        for i in range(1,25):
            if subnet > 2**i:
                pass
            else:
                print(f'IP addresses available for hosts: {2**(24-i)-2}')
                for n in range(0,8):
                    mask.append(1)
                for l in range(0,i):
                    mask.append(1)
                for j in range(len(mask),32):
                    mask.append(0)
                break
        print(f'Project mask: {mask_to_str(mask)}')
    else:
        print('Such number of subnetworks is not advisable')

    print('Class: A \nStarting address: 0.0.0.0 \n'
          'Ending address: 127.255.255.255 \n'
          f'Number of IP addresses: {128*256*256*256}\n'
          f'Stack of first five available IP addresses:\n'
          f'{ip_res[0]}.0.0.2\n'
          f'{ip_res[0]}.0.0.3\n'
          f'{ip_res[0]}.0.0.4\n'
          f'{ip_res[0]}.0.0.5\n'
          f'{ip_res[0]}.0.0.6\n'
          f'Stack of last five available IP addresses:\n'
          f'{ip_res[0]}.255.255.250'
          f'{ip_res[0]}.255.255.251'
          f'{ip_res[0]}.255.255.252'
          f'{ip_res[0]}.255.255.253'
          f'{ip_res[0]}.255.255.254')

elif 127<ip_res[0]<=191:

    if subnet<=1024:
        for i in range(1,17):
            if subnet > 2**i:
                pass
            else:
                print(f'IP addresses available for hosts: {2**(16-i)-2}')
                for n in range(0,16):
                    mask.append(1)
                for l in range(0,i):
                    mask.append(1)
                for j in range(len(mask),32):
                    mask.append(0)
                break
        print(f'Project mask: {mask_to_str(mask)}')
    else:
        print('Such number of subnetworks is not advisable')

    print('Class: B \nStarting address: 128.0.0.0 \n'
          'Ending address: 191.255.255.255 \n'
          f'Number of IP addresses: {64*256*256*256}\n'
          f'Stack of first five available IP addresses:\n'
          f'{ip_res[0]}.{ip_res[1]}.0.2\n'
          f'{ip_res[0]}.{ip_res[1]}.0.3\n'
          f'{ip_res[0]}.{ip_res[1]}.0.4\n'
          f'{ip_res[0]}.{ip_res[1]}.0.5\n'
          f'{ip_res[0]}.{ip_res[1]}.0.6\n'
          f'Stack of last five available IP addresses:\n'
          f'{ip_res[0]}.{ip_res[1]}.255.250'
          f'{ip_res[0]}.{ip_res[1]}.255.251'
          f'{ip_res[0]}.{ip_res[1]}.255.252'
          f'{ip_res[0]}.{ip_res[1]}.255.253'
          f'{ip_res[0]}.{ip_res[1]}.255.254')

elif 191<ip_res[0]<=223:

    if subnet<=4:
        for i in range(1,9):
            if subnet > 2**i:
                pass
            else:
                print(f'IP addresses available for hosts: {2**(8-i)-2}')
                for n in range(0,24):
                    mask.append(1)
                for l in range(0,i):
                    mask.append(1)
                for j in range(len(mask),32):
                    mask.append(0)
                break
        print(f'Project mask: {mask_to_str(mask)}')
    else:
        print('Such number of subnetworks is not advisable')

    print('Class: C \nStarting address: 192.0.0.0 \n'
          'Ending address: 223.255.255.255 \n'
          f'Number of IP addresses: {32*256*256*256}\n'
          f'{ip_res[0]}.{ip_res[1]}.{ip_res[2]}.2\n'
          f'{ip_res[0]}.{ip_res[1]}.{ip_res[2]}.3\n'
          f'{ip_res[0]}.{ip_res[1]}.{ip_res[2]}.4\n'
          f'{ip_res[0]}.{ip_res[1]}.{ip_res[2]}.5\n'
          f'{ip_res[0]}.{ip_res[1]}.{ip_res[2]}.6\n'
          f'Stack of last five available IP addresses:\n'
          f'{ip_res[0]}.{ip_res[1]}.{ip_res[2]}.250'
          f'{ip_res[0]}.{ip_res[1]}.{ip_res[2]}.251'
          f'{ip_res[0]}.{ip_res[1]}.{ip_res[2]}.252'
          f'{ip_res[0]}.{ip_res[1]}.{ip_res[2]}.253'
          f'{ip_res[0]}.{ip_res[1]}.{ip_res[2]}.254')

elif 223<ip_res[0]<=239:
    print('Class: D (reserved, not available to administrators) \nStarting address: 224.0.0.0 \n'
          'Ending address: 239.255.255.255 \n'
          f'Number of IP addresses: {16*256*256*256}\n')

elif 239<ip_res[0]<=255:
    print('Class: E (reserved, not available to administrators) \nStarting address: 240.0.0.0 \n'
          'Ending address: 255.255.255.255 \n'
          f'Number of IP addresses: {16*256*256*256}\n')

