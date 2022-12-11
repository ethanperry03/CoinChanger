# Ethan Perry
# 02/25/2022

import math

def changer(x):
     return math.trunc(x)

def main():
# greeting phase
     
     print('-'*45,
          "\n\n",
          "Hello, welcome to the Republic of Bananaria.")
     NAME = input("Please enter your name to start: ")
     print("Thank you,", NAME)
     INPUTINCOME = float(input("Please enter your yearly income w/ 2 decimals: "))
     
     print(f"\n{'-'*45}")
# end of greeting phase
    
    
# Random number generation using 10000 to get more decimals in tax rate
# since random yeilds integers
     import random
     tax_percent = random.randrange(1, 10000)
     tax = tax_percent / 10000
     
# Defining constants for coin calculations
     ACOIN_CENTS = 1024
     BCOIN_CENTS = 256
     CCOIN_CENTS = 100
     DCOIN_CENTS = 50
     ECOIN_CENTS = 10
     FCOIN_CENTS = 1
     
     ACOIN_DOLS = 10.24
     BCOIN_DOLS = 2.56
     CCOIN_DOLS = 1.00
     DCOIN_DOLS = 0.50
     ECOIN_DOLS = 0.10
     FCOIN_DOLS = 0.01
     
# start of coin calculation by converting into cents
     incometaxed = INPUTINCOME * tax
     TAXED = incometaxed * 100
    
     AcoinFloat = TAXED // ACOIN_CENTS
     balance = TAXED - (AcoinFloat * ACOIN_CENTS)
     Avalue = float(format(AcoinFloat * ACOIN_DOLS, '.2f'))
     acoinFINAL = changer(AcoinFloat)
     
     BcoinFloat = balance // BCOIN_CENTS
     balance = balance - (BcoinFloat * BCOIN_CENTS)
     Bvalue = float(format(BcoinFloat * BCOIN_DOLS, '.2f'))
     bcoinFINAL = changer(BcoinFloat)
    
     CcoinFloat = balance // CCOIN_CENTS
     balance = balance - (CcoinFloat * CCOIN_CENTS)
     Cvalue = float(format(CcoinFloat * CCOIN_DOLS, '.2f'))
     ccoinFINAL = changer(CcoinFloat)
    
     DcoinFloat = balance // DCOIN_CENTS
     balance = balance - (DcoinFloat * DCOIN_CENTS)
     Dvalue = float(format(DcoinFloat * DCOIN_DOLS, '.2f'))
     dcoinFINAL = changer(DcoinFloat)
    
     EcoinFloat = balance // ECOIN_CENTS
     balance = balance - (EcoinFloat * ECOIN_CENTS)
     Evalue = float(format(EcoinFloat * ECOIN_DOLS, '.2f'))
     ecoinFINAL = changer(EcoinFloat)
    
     FcoinFloat = balance // FCOIN_CENTS
     Fvalue = float(format(FcoinFloat * FCOIN_DOLS, '.2f'))
     fcoinFINAL = changer(FcoinFloat)
     
# sum all numbers of coins to get minimum total
# all lowercase are the final values used to print
     incometaxed_decimal = float('{:.2f}'.format(incometaxed))
     
     COINSFINAL = acoinFINAL + bcoinFINAL + ccoinFINAL 
     + dcoinFINAL + ecoinFINAL + fcoinFINAL
     
     
   
# larger line by line print statement to get table
     print(f"Your tax rate is: {tax:.3f}",
        f"\nYou must", f"pay {incometaxed:.2f}", 
        f"in tax using {COINSFINAL:.0f}", "coins",
        f"\n{'':-^45}",
        f"\n{'Coin Type:':>11}{'Number:':>13}{'Value:':>13}",
        f"\n{'1024 ¢ coin':>11}{acoinFINAL:>11}{Avalue:>15}",
        f"\n{'256 ¢ coin':>11}{bcoinFINAL:>11}{Bvalue:>15}",
        f"\n{'100 ¢ coin':>11}{ccoinFINAL:>11}{Cvalue:>15}",
        f"\n{'50 ¢ coin':>11}{dcoinFINAL:>11}{Dvalue:>15}",
        f"\n{'10 ¢ coin':>11}{ecoinFINAL:>11}{Evalue:>15}",
        f"\n{'1 ¢ coin':>11}{fcoinFINAL:>11}{Fvalue:>15}",
        f"\n{'':-^45}",
        f"\n{'Totals:':>11}{COINSFINAL:>11}{incometaxed_decimal:>15}", 
        f"\n{'':-^45}",
        )
   
# if else statements for Kings statement
# depending on random tax rate from above
     print("A message from His Magesty:")
     
     if tax <= .1:
          return "I am pleased with your loyalty."
     elif .1 < tax < .25:
          return "Your loyalty is adequate."
     elif .25 <= tax <=  .40:
          return "You must improve your work."
     elif .40 < tax < .55:
          return "You are on thin ice."
     elif .55 <= tax < .65:
          return "My men are on their way..."
     else:
          print("You are an official enemy of the state,", 
                f"\n{'You are being taxed accordingly!'}")       
    
main()