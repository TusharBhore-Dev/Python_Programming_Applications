####################################################
#
#     Algorithm
#
#     START 
#           Accept year
#           Check the year has four digit or not
#           Check the year is divisible by 4
#           If yes the year is leap year 
#           if Not the year is not leap year
#           Display the result
#     STOP
# 
###################################################

# /////////////////////////////////////////////////////////////////
# //
# //  Function Name : CheckLeap
# //  Description :   It is used to check year is leap or not         
# //  Output :        Display the year is leap or not
# //  Author :        Tushar vikas bhore.
# //  Date :          24/03/2025
# //
# /////////////////////////////////////////////////////////////////

def CheckLeap( iYr ):

    return( iYr % 4 == 0 )  #   Check the year is divisible by four

#################################################################
#####
###
#       Entry Point Function Of Application
###
#####
#################################################################

def main():

    iYear = 0

    bRet = False

    print( "Enter the Year : " )
    iYear = int ( input() )

    if( iYear < 1000 or iYear > 10000 ):    

        print( "Error : Please enter the valid year which will contain four digit and its positive." )
        
        return
    
    bRet = CheckLeap( iYear )

    if( bRet == True ):

        print( "The entered year is leap year." )

    else:

        print( "The entered year is not a leap year.")

#    // End of main


##################################
#   Starter for the main function
##################################

if __name__ == "__main__"  :

    main()

############################################################
######
####
##
#       Input1 : 999
#       Output : Error : Please enter the valid year which will contain four digit and its positive.
#
#       Input2 : 2024
#       Output : The entered year is leap year.
##
####
######
#############################################################

