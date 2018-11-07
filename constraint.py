from Z3 import *

#Andrew Heiges
#Constraint Satisfaction Lab
#11.7.18

s = z3.Solver()
s.push()
s.add(constraints)
if s.check() == z3.sat:
   print "Satisfiable!"
   print "Here is the model: ", s.model()
s.pop()