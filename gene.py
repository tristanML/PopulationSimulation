#!/usr/bin/env python
# coding: utf-8

# In[9]:


import random
import time
import numpy as np

class Genotype:
    def __init__(self, gene_lower_letter, fully_dominant = False, fully_recessive = False, name = ""):
        self.gene_lower_letter = gene_lower_letter
        self.fully_dominant = fully_dominant
        self.fully_recessive = fully_recessive
        self.name = name
        #key_dict = {}
        #key = {"dominant" or True: dominant_letter, "recessive" or False: recesive_letter}
        #key_dict[dominant_letter+recesive_letter] = key
        #self.global_keys = key_dict[gene_lower_letter.upper()+ gene_lower_letter]
        if fully_dominant == True:
            dominant_letter = gene_lower_letter.upper()
            self.keys = {"dominant allele" or True: self.gene_lower_letter.upper(), "recessive allele": self.gene_lower_letter.upper()}
            self.isdominant = True
        elif fully_recessive == True:
            recessive_letter = gene_lower_letter
            self.keys = {"dominant allele" or True: self.gene_lower_letter, "recessive allele" or False: self.gene_lower_letter}
            self.isdominant = False
        else:
            self.keys = {"dominant allele" or True: self.gene_lower_letter.upper(), "recessive allele" or False: self.gene_lower_letter}
        self.dominant_allele = self.keys["dominant allele"]
        self.recessive_allele = self.keys["recessive allele"]
        self.isdominant = True
        self.full_allele = self.dominant_allele+self.recessive_allele
        
    def punnet_square(self, other_genotype):
        og = other_genotype
        genotype_array = np.array([["",""],["",""]])
        offspring_list = []
        if self.dominant_allele.isupper() == True:
            if og.dominant_allele.isupper() == True:
                genotype_array[0][0] = "dominant"
            if og.dominant_allele.islower() == True:
                genotype_array[0][0] = "hybrid"
            if og.recessive_allele.isupper() == True:
                genotype_array[1][0] = "dominant"
            if og.recessive_allele.islower() == True:
                genotype_array[1][0] = "hybrid"
                
        if self.dominant_allele.islower() == True:
            if og.dominant_allele.isupper() == True:
                genotype_array[0][0] = "hybrid"
            if og.dominant_allele.islower() == True:
                genotype_array[0][0] = "recessive"
            if og.recessive_allele.isupper() == True:
                genotype_array[1][0] = "hybrid"
            if og.recessive_allele.islower() == True:
                genotype_array[1][0] = "recessive"
            
        if self.recessive_allele.isupper() == True:
            if og.dominant_allele.isupper() == True:
                genotype_array[0][1] = "dominant"
            if og.dominant_allele.islower() == True:
                genotype_array[0][1] = "hybrid"
            if og.recessive_allele.isupper() == True:
                genotype_array[1][1] = "dominant"
            if og.recessive_allele.islower() == True:
                genotype_array[1][1] = "hybrid"
                
        if self.recessive_allele.islower() == True:
            if og.dominant_allele.isupper() == True:
                genotype_array[0][1] = "hybrid"
            if og.dominant_allele.islower() == True:
                genotype_array[0][1] = "recessive"
            if og.recessive_allele.isupper() == True:
                genotype_array[1][1] = "hybrid"
            if og.recessive_allele.islower() == True:
                genotype_array[1][1] = "recessive"
        
        
        for x in genotype_array:
            for y in x:
                if y == "d":
                    offspring_list.append(Genotype(self.gene_lower_letter, fully_dominant=True, name="dominant"))
                if y == "r": 
                    offspring_list.append(Genotype(self.gene_lower_letter, fully_recessive=True, name="recesive"))
                if y == "h":
                    offspring_list.append(Genotype(self.gene_lower_letter, name="hybrid"))
                    
        print(genotype_array)


# In[51]:


genotype_list = []


# In[68]:


# test = Genotype("b", fully_recessive= True)
# test2 = Genotype("b", fully_recessive= True)


# In[69]:


# test.punnet_square(test2)

def population_maker(size, gene_lower_letter):
    global population_list
    store_list = [] 
    population_list = []
    b_comb_list = [Genotype(gene_lower_letter, name="hybrid"), Genotype(gene_lower_letter, True, name="Fully Dominant"), Genotype(gene_lower_letter, False, True, "Fully Recesive")]
    for x in b_comb_list:
        store_list.append(x)
    while len(population_list) < size:
        population_list.append(random.choice(b_comb_list))
    print(population_list)
        
        
# population_maker(100, "b")


# In[9]:


def sorter(list_to_sort):
    elements = []
    element_name = {}
    element_num = {}
    for x in list_to_sort:
        if x in elements:
            element_num[x.name] += 1
        else:
            elements.append(x)
            element_name[x.name] = x
            element_num[x.name] = 0
    print(element_name)
    print(element_num)
    
# sorter(population_list)


# In[32]:




# In[33]:


b_comb_list = [Genotype("b"), Genotype("b", True), Genotype("b", False, True)]

# random.choice(b_comb_list)


# In[35]:


# "B".isupper() > "b".isupper()


# In[44]:


def key_maker(lower_letter):
    Genotype_list = {}
    ll = lower_letter
    up = ll.upper()
    key_string = {"dominant" or True: up, "recessive" or False: ll}
    Genotype_list[up+ll] = key_string
    print(Genotype_list[up+ll])


# In[47]:


# key_maker("q")


# In[ ]:


def punnet_square(self, other_Genotype):
        oa = other_Genotype
        sq1 = False
        sq2 = False
        sq3 = False
        sq4 = False
        if self.dominant.isupper() > oa.dominant.isupper():
            print(self.dominant, "is dominant over", oa.dominant)
            sq1 = True
        if self.dominant.isupper() > oa.recessive.isupper():
            print(self.dominant, "is dominant over", oa.dominant)
            sq2 = True
        if self.recessive.isupper() > oa.dominant.isupper():
            print(self.dominant, "is dominant over", oa.dominant)
            sp3 = True
        if self.recessive.isupper() > oa.recessive.isupper():
            print(self.dominant, "is dominant over", oa.dominant)
            sq4 = True
        print(sq1, sq2)
        print(sq3, sq4)


# In[16]:


import numpy as np







