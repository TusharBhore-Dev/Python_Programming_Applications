class CountDigitLogic:
        
    #Static variables of class

    iNum = 0

        #// Parameterized Constructor

    def __init__( self , iNum ):

        self.iNum = iNum

        ############################
        #   End Of Constructor
        ############################

        # ////////////////////////////////////////////////////////
        # //
        # //  Function Name : CountDigitX()
        # //  Description :   It is used to count the digits in a given number  
        # //  Author :        Tushar vikas bhore
        # //  Date :          05/04/2026
        # //
        # ///////////////////////////////////////////////////////

    def CountDigitX( self ):

        iTempNum = 0
        iCount = 0
    
        iTempNum = self.iNum        #   //  Copied static characteristics to dont affect the original val

        while( iTempNum != 0 ):

            # {{{{{{   //  Removed iDigit variable  }}}}}}

            iCount = iCount + 1

            iTempNum = iTempNum // 10       #   uSed floor division to get actual int without decimals
    
        return iCount
    
    ###############################################################
    ###
    ##
    #       End Of CountDigitX()
    ##
    ###
    ###############################################################
    
###############################################################
###
##
#       End Of Class CountDigitLogic
##
###
###############################################################

class CountDigitX:

    ###############################################################
    ###
    ##
    #       Entry point function for the application
    ##
    ###
    ###############################################################

    def main( ):

        iNum = 0 
        iRet = 0

        print( "Enter the number:\t" )
        
        try:
            
            iNum = int( input() )

            #// Input Validation
            if( iNum <= 0 ):

                print("Error : Please provide non zero and positive values only.")

                return
            

            sobj = CountDigitLogic( iNum )
            iRet = sobj.CountDigitX()

            print( f"There are { iRet } digits in the number { iNum } ." )


        except  ValueError :

            print( "Invalid input. Please enter a number again." )

    ###############################################################
    #####
    #######       End Of main()
    #####
    ###############################################################

#############################################
###
####        End Of Class CountDigitX
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
# //            Enter the number:
# //                123
# //            There are 3 digits in the number 123 .
# //
# //    
# //        TestCase : 2
# //
# //            Enter the number:
# //                5268
# //            There are 4 digits in the number 5268 .    
# //        
# //        TestCase : 3
# //            Enter the number:
# //                fsd
# //            Invalid input. Please enter a number again.
# //
# /////////////////////////////////////////////////////////////////
#####################################################################