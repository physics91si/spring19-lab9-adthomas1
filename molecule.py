# Physics 91SI
# Spring 2019
# Lab 9

import numpy as np
import particle

class Molecule:
    """Stores information about a particle with mass, position, and velocity."""
    
    def __init__(self, p1p, p2p, m1,m2,springconstant,equilength):
        self.p1 = particle.Particle(p1p,m1)
        self.p2 = particle.Particle(p2p,m2)
        self.k = springconstant
        self.L0 = equilength
        
    def get_displ(mol):
        return (np.array(mol.p2.position) - np.array(mol.p1.position))
    
    def get_force(mol):
        return -get_displ(mol)*k
    