# -*- coding: utf-8 -*-
"""Carbon.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aukaZ_TlvcBGFHGfdJQUUuec9JEtOllb
"""

from numpy import log as ln

#Rubber Tree

Total_Rubber_trees_Predicted = 15340 #(13% of total trees prediction)
Total_Pine_trees_Predicted = 102660  #(87% of total trees prediction)
x1 = 2020 #year
x2 = 2021 #year
y1 = 0 #carbon stored
y2 = 0 #carbon stored

#Total additionality of C stored through trees for 2020 for 15k count:
y1 = 453643.737589962*ln(x1)-3449595.48627931

#Total additionality of C stored through trees for 2021 15k count:
y2 = 453643.737589962*ln(x2)-3449595.48627931


#Total additionality of C stored through trees in a Year
y= abs(y2-y1)

x = y/(15000) #(carbon per tree in tons)

print("Actual Rubber trees:")
print('15000')

print("Actual Total additionality of C stored in Rubber trees/year in tons: ")
print(y)

print("Actual Total additionality of C02 stored in Rubber trees/year in tons: ")
a = y*(44/12)
print(a)

print("Predicted Rubber trees:")
print(Total_Rubber_trees_Predicted)
print("Predicted Total additionality of C stored in Rubber trees/year in tons: ")
b = x*Total_Rubber_trees_Predicted
print(b)

print("Predicted Total additionality of C02 stored in Rubber trees/year in tons: ")
c= x*Total_Rubber_trees_Predicted*(44/12)
print(c)

#PineApple plants

#Total additionality of C stored through plants for 2019 for 1 lakh count:
y3 = 62400.9647543156*ln(x1)-474639.726413728

#Total additionality of C stored through plants for 2020 1 lakh count:
y4 = 62400.9647543156*ln(x2)-474639.726413728


#Total additionality of C stored through plants in a Year
y0= abs(y4-y3)

x0 = y0/(100000) #carbon per plant in tons

print("Actual Pineapple plants:")
print('100000')

print("Actual Total additionality of C stored in Pineapple plants/year in tons: ")
print(y0)

print("Actual Total additionality of C02 stored in Pineapple plants/year in tons: ")
a1=y0*(44/12)
print(a1)

print("Predicted Pineapple plants:")
print(Total_Pine_trees_Predicted)
print("Predicted Total additionality of C stored in Pineapple plants/year in tons: ")
b1=x0*Total_Pine_trees_Predicted
print(b1)

print("Predicted Total additionality of C02 stored in Pineapple plants/year in tons: ")
c1=x0*Total_Pine_trees_Predicted*(44/12)
print(c1)

#Total carbon (Rubber + Pineapple)

print("Actual Trees/plants:")
print('115000')

print("Actual Total additionality of C stored in total trees/year in tons: ")
print((y+y0))

print("Actual Total additionality of C02 stored in total trees/year in tons: ")
print(a+a1)

print("Predicted total trees:")
print(Total_Rubber_trees_Predicted+Total_Pine_trees_Predicted)
print("Predicted Total additionality of C stored in total trees/year in tons: ")
print(b+b1)

print("Predicted Total additionality of C02 stored in total trees/year in tons: ")
print(c+c1)

#Total c and co2 using linear regression

#Total additionality of C stored through plants for 2020 for all trees:
y5 = 516044.702344278*ln(x1)-3924235.21296304

#Total additionality of C stored through plants for 2021  all trees:
y6 = 516044.702344278*ln(x2)-3924235.21296304


#Total additionality of C stored through Trees/plants in a Year
y01= abs(y6-y5)

x01 = y01/(115000) #carbon per tree/plant in tons

print("Actual Trees/plants:")
print('115000')

print("Actual Total additionality of C stored in all trees and plants/year in tons: ")
print(y01)

print("Actual Total additionality of C02 stored in all trees plants/year in tons: ")
a11=y01*(44/12)
print(a11)

print("Predicted Trees/plants:")
print(Total_Rubber_trees_Predicted+Total_Pine_trees_Predicted)
print("Predicted Total additionality of C stored in all trees and plants/year in tons: ")
b11=x01*(Total_Rubber_trees_Predicted+Total_Pine_trees_Predicted)
print(b11)

print("Predicted Total additionality of C02 stored in all trees plants/year in tons: ")
c11=x01*(Total_Rubber_trees_Predicted+Total_Pine_trees_Predicted)*(44/12)
print(c11)