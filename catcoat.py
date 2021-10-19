# Dictionary then PnC of the genes.
# Cat will randomly get a random set of gene from both mum & dad

from random import randint

color_dict = {"BLACK":['B','-','D','-'], 
              "BLUE":['B','-','d','d'],
              "LILAC":['b','b','d','d'],
              "CHOCOLATE":['b','b','D','-'],
              "RED":['D','-','O','O'],
              "CREAM":['d','d','O','O'],
              "BLACK-RED TORTIE":['B','-','D','-','O','o'],
              "BLUE-CREAM TORTIE":['B','-','d','d','O','o'],
              "CHOCOLATE-RED TORTIE":['b','b','D','-','O','o'],
              "LILAC-CREAM TORTIE":['b','b','d','d','O','o']
              }

mom_color = color_dict[input().upper()]
dad_color = color_dict[input().upper()]

isMale = randint(0,1)
offspring_genes = []

if isMale:
    