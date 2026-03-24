
# /////////////////////////////////////////////////////////////////
# //
# //  Function Name : Division
# //  Description :   It is used to do division
# //  Input:           int , int           
# //  Output :        Display the division answer
# //  Author :        Tushar vikas bhore.
# //  Date :          24/03/2025
# //
# /////////////////////////////////////////////////////////////////

def Division( A , B ):

    iAns = 0

    iAns = A / B    #   Ans will be in floating point number

    return iAns
#################################################################
#####
###
#       Entry Point Function Of Application
###
#####
#################################################################

def main():

    iNo1 = 0

    iNo2 = 0

    iRet = 0
    
    print( "Enter the first number : " )
    iNo1 = int ( input() )

    print( "Enter the second number : " )
    iNo2 = int ( input() )

    if( iNo2 == 0 ):
        print( "The division by zero denominator is undefined." )
        return

    iRet = Division( iNo1 , iNo2 )

    print( "The division of the numbers is : " ,iRet )

#    // End of main


##################################
#   Starter for the main function
##################################

if __name__ == "__main__":

    main()


