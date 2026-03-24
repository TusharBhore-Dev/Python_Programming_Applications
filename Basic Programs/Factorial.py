# /////////////////////////////////////////////////////////////////
# //
# //  Function Name : CalcFactorial
# //  Description :   It is used to calculate the factorial 
# //  Input :         int 
# //  Output :        Factorial of that number
# //  Author :        Tushar vikas bhore.
# //  Date :          24/03/2025
# //
# /////////////////////////////////////////////////////////////////

def CalcFactorial( iNum ):

    dFact = 1.0

    for i in range( 1 , iNum + 1 , 1 ):

        dFact = dFact * i
    
    return dFact

#################################################################
#####
###
#       Entry Point Function Of Application
###
#####
#################################################################

def main():

    iValue = 0

    print( "Enter the number to get its factorial : " )
    iValue = int( input() )

    dRet = CalcFactorial( iValue )

    print( "The factorial of " ,iValue , " is : " ,dRet )

#    // End of main


##################################
#   Starter for the main function
##################################

if __name__ == "__main__":

    main()

