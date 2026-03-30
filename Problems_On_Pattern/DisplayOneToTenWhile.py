
# /////////////////////////////////////////////////////////////////
# //
# //  Function Name : DisplayOneToTenWhile()
# //  Description :   It is used to display the digits 1 to 10 using while loop. 
# //  Output :        1 - 10 digits.
# //  Author :        Tushar vikas bhore.
# //  Date :          30/03/2025
# //
# /////////////////////////////////////////////////////////////////

def DisplayOneToTenWhile( ):

    i = 1

    while( i < 11 ):

        print( i , end = "\t" )

        i = i + 1

# End of DisplayOneToTenWhile() 


#################################################################
#####
###
#       Entry Point Function Of Application
###
#####
#################################################################

def main():

    print( "The expected output is as follow : "  , end = "\n\n" )

    DisplayOneToTenWhile()

#    // End of main

################################################
####
###
#       Starter Function For The APPLICATION
###
####
################################################

if __name__ == "__main__":
    
    main()

#End of starter funtion

###########################################################
###########################################################
################################
#
#       TestCases Successfully Handled By The Application
#
########
##########  TestCase 1 :
########
#               The expected output is as follow :
#               1       2       3       4       5       6       7       8       9       10
# 
#################################
##########################################################
##########################################################