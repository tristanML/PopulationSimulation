#!/usr/bin/env python
# coding: utf-8

# In[171]:


from gene import *
import random


# In[172]:


class Organism:
    def __init__(self, list_of_genes, name=""):
        self.genome = list_of_genes
        self.name = name
        self.genome_length = len(list_of_genes)
        self.genome_attr = {}
        for x in self.genome:
            self.genome_attr[x.dominant_allele+x.recessive_allele] = x.keys
    def breeding(self, other_organism):
        other = other_organism
        self.offspring_genome = []
        self.offspring_genome_attr = {}
        self.offspring_genome_letters = []
        self.gamete = []
        other_gamete = []
        for genotype in self.genome:
            self_choice_list = [genotype.dominant_allele, genotype.recessive_allele]
            self_gamete_gene = random.choice(self_choice_list)
            self.gamete.append(self_gamete_gene)
        for other_genotype in other.genome:
            other_choice_list = [other_genotype.dominant_allele, other_genotype.recessive_allele]
            other_gamete_gene = random.choice(other_choice_list)
            other_gamete.append(other_gamete_gene)  
        for x in range(len(self.gamete)):
            gene_letter = self.gamete[x].lower()
            gene_string = self.gamete[x]+other_gamete[x]
            if gene_string == gene_letter.upper()+gene_letter.upper():
                fd = True
                fr = False
            if gene_string == gene_letter+gene_letter:
                fd = False
                fr = True
            if gene_string == gene_letter.upper()+gene_letter or gene_string == gene_letter+gene_letter.upper():
                gene_string = gene_letter.upper()+gene_letter
                fd = False
                fr = False
            self.offspring_genome.append(Genotype(gene_letter, fd, fr, self.genome[x].name))
            self.offspring_genome_letters.append(gene_string)
            self.offspring_genome_attr[gene_string] = self.offspring_genome[x].keys


# In[189]:


#lizard_genome = [Genotype("e", name = "eye color"), Genotype("c", name = "claw color"), Genotype("s", name = "spine color")]


# In[197]:


# lizard1 = Organism(lizard_genome, "lizard")
# lizard2 = Organism(lizard_genome, "lizard")

# lizard2.breeding(lizard1)


# In[55]:





# In[ ]:


#"dictionary corresponding to colors on animal: pygame"

