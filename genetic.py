#Genetic Algorithms are usefull when little is known
# about a problem, especially with a nonlinear problem
# in which brute force methods are needed in a large
# search space. They are easy to grasp and implement

#Breed Super Rats, with avg. weight of 110lbs

import time
import random
import statistics

#INPUT ASSUMPTIONS FOR SUPER-RATES GENETIC ALGORITHM
GOAL = 50000    #weight in grams
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
def populate(num_rats, min_wt, max_wt, mode_wt):
    """Initialize a population wit ha triangular distribution of weights"""
    return [int(random.triangular(min_wt, max_wt, mode_wt))\
        for i in range(num_rats)]
#Grade
def fitness(population, goal):
    """Measure population fitness based on an attribute mean vs target."""
    ave = statistics.mean(population)
    return ave / goal
#Select
def select(population, to_retain):
    """Cull a population to retain only a specified number of members."""
    sorted_population = sorted(population)
    to_retain_by_sex = to_retain//2
    members_per_sex = len(sorted_population)//2
    females = sorted_population[:members_per_sex]
    males = sorted_population[members_per_sex:]
    selected_females = females[-to_retain_by_sex:]
    selected_males = males[-to_retain_by_sex:]
    return selected_males, selected_females
#Breed
def breed(males, females, litter_size):
    """Crossover genes among members (weights) of a population."""
    random.shuffle(males)
    random.shuffle(females)
    children = []
    for male, female in zip(males, females):
        for child in range(litter_size):
            child = random.randint(female, male)
            children.append(child)
    return children
#Mutate
def mutate(children, mutate_odds, mutate_min, mutate_max):
    """Randomly alter rat weights using input odds & fractional changes."""
    for index, rat in enumerate(children):
        if mutate_odds >= random.random():
            children[index] = round(rat * random.uniform(mutate_min, mutate_max))
    return children

def main():
    """Initialize population, select, breed, and mutate, display results."""
    generations = 0
    parents = populate(NUM_RATS, INITIAL_MIN_WT, INITIAL_MAX_WT, INITIAL_MODE_WT)
    print("initial populate weights = {}".format(parents))
    popl_fitness = fitness(parents, GOAL)
    print("initial population fitness = {}".format(popl_fitness))
    print("number to retain = {}".format(NUM_RATS))

    ave_wt = []

    while popl_fitness < 1 and generations < GENERATION_LIMIT:
        selected_males, selected_females = select(parents, NUM_RATS)
        children = breed(selected_males, selected_females, LITTER_SIZE)
        children = mutate(children, MUTATE_ODDS, MUTATE_MIN, MUTATE_MAX)
        parents = selected_males + selected_females + children
        popl_fitness = fitness(parents, GOAL)
        print("Generation {} fitness = {:.4f}".format(generations, popl_fitness))
        ave_wt.append(int(statistics.mean(parents)))
        generations += 1
    print("average weight per generation = {}".format(ave_wt))
    print("\nnumber of generations = {}".format(generations))
    print("number of years = {}".format(int(generations / LITTERS_PER_YEAR)))

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print("\nRuntime for this program was {} seconds.".format(duration))