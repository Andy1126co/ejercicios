from functools import reduce


palindromo = lambda string : (string.lower()).replace(" ","") \
         == (string.lower()).replace(" ","")[::-1]

print(palindromo('Arriba la birra'))


my_list =[1,4,5,6,9,13,19,21]
odd = list(filter(lambda x : x%2 != 0,my_list))
print("/////////////////////////////////")
print(odd)

natural_number = [i**2 for i in range(1,101) if i%3 ]

print("**********************************")

my_list_two = [1,2,3,4,5]
opp = list(map(lambda x : x**2,my_list_two))
print(f'lista doble: {opp} ')

my_list_three = [2,2,2,2,2]
ipp = reduce(lambda x,y :x*y,my_list_three )
print(f'list three : {ipp}')