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

    iValue1 = 10
    iValue2 = 11

    iRet = 0

    iRet = Addition( iValue1 , iValue2 )

    print( "The addition is : " ,iRet )
#    // End of main


##################################
#   Starter for the main function
##################################
if __name__ == "__main__":

    main()


############################################################
######
####
##      Output : The addition is : 21
####
######
#############################################################
