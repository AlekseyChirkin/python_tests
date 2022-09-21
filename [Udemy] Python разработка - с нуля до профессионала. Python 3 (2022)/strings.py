word = 'word from letters'

print(word[:3])
print(word[-5:]*2)

yummy = 'Yum'
print(yummy.upper().lower())
print(word.split())

print('1' + '1')
print('1' + str(1))

name = 'Sasha'
age = 24

print()
print('His name is {0}. He is {1} years old'.format(name, age))
print('His name is {}. He is {} years old'.format(name, age))
print('His name is %s. He is %d years old' % (name, age))
print()

print('There are seven days in a week: {mo}, {tu}, {wed}, {th}, {fr}, {sat}, {sun}'
      .format(mo='monday', tu='tuesday', wed='wednesday', th='thursday', fr='friday',
              sat='saturday', sun='sunday'))
print(f"There are seven days in a week: {'monday'}, {'tuesday'}, {'wednesday'}, {'thursday'}, {'friday'}, {'saturday'}, {'sunday'}")

float_res = 1000 / 7
print(float_res)

print('The result of division is {0:20.3f}'.format(float_res))

print('''
{:5.0f}{:5.0f}{:5.0f}{:5.0f}{:5.0f}
{:5.0f}{:5.0f}{:5.0f}{:5.0f}{:5.0f}
{:5.0f}{:5.0f}{:5.0f}{:5.0f}{:5.0f}
'''.format(10, 30, 100, 4, 99, 10, 30, 100, 4, 1000, 10, 30, 100, 4, 100))
