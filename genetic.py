#Genetic Algorithms are usefull when little is known
# about a problem, especially with a nonlinear problem
# in which brute force methods are needed in a large
# search space. They are easy to grasp and implement

#Breed Super Rats, with avg. weight of 110lbs

import time
import random
import statistics

#INPUT ASSUMPTIONS FOR SUPER-RATES GENETIC ALGORITHM
Goal = 50000    #weight in grams
NUM_RATS = 20
INITIAL_MIN_WT = 200
INITIAL_MAX_WT = 600
INITIAL_MODE_WT = 300
MUTATE_ODDS = 0.01
MUTATE_MIN = 0.5
MUTATE_MAX = 1.2
LITTER_SIZE = 8
LITTERS_PER_YEAR = 10
GENERATION_LIMIT = 500

# ensure even-number of rates for breeding pairs:
if NUM_RATS % 2 != 0:
    NUM_RATS += 1

    #Populate
    #Grade
    #Select
    #Breed
    #Mutate
