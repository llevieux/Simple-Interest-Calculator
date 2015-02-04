'''
SIMPLE INTEREST CALCULATOR
By Lucas LeVieux
(c) 2015

CHANGELOG

2.0: 
    Based on feedback, I've created my own error messages instead of raise()ing the system messages (for added user friendliness)
    validate() now handles all type reassignments
    Prompts are spread to multiple lines for better readability
    Variable names are more clear
    Interest amount is now displayed along with accrued
    Prompts and outputs are now more accurately labeled (with units!)
    There is now a CHANGELOG!  Thank heavens!

1.0: 
    Initial release
'''

def validate(inarray): #makes sure each value in input array is valid
    for value in inarray:
        try:
            inarray[inarray.index(value)] = float(value)
        except:
            print "\nINPUT ERROR: %s is not a valid number" % str(value)
            exit()
        if value<0:
            print "\nINPUT ERROR: %s is a negative number" % str(value)
            exit()
    return inarray

def interest(p,r,t): #takes principal, rate, time (all numbers), returns interest amount
    [p,r,t] = validate([p,r,t])
    return p*r*t
    
def accrued(p,r,t): #takes principal, rate, time (all numbers), returns accrued amount
    [p,r,t] = validate([p,r,t])
    return p+inetrest(p,r,t)

principal = raw_input('Prinipal amount: $')
rate = raw_input('Rate (decimal form): ')
time = raw_input('Time (unit consistent with rate): ')
print "\nAccrued amount: $" + str(accrued(principal, rate, time)) #outputs accrued amount
print "Intrest amount: $" + str(interest(principal, rate, time)) #outputs interest amount