# /////////////////////////////////////////////////////////
# //////
# ////
# ///     Expected Pattern : * * * * *
# ///
# ////
# /////
# /////////////////////////////////////////////////////////


# /////////////////////////////////////////////////////////////////
# //
# //  Function Name : DisplayPattern()
# //  Description :   It is used to display the stars in a row using while loop. 
# //  Input :         int
# //  Output :        stars in a row
# //  Author :        Tushar vikas bhore.
# //  Date :          30/03/2025
# //
# /////////////////////////////////////////////////////////////////


def DisplayPattern( iLim ):

   i = 1
   while( i <= iLim ):
           
        print( "*" , end = "\t" )

        i = i + 1

# End of DisplayPattern() 


#################################################################
#####
###
#       Entry Point Function Of Application
###
#####
#################################################################

def main():

    iLimit = 0

    print( "Enter how many stars you want to display :\t" )
    iLimit = int( input() )

    if iLimit < 0 :

        print( "Error : Please provide the valid input." )
        
        return

    DisplayPattern( iLimit )

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
#                   Enter how many stars you want to display :
#                   
#                       5
#                   
#                       *       *       *       *       *  
#
#
########
##########  TestCase 2 :
########
#                   Enter how many stars you want to display :
#                       11
#                       *       *       *       *       *       *       *       *       *       *       *
# #
########
##########  TestCase 3 :
########
#
#                   Enter how many stars you want to display :
#                       -5
#                        Error : Please provide the valid input.
#
#################################
##########################################################
##########################################################