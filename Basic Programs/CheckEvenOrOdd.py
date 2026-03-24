####################################################
#
#     Algorithm
#
#     START 
#           Accept number as No
#           Call the function CheckEvenOrOdd
#           Check the number is divisile by 2 or not
#           If divisible then the number is even 
#           if Not the number is odd
#           Display the result
#     STOP
# 
###################################################

# /////////////////////////////////////////////////////////////////
# //
# //  Function Name : CheckEvenOrOdd
# //  Description :   It is used to check the number is odd or even         
# //  Output :        Display the number is odd or even
# //  Author :        Tushar vikas bhore.
# //  Date :          24/03/2025
# //
# /////////////////////////////////////////////////////////////////

def CheckEvenOrOdd( iNum ):

    if( iNum % 2 == 0 ):

        return True
    
    else:

        return False
    

#################################################################
#####
###
#       Entry Point Function Of Application
###
#####
#################################################################

def main():

    iNumber = 0

    print( "Enter the number to check is it even or odd : " )
    iNumber = int ( input() )

    bRet = CheckEvenOrOdd( iNumber )

    if( bRet == True ):

        print( "The entered number" , iNumber ,"is even number." ) 

    else:

        print( "The entered number" , iNumber ,"is odd number." ) 

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
#       Input1 : 10 
#       Output : The entered number 10 is even number.
#
#       Input2 : 11 
#       Output : The entered number 11 is odd number.
##
####
######
#############################################################
