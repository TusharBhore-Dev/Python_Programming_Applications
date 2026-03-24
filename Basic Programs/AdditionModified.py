# 
#     Algorithm
#
#     START 
#           Accept first number as No1
#           Accept second number as No2
#           Call the function Addition
#           Perform Addition of no1 & no2
#           Display the addition on screen
#     STOP
# 


# /////////////////////////////////////////////////////////////////
# //
# //  Function Name : Addition
# //  Description :   It is used to perform addition 
# //  Input :         int , int         
# //  Output :        Addition of two integer
# //  Author :        Tushar vikas bhore.
# //  Date :          24/03/2025
# //
# /////////////////////////////////////////////////////////////////

def Addition( A , B ):

    iAns = 0

    iAns = A + B 

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

    iRet = Addition( iNo1 , iNo2 )

    print( "The addition of the numbers is : " ,iRet )
#    // End of main

##################################
#   Starter for the main function
##################################

if __name__ == "__main__":

    main()


############################################################
######
####
##
#       Input1 : 10     Input2 : 11     Output : 21
##
####
######
#############################################################
