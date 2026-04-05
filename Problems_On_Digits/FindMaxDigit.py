class FindMaxDigitLogic:
        
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
        # //  Function Name : FindMaxDigit()
        # //  Description :   It is used to find the largest digit in a given number  
        # //  Author :        Tushar vikas bhore
        # //  Date :          05/04/2026
        # //
        # ///////////////////////////////////////////////////////

    def FindMaxDigit( self ):

        iTempNum = 0
        iMaxDig = 0
    
        iTempNum = self.iNum        #   //  Copied static characteristics to dont affect the original val

        while( iTempNum != 0 ):

            iDigit = iTempNum % 10

            if( iDigit > iMaxDig ):

                iMaxDig = iDigit

            iTempNum = iTempNum // 10       #   uSed floor division to get actual int without decimals
    
        return iMaxDig
    
    ###############################################################
    ###
    ##
    #       End Of FindMaxDigit()
    ##
    ###
    ###############################################################
    
###############################################################
###
##
#       End Of Class FindMaxDigitLogic
##
###
###############################################################

class FindMaxDigit:

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
            

            sobj = FindMaxDigitLogic( iNum )
            iRet = sobj.FindMaxDigit()

            print( f"The largest digit in the number { iNum } is : { iRet } ." )


        except  ValueError :

            print( "Invalid input. Please enter a number again." )

    ###############################################################
    #####
    #######       End Of main()
    #####
    ###############################################################

#############################################
###
####        End Of Class FindMaxDigit
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
# //            Enter the number:
# //                526
# //            The largest digit in the number 526 is : 6 .
# //        
# //        TestCase : 2
# //            Enter the number:
# //                569
# //            The largest digit in the number 569 is : 9 .
# //    
# /////////////////////////////////////////////////////////////////
#####################################################################