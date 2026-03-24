
# /////////////////////////////////////////////////////////////////
# //
# //  Function Name : DisplayGreater
# //  Description :   It is used to find greater number
# //  Input :         int  , int , int
# //  Output :        Greater number
# //  Author :        Tushar vikas bhore.
# //  Date :          24/03/2025
# //
# /////////////////////////////////////////////////////////////////

def DisplayGreater( iNo1 , iNo2 , iNo3 ):

    if( iNo1 > iNo2 and iNo1 > iNo3 ):

        print( "The greater number is : " ,iNo1 )
    elif( iNo2 > iNo1 and iNo2 > iNo3 ):

        print( "The greater number is : " ,iNo2 )
    else:

        print( "The greater number is : " ,iNo3 )

#################################################################
#####
###
#       Entry Point Function Of Application
###
#####
#################################################################

def main():

    iValue1 = 0
    iValue2 = 0
    iValue3 = 0

    print( "Enter the first number : " )
    iValue1 = int ( input() )

    print( "Enter the second number : " )
    iValue2 = int ( input() )

    print( "Enter the third number : " )
    iValue3 = int ( input() )

    DisplayGreater( iValue1 , iValue2 , iValue3 )

#    // End of main


##################################
#   Starter for the main function
##################################

if __name__ == "__main__":

    main()

