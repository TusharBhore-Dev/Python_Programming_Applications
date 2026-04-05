class SumOfDigitLogic:
        
    #Static variables of class

    iNum = 0

        #// Parameterized Constructor
    def __init__( self , iNum ):

        self.iNum = iNum

        ############################
        #   End Of Constructor
        ############################

        # //////////////////////////////////////////////////////////////////////////////
        # //
        # //  Function Name : CalculateSumOfDig()
        # //  Description :   It is used to calculate the sum of all digits in a number         
        # //  Author :        Tushar vikas bhore
        # //  Date :          05/04/2026
        # //
        # //////////////////////////////////////////////////////////////////////////////

    def CalculateSumOfDig( self ):

        iTempNum = 0
        iDigit = 0
        iSum = 0

        iTempNum = self.iNum        #   //  Copied static characteristics to dont affect the original val

        while( iTempNum != 0 ):

            iDigit = iTempNum % 10

            iSum = iSum + iDigit

            iTempNum = iTempNum // 10       #   uSed floor division to get actual int without decimals
        
        return iSum
    
    ###############################################################
    ###
    ##
    #       End Of CalculateSumOfDig()
    ##
    ###
    ###############################################################
    
###############################################################
###
##
#       End Of Class SumOfDigitLogic
##
###
###############################################################

class SumOfDigits:

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

        print( "Enter the number to get the sum of digits :\t" )
        
        try:
            
            iNum = int( input() )

            #// Input Validation
            if( iNum <= 0 ):

                print("Error : Please provide non zero and positive values only.")

                return
            

            sobj = SumOfDigitLogic(iNum)
            iRet = sobj.CalculateSumOfDig()

            print( f"The sum of the digits of the number  { iNum }  is : { iRet } ." )
        
        except  ValueError :

            print( "Invalid input. Please enter a number again." )

    ###############################################################
    #####
    #######       End Of main()
    #####
    ###############################################################
    

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
# /////////////////////////////////////////////////////////////////
# //
# //  Testcases successfully handled by the application
# //
# //      TestCase 1 :
# //
# //          Enter the number to get the sum of digits :     123
# //
# //          The sum of the digits of the number 123 is : 6 .
# //
# //      TestCase 2 :
# //
# //          Enter the number to get the sum of digits :     258
# //
# //          The sum of the digits of the number 258 is : 15 .
# //
# # ////////////////////////////////////////////////////////////////
#####################################################################