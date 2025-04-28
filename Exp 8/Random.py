#Random(): This function returns a random floating-point number
#in the range [0.0, 1.0).
import random
print(random.random()) # Output: a random float between 0.0 and 1.0
#randint(a, b): This function returns a random integer N such
#that a <= N <= b.
import random
print(random.randint(1, 10)) # Output: a random integer between 1 and 10

#uniform(a, b): This function returns a random floating-point
#number N such that a <= N <= b.
import random
print(random.uniform(1.0, 10.0)) # Output: a random float between 1.0 and 10.0

#randrange([start], stop[, step]): This function returns a randomly
#selected element from the specified range.
import random
print(random.randrange(0, 100, 2)) # Output: a random even number between 0 and 100

#choice(seq): This function returns a random element from the
#non-empty sequence seq.
import random
my_list = ['apple', 'banana', 'cherry']
print(random.choice(my_list)) # Output: a random element from thelist

#shuffle(seq): This function shuffles the elements of the
#sequence seq in place.
import random
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list) # Output: a shuffled version of the list

#sample(population, k): This function returns a random sample
#of k elements from the population sequence without replacement.
import random
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(random.sample(my_list, k=3)) # Output: a random sample of 3 elements from the list

#It's important to note that Python's random number generator is
#deterministic, meaning that it produces the same sequence of
#random numbers every time the program runs with the same seed
#value. You can set the seed value using random.seed() to produce
#reproducible results.
import random
random.seed(42) # Set seed value for reproducibility
print(random.random()) # Output: 0.6394267984578837

