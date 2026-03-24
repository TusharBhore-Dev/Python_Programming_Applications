####################################################
#
#     Algorithm
#
#     START 
#           Accept number as No
#           Check the number has factor betwn 2 to num -1
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

    for i in range( 2 , iNum  , 1 ):

        if( iNum % i == 0 ):
            
            return False
            break
    
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

