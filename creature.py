# creature.py

import random

def create_hybrid_name(c1, c2):
    # create hybrid name by combining parts of each input
    part1 = c1[:len(c1)//2]
    part2 = c2[len(c2)//2:]
    return part1.capitalize() + part2.capitalize()

def generate_stats():
    # generate a random weight and diet for the creature
    weight = random.randint(50, 2000)
    diets = ['berries', 'insects', 'celery', 'fish', 'plants', 'cookies']
    diet = random.choice(diets)
    return weight, diet

def create_hybrid_creature(c1, c2):
    name = create_hybrid_name(c1, c2)
    weight, diet = generate_stats()
    return {
        "name": name,
        "weight": weight,
        "diet": diet
    }
