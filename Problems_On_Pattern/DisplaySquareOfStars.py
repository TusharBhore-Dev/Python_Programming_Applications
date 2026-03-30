# /////////////////////////////////////////////////////////
# //////
# ////
# ///     Expected Pattern : * * * * * *
# //                         * * * * * *
# ///                        * * * * * *
# ////
# /////
# /////////////////////////////////////////////////////////

# /////////////////////////////////////////////////////////////////
# //
# //  Function Name : DisplayPattern()
# //  Description :   It is used to display the pattern.
# //  Input       :   int  , int
# //  OutPut      :    Pattern
# //  Author :        Tushar vikas bhore.
# //  Date :          31/03/2025
# //
# /////////////////////////////////////////////////////////////////

def DisplayPattern( iRow , iCol ):

    for i in range( 1 , iRow + 1 ):

        for j in range( 1 , iCol + 1 ):

            print( "*", end = "\t" )
    
        print( end = "\n" )

# End of DisplayPattern() 

#################################################################
#####
###
#       Entry Point Function Of Application
###
#####
#################################################################

def main():

    iRowLim = 0
    iColLim = 0

    print( "Enter how many rows you want to display :\t" )
    iRowLim = int( input() )

    print( "Enter how many rows you want to display :\t" )
    iColLim = int( input() )

    if iRowLim != iColLim :

        print( "Error : Please provide the valid input.( Equal  and positive number of rows and coloms )" )
        
        return

    DisplayPattern( iRowLim , iColLim )

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
#               
#                       Enter how many rows you want to display :
#                           4
#                       Enter how many rows you want to display :
#                           4
#                        *       *       *       *
#                        *       *       *       *
#                        *       *       *       *
#                        *       *       *       *
#
#
########
##########  TestCase 2 :
########
# 
#                       Enter how many rows you want to display :
#                           3
#                       Enter how many rows you want to display :
#                           3
#                        *       *       *     
#                        *       *       *       
#                        *       *       *            
#
#
########
##########  TestCase 3 :
########
#
#                       Enter how many rows you want to display :
#                           5
#                       Enter how many rows you want to display :
#                           8
#                       Error : Please provide the valid input.( Equal  and positive number of rows and coloms )
#
#
#################################
##########################################################
##########################################################