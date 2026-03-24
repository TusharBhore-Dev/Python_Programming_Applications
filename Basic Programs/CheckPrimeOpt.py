####################################################
#
#     Algorithm
#
#     START 
#           Accept number as No
#           Check the number has factor betwn 2 to half of the number
#           If yes then the number is not prime 
#           if Not the number is prime
#           Display the result
#     STOP
# 
###################################################

# /////////////////////////////////////////////////////////////////
# //
# //  Function Name : CheckPrime
# //  Description :   It is used to check the number is prime  or not
# //  Input:           int          
# //  Output :        Display the number is prime or not
# //  Author :        Tushar vikas bhore.
# //  Date :          24/03/2025
# //
# /////////////////////////////////////////////////////////////////

def CheckPrime( iNum ):

    for i in range( 2 , ( ( iNum  // 2 ) + 1 )  , 1 ): # floor division used

        if( iNum % i == 0 ):
            
            return False
            break           # To break the loop as finds first factor
    
    return True

#################################################################
#####
###
#       Entry Point Function Of Application
###
#####
#################################################################

def main():

    iNum = 0

    print( "Enter the number to is it prime or not : " )
    iNum = int( input() )

    if( iNum == 1 ):

        print( "The number" , 1 , "is not prime." )
        return

    bRet = CheckPrime( iNum )

    if( bRet == True ):

        print( "The number ", iNum ," is prime." )
    
    else:
        
        print( "The number", iNum ,"is not prime." )

#    // End of main


##################################
#   Starter for the main function
##################################


if __name__ == "__main__":

    main()

