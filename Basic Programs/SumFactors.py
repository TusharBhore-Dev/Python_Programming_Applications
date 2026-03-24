
# /////////////////////////////////////////////////////////////////
# //
# //  Function Name : Subtraction
# //  Description :   It is used to calculate the sum of factors
# //  Input :         int  , int 
# //  Output :        Sum of factors of the entered number 
# //  Author :        Tushar vikas bhore.
# //  Date :          24/03/2025
# //
# /////////////////////////////////////////////////////////////////

def SumFactors( iNo ):

    iSum = 0

    for i in range( 1 , iNo + 1 ):

        if( iNo % i == 0 ):

            iSum = iSum + i

    return iSum

#################################################################
#####
###
#       Entry Point Function Of Application
###
#####
#################################################################

def main():

    iNum = 0
    iRet = 0

    print( "Enter the number : " )
    iNum = int ( input() )

    if( iNum <= 0 ):

        print( "Error : Please enter the non zero and positive values only" )
        return
    
    iRet = SumFactors( iNum )

    print( "The sum of the factors is : " ,iRet )

#    // End of main


##################################
#   Starter for the main function
##################################

if __name__ == "__main__":

    main()

