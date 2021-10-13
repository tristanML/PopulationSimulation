from organism_code import *
import random
import pygame
import shutil
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use("tkagg")

population = []
dead_entity_list = []

live_cycle_data = []
dead_cycle_data = []
total_dead_cycle_data = []
offspring_cycle_data = []

class Entity:
    def __init__(self, genome):
        self.organism = Organism(genome)
        self.ent_int = random.randint(1, 100000)
        self.age = 1
        self.offspring_list = []
        
    def breed(self, other_org, population_list):
        self.organism.offspring_genome = []
        self.organism.breeding(other_org.organism)
        offspring = Entity(self.organism.offspring_genome)
        self.offspring_list.append(offspring)
        population_list.append(offspring)

class Predator():
    def __init__(self, gene_to_hunt, kill_percentage):
        self.target = gene_to_hunt
        self.kill_percentage = kill_percentage
        self.choice_list = [True, False]
        self.weight_list = [kill_percentage, 100-(kill_percentage*100)]

predator_ss = Predator("ss", 80)
predator_EE = Predator("EE", 80)
predator_list = [predator_ss, predator_EE]

def simple_population(population_list):
    size = int(input("Population Initial Size "))
    cycles = int(input("Population Cycles "))
    disaster_chance = float(input("Natural Disaster Chance (In float form e.g. 0.1, 0.69, 0.99) "))
    disaster_kill = float(input("Percent of population killed in a natural disaster (In float form e.g. 0.5, 0.1, 0.66) "))
    age_death = int(input("Cycle Age that Entities die "))
    
    population_list = []
    offspring = []
    dead_ents = []
    temp_dead = []
    natural_disaster_kill = []
    predator_kill = []
    age_kill = []
    gene_letter_list = []
    genome_list = []
    predator_list = []
    
    print("Projected Max Population: ", int((0.5*size) * (2**cycles)))
    print("")
    
    on = True
    while on:
        letter = input("Input a genome letter; enter QUIT to leave: ")
        if letter == "QUIT":
            on = False
        else:
            genome_list.append([Genotype(letter), Genotype(letter, True), Genotype(letter, False, True)])
            gene_letter_list.append(letter)
            
    on = True
    while on:
        gene = input("Input a gene for a predator to hunt; enter QUIT to leave: ")
        if gene == "QUIT":
            on = False
        else:
            percentage = input("Kill Percentage Chance(In float form e.g. 0.1, 0.99): ")
            predator_list.append(Predator(gene, float(percentage)))
    
    for _ in range(size):
        random_genome = []
        for gene_set in genome_list:
            random_genome.append(random.choice(gene_set))
        population_list.append(Entity(random_genome))
                               
    for x in range(cycles):
        pop_len = len(population_list)
        print("Cycle",str(x+1)+":")
        print("Current Population:", pop_len)
        live_cycle_data.append((x, pop_len))
        
        if random.randint(1, 10) <= (disaster_chance*10) and pop_len > 0:
            cutoff = int(pop_len*disaster_kill)
            dead_ents += population_list[:cutoff]
            temp_dead += population_list[:cutoff]
            natural_disaster_kill += population_list[:cutoff]
            
            population_list = population_list[cutoff:]
            print("Natural disaster killed: ", cutoff, "creatues")
        
        for entity in population_list:
            if entity.age > age_death:
                population_list.remove(entity)
                dead_ents.append(entity)
                temp_dead.append(entity)
                age_kill.append(entity)
                
            else:
                entity.age += 1
                if [x for x in population_list if x != entity] == []:
                    on == False
                    break
                else:
                    other_entity = random.choice([x for x in population_list if x != entity])
                entity.organism.breeding(other_entity.organism)
                offspring_entity = Entity(entity.organism.offspring_genome)
                offspring.append(offspring_entity)
                
            for predator in predator_list:
                for gene in entity.organism.genome:
                    if gene.full_allele == predator.target:
                        if random.choices(predator.choice_list, predator.weight_list) == [True]:
                            if entity in population_list:
                                population_list.remove(entity)
                                dead_ents.append(entity)
                                temp_dead.append(entity)
                                predator_kill.append(entity)

        population_list += offspring
        print("Entities that have died this round:", len(temp_dead))
        print("Entities that have been born this round:", len(offspring))
        print("New Population:", len(population_list))
        print("")
        dead_cycle_data.append((x, len(temp_dead)))
        total_dead_cycle_data.append((x, len(dead_ents)))
        offspring_cycle_data.append((x, len(offspring)))
        temp_dead = []
        offspring = []
        
        
    print("Final Population:", len(population_list))
    print("Total dead creatures:", len(dead_ents))
    print("Predators killed:", len(predator_kill), "creatures")
    print("Age killed:", len(age_kill), "creatures")
    print("Natural Disasters killed:", len(natural_disaster_kill), "creatures")
    
population = simple_population(population)

fig, ax = plt.subplots()
ax.grid(True)
ax.set(xlabel='Cycles', ylabel='Population')

data_lists = {"Population":live_cycle_data, 
              "Cycle Dead Entities":dead_cycle_data, 
              "Total Dead Entities":total_dead_cycle_data, 
              "Cycle Offspring":offspring_cycle_data}

color_list = ["blue", "red", "purple", "green"]
color_int = 0

for list_key in data_lists:
    x_list = []
    y_list = []
    for coord in data_lists[list_key]:
        x_list.append(coord[0])
        y_list.append(coord[1])
    plt.plot(x_list, y_list, c=color_list[color_int], label = str(list_key), marker="o")
    color_int += 1

ax.legend()
fig.savefig("PopulationGraph.png")
plt.show()