
# /////////////////////////////////////////////////////////////////
# //
# //  Function Name : DisplayOneToTen()
# //  Description :   It is used to display the digits 1 to 10. 
# //  Output :        1 - 10 digits.
# //  Author :        Tushar vikas bhore.
# //  Date :          30/03/2025
# //
# /////////////////////////////////////////////////////////////////

def DisplayOneToTen( ):

    i = 0

    for i in range( 1 , 11 ):

        print( i , end = "\t" )

# End of DisplayOneToTen() 


#################################################################
#####
###
#       Entry Point Function Of Application
###
#####
#################################################################

def main():

    print( "The expected output is as follow : "  , end = "\n\n" )

    DisplayOneToTen()

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