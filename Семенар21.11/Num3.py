a,b = map(int, input('Enter first coordinates with comma: ').split(','))
c,d = map(int, input('Enter second coordinates with comma: ').split(','))
q,f = map(int, input('Enter third coordinates with comma: ').split(','))

def TypeTrl(a,b,c,d,q,f):
    len_ab_cd = ((a-c)**2+(b-d)**2)**0.5
    len_cd_qf = ((c-q)**2+(d-f)**2)**0.5
    len_ab_qf = ((a-q)**2+(b-f)**2)**0.5
    if len_ab_cd==len_cd_qf==len_ab_qf:
        print('This is equilteral triangle: ')
    elif (len_ab_cd==len_cd_qf and len_ab_cd!=len_ab_qf and len_cd_qf!=len_ab_qf) \
        or (len_ab_cd==len_ab_qf and len_ab_cd!=len_cd_qf and len_ab_qf!=len_cd_qf) \
        or (len_cd_qf==len_ab_qf and len_cd_qf!=len_ab_cd and len_ab_qf!=len_ab_cd):
        print('This triangle is isoseles')
    elif len_ab_cd**2+len_cd_qf**2==len_ab_qf**2\
        or len_cd_qf**2+len_ab_qf**2==len_ab_cd**2\
        or len_ab_cd**2+len_ab_qf**2==len_cd_qf**2:
        print('This triangle is rectangular')
    else:
        print('This triangle is simple')

TypeTrl(a,b,c,d,q,f)