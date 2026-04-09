#################################################################################
#
#       Algorithm : 
# 
#                       Start
#                       Initialize the three variables as first sec and res
#                       Assign the first  and res variable with 0 
#                       Assign the second variable with 1
#                       Accept range from user and itterate loop upto the range
#
#                       Display the first every time loop itterate
#                       assign the second value to first and res value to second
#                       
#
#################################################################################


class DisplayFibonnacciWhileLogic:

        #  Static characteristics of the class 
    iRange = 0

    #   Parameterized constructor
    def __init__( self , iRange ):

        self.iRange = iRange

        ############################
        #   End Of Constructor
        ############################

        # ////////////////////////////////////////////////////////
        # //
        # //  Function Name : DisplayFibonnacciWhile()
        # //  Description :   It is used to display the elements of fibonnacci series upto the range 
        # //  Author :        Tushar vikas bhore
        # //  Date :          09/04/2026
        # //
        # ///////////////////////////////////////////////////////

    def DisplayFibonnacciWhile( self ):

        """

            Description : The method DisplayFibonnacci() is going to display the 
            elements of the fibonnacci series upto the specified range that user want.

        """

        iFirst = 0
        iSecond = 1
        iRes = 0

        print( "The fibonnacci series is as follow :\n" )

        ##//##//##  Business Logic

        i = 0

        while( i < self.iRange ):

            print( iFirst , end="\t" )

            iRes = iFirst + iSecond
            
            iFirst = iSecond            
            iSecond = iRes

            i = i + 1

    ###############################################################
    ###
    ##
    #       End Of DisplayFibonnacciWhile()
    ##
    ###
    ###############################################################
    
###############################################################
###
##
#       End Of Class DisplayFibonnacciWhileLogic
##
###
###############################################################


class DisplayFibonnacciWhile:

    def main( ):

        iLimit = 0 

        print( "Enter the range to display the elements of fibonnacci series :\t" )
        
        try:
        
            iLimit = int ( input() )
            
            #// Input Validation
            if( iLimit <= 0 ):

                print("Error : Please provide non zero and positive values only.")

                return
            
            dfilobj = DisplayFibonnacciWhileLogic( iLimit )
            dfilobj.DisplayFibonnacciWhile()

        except  ValueError :

            print( "Invalid input. Please enter a number again." )

    ###############################################################
    #####
    #######       End Of main()
    #####
    ###############################################################

#############################################
###
####        End Of Class DisplayFibonnacciWhile
###
#############################################


###############################################
####
###
##
#       Starter function for the application
##
###
####
###############################################

    if __name__ == "__main__":

        main()

#########################################
###
####    End Of Starter
###
#########################################


###################################################################
# //
# //  Testcases successfully handled by the application
# //    
# //        TestCase : 1
# //    
# //        Enter the range to display the elements of fibonnacci series :
# //            8
# //        The fibonnacci series is as follow :
# // 
# //            0       1       1       2       3       5       8       13
# //        
# /////////////////////////////////////////////////////////////////
#####################################################################
        




