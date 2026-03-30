# /////////////////////////////////////////////////////////
# //////
# ////
# ///     Expected Pattern : #    2   #   4   #   6
# //                         #    2   #   4   #   6
# ///                        #    2   #   4   #   6
# ////
# /////
# /////////////////////////////////////////////////////////

# /////////////////////////////////////////////////////////////////
# //
# //  Function Name : DisplayPattern()
# //  Description :   It is used to display the Pattern using while.
# //  Author :        Tushar vikas bhore.
# //  Date :          31/03/2025
# //
# /////////////////////////////////////////////////////////////////

def DisplayPattern( iRow , iCol ):

    i = 1
    j = 1

    while( i <= iRow ):

        j = 1

        while( j <= iCol ):

            #   Handling odd places
            if( j % 2 != 0 ):

                print( "#", end = "\t" )
            else :

                print( j , end = "\t")
            
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
#               Enter how many rows you want to display :
#                   4
#               Enter how many rows you want to display :
#                   4
#                   #       2       #       4
#                   #       2       #       4
#                   #       2       #       4
#                   #       2       #       4
#
#
#
########
##########  TestCase 2 :
########
#
#               Enter how many rows you want to display :
#                   5
#               Enter how many rows you want to display :
#                   5
#                   #       2       #       4       #
#                   #       2       #       4       #
#                   #       2       #       4       #
#                   #       2       #       4       #
#                   #       2       #       4       #
#
# 
########
##########  TestCase 3 :
########
#
#               Enter how many rows you want to display :
#                  -5
#               Enter how many rows you want to display :
#                   5
#               Error : Please provide the valid input.( Equal  and positive number of rows and coloms )
#
#
#################################
##########################################################
##########################################################