class CountDigitFreqLogic:
        
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
        # //  Function Name : CountDigitFreq()
        # //  Description :   It is used to count the frequency of digit in a given number  
        # //  Author :        Tushar vikas bhore
        # //  Date :          05/04/2026
        # //
        # ///////////////////////////////////////////////////////

    def CountDigitFreq( self , iDig  ):

        iTempNum = 0
        ifreq = 0
        iDigit = 0
    
        iTempNum = self.iNum        #   //  Copied static characteristics to dont affect the original val

        while( iTempNum != 0 ):

            iDigit = iTempNum % 10

            if( iDigit == iDig ):

                ifreq = ifreq + 1 
            
            iTempNum = iTempNum // 10       #   uSed floor division to get actual int without decimals
    
        return ifreq
    
    ###############################################################
    ###
    ##
    #       End Of CountDigitFreq()
    ##
    ###
    ###############################################################
    
###############################################################
###
##
#       End Of Class CountDigitFreqLogic
##
###
###############################################################

class CountDigitFreq:

    ###############################################################
    ###
    ##
    #       Entry point function for the application
    ##
    ###
    ###############################################################

    def main():

        iNum = 0 
        iDig = 0
        iRet = 0

        print( "Enter the number:\t" )

        try:
            
            iNum = int( input() )

            #// Input Validation
            if( iNum <= 0 ):

                print("Error : Please provide non zero and positive values only.")

                return
            
            print( "Enter the digit to find its frequency :\t")
        
            iDig = int( input() )

            #// Input Validation
            if( iDig <= 0 ):

                print("Error : Please provide non zero and positive values only.")

                return
            
            sobj = CountDigitFreqLogic( iNum )
            iRet = sobj.CountDigitFreq( iDig )

            print( f"The frequency of the digit { iDig } in the number is { iRet } ." )


        except  ValueError :

            print( "Invalid input. Please enter a number again." )

    ###############################################################
    #####
    #######       End Of main()
    #####
    ###############################################################

#############################################
###
####        End Of Class CountDigitFreq
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