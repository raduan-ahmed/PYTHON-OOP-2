import random

#float between 0 and 1
random_float = random.random()
print("Random float between 0 and 1:", random_float)

#random integer within a specific range
random_int = random.randint(1, 10)
print("Random integer between 1 and 10:", random_int)

#within a specified range with step size
random_range = random.randrange(0, 20, 2)  # Generates an even number between 0 and 20
print("Random number from range 0 to 20 with step 2:", random_range)

#float within a specific range
random_uniform = random.uniform(1.5, 5.5)
print("Random float between 1.5 and 5.5:", random_uniform)

#random element from a list
sample_list = [10, 20, 30, 40, 50]
random_choice = random.choice(sample_list)
print("Random choice from the list:", random_choice)

#Shuffle a list randomly
random.shuffle(sample_list)
print("Shuffled list:", sample_list)

#multiple random elements from a list
random_sample = random.sample(sample_list, 2)  # Selects 2 random elements
print("Random sample of 2 elements from the list:", random_sample)
