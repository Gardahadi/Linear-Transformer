#Convention : A Quaternion shall be represented as a list with the following format
# Q = S + Xi + Yj + Zk --> Q = [X,Y,Z,S]
import math
import copy

def productQ(Q1,Q2) :
  #Returns the product of two quaternions

  TempQ1 = Q1.copy()
  TempQ2 = Q2.copy()
  ReturnQ = []
  CrossProduct = []
  # Product 1 : S1 * S2
  P1 = Q1[3] * Q2[3]

  # Product 2 : V1 . V2
  P2 = (Q1[0]*Q2[0])+(Q1[1]*Q2[1])+(Q1[2]*Q2[2])

  # Product 3 : S1 * V2
  TempQ2[0] *= Q1[3]
  TempQ2[1] *= Q1[3]
  TempQ2[2] *= Q1[3]

  # Product 4 : S2 * V1
  TempQ1[0] *= Q2[3]
  TempQ1[1] *= Q2[3]
  TempQ1[2] *= Q2[3]

  # Product 5 : V1 x V2
  CrossProduct.append(Q1[1]*Q2[2]-Q1[2]*Q2[1])
  CrossProduct.append(Q1[2]*Q2[0]-Q1[0]*Q2[2])
  CrossProduct.append(Q1[0]*Q2[1]-Q1[1]*Q2[0])

  ReturnQ.append(TempQ1[0]+TempQ2[0]+CrossProduct[0])
  ReturnQ.append(TempQ1[1]+TempQ2[1]+CrossProduct[1])
  ReturnQ.append(TempQ1[2]+TempQ2[2]+CrossProduct[2])
  ReturnQ.append(P1 - P2)


  return ReturnQ

def addQ (Q1,Q2) :

    AddedQ = []

    AddedQ.append(Q1[0]+Q2[0])
    AddedQ.append(Q1[1]+Q2[1])
    AddedQ.append(Q1[2]+Q2[2])
    AddedQ.append(Q1[3]+Q2[3])

    return AddedQ
