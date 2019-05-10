import datetime
import random_name
import random

for i in range(1,20):
    print('\n') 
print('Today is {0} and {1} feels like having {2} beers!'.format(datetime.date.today(), random_name.generate(1), random.randint(0,10)))
input("Press Enter to continue...")
