#Konvensi : A Quaternion shall be represented as a list with the following format
# Q = S + Xi + Yj + Zk --> Q = [S,X,Y,Z]
import math
import copy

p = [0,1,1,0]
q=[math.cos(math.radians(45)),0,math.sin(math.radians(45)),0]
q1=[math.cos(math.radians(45)),0,-math.sin(math.radians(45)),0]

def productQ(Q1,Q2) :
  #Returns the product of two quaternions

  TempQ1 = Q1.copy()
  TempQ2 = Q2.copy()
  ReturnQ = []
  CrossProduct = []
  # Product 1 : S1 * S2
  P1 = Q1[0] * Q2[0]

  # Product 2 : V1 . V2
  P2 = (Q1[1]*Q2[1])+(Q1[2]*Q2[2])+(Q1[3]*Q2[3])

  # Product 3 : S1 * V2
  TempQ2[1] *= Q1[0]
  TempQ2[2] *= Q1[0]
  TempQ2[3] *= Q1[0]

  # Product 4 : S2 * V1
  TempQ1[1] *= Q2[0]
  TempQ1[2] *= Q2[0]
  TempQ1[3] *= Q2[0]

  # Product 5 : V1 x V2
  CrossProduct.append(Q1[2]*Q2[3]-Q1[3]*Q2[2])
  CrossProduct.append(Q1[1]*Q2[3]-Q1[3]*Q2[1])
  CrossProduct.append(Q1[1]*Q2[2]-Q1[2]*Q1[1])

  ReturnQ.append(TempQ1[1]+TempQ2[1]+CrossProduct[0])
  ReturnQ.append(TempQ1[2]+TempQ2[2]+CrossProduct[1])
  ReturnQ.append(TempQ1[3]+TempQ2[3]+CrossProduct[2])
  ReturnQ.append(P1 - P2)

  return ReturnQ

def addQ (Q1,Q2) :

    AddedQ = []

    AddedQ.append(Q1[0]+Q2[0])
    AddedQ.append(Q1[1]+Q2[1])
    AddedQ.append(Q1[2]+Q2[2])
    AddedQ.append(Q1[3]+Q2[3])

    return AddedQ
