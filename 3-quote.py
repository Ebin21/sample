REFRAIN = '''
{} bottles of beer on the wall,
{} bottles of beer,
take one down, pass it around,
{} bottles of beer on the wall!
'''
bottles_of_beer = 9
while bottles_of_beer > 1:
    print (REFRAIN.format(bottles_of_beer, bottles_of_beer,
        bottles_of_beer - 1))
    bottles_of_beer -= 1