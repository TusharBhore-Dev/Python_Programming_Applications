
# /////////////////////////////////////////////////////////////////
# //
# //  Function Name : Multiplication
# //  Description :   It is used to display the multiplication
# //  Input :         int  , int 
# //  Output :        Answer of multiplication
# //  Author :        Tushar vikas bhore.
# //  Date :          24/03/2025
# //
# /////////////////////////////////////////////////////////////////

def Multiplication( A , B ):

    iAns = 0

    iAns = A * B 

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

    iRet = Multiplication( iNo1 , iNo2 )

    print( "The multiplication of the numbers is : " ,iRet )

#    // End of main


##################################
#   Starter for the main function
##################################

if __name__ == "__main__":

    main()


