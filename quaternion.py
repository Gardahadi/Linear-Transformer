#Konvensi : A Quaternion shall be represented as a list with the following format
# Q = S + Xi + Yj + Zk --> Q = [X,Y,Z,S]


def productQ(Q1,Q2) :
  #Returns the product of two quaternions

  TempQ1 = Q1
  TempQ2 = Q2
  ReturnQ = []
  CrossProduct = []
  # Product 1 : S1 * S2
  P1 = Q1[3] * Q2[3]

  # Product 2 : V1 . V2
  P2 = (Q1[0]*Q2[0])+(Q1[1]*Q2[1])+(Q[2]*Q[2])

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
  CrossProduct.append(Q1[0]*Q2[2]-Q1[2]*Q2[0])
  CrossProduct.append(Q1[0]*Q2[1]-Q1[1]*Q1[0])
