'''
SIMPLE INTEREST CALCULATOR
By Lucas LeVieux
(c) 2015

CHANGELOG

3.0:
    Introducing compound interest
    While loops allow errors to be corrected
    Prompts the user to select simple or compound
    This project is now on github at https://github.com/llevieux/Simple-Interest-Calculator
    The CHANGELOG has changed!  Surprised?
    
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
    return p+interest(p,r,t)

def c_accrued(p,r,t,n): #takes principal, rate, time, and interval (all numbers), returns compound accrued amount
    [p,r,t,n] = validate([p,r,t,n])
    return p*(1 + r/n)**(r*t)

interesttype = " "
interval = 0
while True: #loops until valid input is given
    interesttype = raw_input('Compound or Simple interest? ')
    if interesttype[0].lower() != 'c' and interesttype[0].lower() != 's':
        print "INPUT ERROR: %s is not a valid interest type\n" % interesttype
    else:
        break

principal = raw_input('\nPrinipal amount: $')
rate = raw_input('Rate (decimal form): ')
time = raw_input('Time (unit consistent with rate): ')

if interesttype[0].lower() == 'c': #compound interest block
    while True: #loops until valid input
        interval = raw_input('Compounding intervals per (unit): ')
        if validate([interval])[0]<=0:
            print "INPUT ERROR: %s is not a valid interval\n" % interval
        else:
            break
            
    print "\nAccrued amount: $" + str(c_accrued(principal, rate, time, interval)) #outputs accrued amount
    #print "Interest amount: $" + str(interest(principal, rate, time)) #outputs interest amount
    
elif interesttype[0].lower() == 's': #simple interest block
    print "\nAccrued amount: $" + str(accrued(principal, rate, time)) #outputs accrued amount
    print "Interest amount: $" + str(interest(principal, rate, time)) #outputs interest amount