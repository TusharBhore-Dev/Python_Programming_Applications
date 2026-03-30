
# /////////////////////////////////////////////////////////
# //////
# ////
# ///     Expected Pattern : 1    1   1   1   1
# //                         2    2   2   2   2
# ///                        3    3   3   3   3
# ////
# /////
# /////////////////////////////////////////////////////////

# /////////////////////////////////////////////////////////////////
# //
# //  Function Name : DisplayPattern()
# //  Description :   It is used to display the digit in a row using while.
# //  Input       :   int  , int
# //  OutPut      :    Pattern
# //  Author :        Tushar vikas bhore.
# //  Date :          30/03/2025
# //
# /////////////////////////////////////////////////////////////////

def DisplayPattern( iRow , iCol ):

    i = 1
    j = 1

    while( i <= iRow ):

        j = 1

        while( j <= iCol ):

            print( i , end = "\t" )

            j = j + 1
        
        i = i + 1    
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
#                        1       1       1       1
#                        2       2       2       2
#                        3       3       3       3
#                        4       4       4       4
#
########
##########  TestCase 2 :
########
# 
#                       Enter how many rows you want to display :
#                           5
#                       Enter how many rows you want to display :
#                           5
#                       1       1       1       1       1
#                       2       2       2       2       2
#                       3       3       3       3       3
#                       4       4       4       4       4
#                       5       5       5       5       5
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
########
##########  TestCase 4 :
########
#
#                       Enter how many rows you want to display :
#                          3
#                       Enter how many rows you want to display :
#                          3
#                                          
#                           1       1       1
#                           2       2       2
#                           3       3       3
#################################
##########################################################
##########################################################