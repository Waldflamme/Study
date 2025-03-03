import numpy as np

print('Разминка')

print('Задание 1')
print()

arr0 = np.random.uniform(0,20,(4,7))
maks = np.max(arr0)
minim = np.min(arr0)

a = 1/(maks-minim)
b = 1 - a*maks
c = -a*minim

arr2 = a*arr0+c

print(arr0)
print()
print(minim)
print()
print(maks)
print()
print(a)
print()
print(b)
print()
print(c)
print()
print(arr2)
print()

print('Задание 2')
print()

arr3 = np.random.randint(0,10,(8,10))
sums = np.array(np.sum(arr3,1))
minim1 = np.argmin(np.array(np.sum(arr3,1)))

print(arr3)
print()
print(sums)
print()
print(minim1)
print()
print(arr3[minim1])
print()

print('Задание 3')
print()

a = np.array([1,3])
b = np.array([2,5])

dist = np.linalg.norm(a-b)

print(dist)
print()

print('Задание 4')
print()

A = np.array([[-1,2,4],[-3,1,2],[-3,0,1]])
B = np.array([[3,-1],[2,1]])
C = np.array([[7,21],[11,8],[8,4]])

X = np.linalg.inv(A)@-C@np.linalg.inv(B)
M = -(A@X@B)

print(X)
print(M)
print()

print('Начало лабораторной работы')
print()
print('Задание 1')
print()

arr1 = np.loadtxt('minutes_n_ingredients.csv',delimiter = ',', dtype = np.int32, skiprows = 1)

print(arr1[:5])
print()

print('Задание 2')
print()

print(np.mean(arr1[:,1:],0))
print(np.max(arr1[:,1:],0))
print(np.min(arr1[:,1:],0))
print(np.median(arr1[:,1:],0))
print()

print('Задание 3')
print()

sec_col = np.array(arr1[:,1])
q_75 = np.quantile(sec_col, 0.75)
quant_mask = sec_col<q_75 #или sec_col<=q_75

print(sec_col)
print()
print(q_75)
print()
print(sec_col[quant_mask])
print()

print('Задание 4')
print()

zero_sec_col = np.size(sec_col[sec_col == 0])
sec_col_no_zeros = sec_col.copy()
sec_col_no_zeros[sec_col_no_zeros == 0] = 1

print(zero_sec_col)
print()
print(np.size(sec_col[sec_col == 1]))
print()
print(np.size(sec_col_no_zeros[sec_col_no_zeros == 1]))
print()
print(sec_col_no_zeros)
print()

print('Задание 5')
print()

unic_res_pair = np.array(arr1[:,1:])
uniq_rec = np.unique(unic_res_pair, axis = 0)

print(uniq_rec)
print()
print(np.size(uniq_rec))
print()

print('Задание 6')
print()

uniq_rec_ing = np.unique(arr1[:,2])
uniq_rec_ing_num = np.size(uniq_rec_ing)

print(uniq_rec_ing_num)
print()
print(uniq_rec_ing)
print()

print('Задание 7')
print()

ing_mask = arr1[:,2]<=5
f_ing_arr = arr1[ing_mask]

print(np.size(arr1[ing_mask]))
print()
print(np.size(f_ing_arr))
print()
print(f_ing_arr)
print()

print('Задание 8')
print()

ing_per_min = np.array(arr1[:,2]/sec_col_no_zeros)
max_ing_per_min = np.max(ing_per_min)

print(ing_per_min)
print()
print(max_ing_per_min)
print()

print('Задание 9')
print()

top_dur = np.flip(np.argsort(arr1[:,1]))
top_dur_sort = arr1[top_dur]
mean_top_dur = np.mean(top_dur_sort[:100,2])

print(top_dur_sort)
print()
print(top_dur_sort[:100,1:])
print()
print(mean_top_dur)
print()

print('Задание 10')
print()

rand_rec_ind = np.random.randint(0,100000,10)
rand_rec = arr1[rand_rec_ind]

print(rand_rec_ind)
print()
print(rand_rec)
print()

print('Задание 11')
print()

less_then_mean = arr1[:,2]<np.mean(arr1[:,2])
perc_less_then_mean = np.size(arr1[:,2][less_then_mean])/np.size(arr1[:,2])

print(perc_less_then_mean)
print()

print('Задание 12')
print()

simp_rec = ((arr1[:,1]<=20) * (arr1[:,2]<=5))*1
simp_rec_ls = np.hstack((arr1, simp_rec [:, np.newaxis]))

print(simp_rec)
print()
print(simp_rec_ls)
print()

print('Задание 13')
print()

simp_rec_proc = np.size(simp_rec[simp_rec == 1])/np.size(simp_rec)

print(simp_rec_proc)
print()

print('Задание 14')
print()

simple_rec = arr1[arr1[:,1]<=10]
stand_rec = arr1[(10<arr1[:,1]) & (arr1[:,1]<=20)]
long_rec = arr1[arr1[:,1]>20]

min_len_ls = min(len(simple_rec),len(stand_rec),len(long_rec))

simple_rec_minim = simple_rec[:min_len_ls]
stand_rec_minim = stand_rec[:min_len_ls]
long_rec_minim = long_rec[:min_len_ls]

t_d_arr = np.array([simple_rec_minim,stand_rec_minim,long_rec_minim])
print(min_len_ls)
print()
print(t_d_arr)