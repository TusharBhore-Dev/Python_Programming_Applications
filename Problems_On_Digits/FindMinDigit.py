class FindMinDigitLogic:
        
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
        # //  Function Name : FindMinDigit()
        # //  Description :   It is used to find the smallest digit in a given number  
        # //  Author :        Tushar vikas bhore
        # //  Date :          05/04/2026
        # //
        # ///////////////////////////////////////////////////////

    def FindMinDigit( self ):

        iTempNum = 0
        iMinDig = 9
    
        iTempNum = self.iNum        #   //  Copied static characteristics to dont affect the original val

        while( iTempNum != 0 ):

            iDigit = iTempNum % 10

            if( iDigit < iMinDig ):

                iMinDig = iDigit

            iTempNum = iTempNum // 10       #   uSed floor division to get actual int without decimals
    
        return iMinDig
    
    ###############################################################
    ###
    ##
    #       End Of FindMinDigit()
    ##
    ###
    ###############################################################
    
###############################################################
###
##
#       End Of Class FindMinDigitLogic
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
            

            sobj = FindMinDigitLogic( iNum )
            iRet = sobj.FindMinDigit()

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
####        End Of Class FindMinDigit
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
# //            The largest digit in the number 526 is : 2 .
# //        
# //        TestCase : 2
# //            Enter the number:
# //                569
# //            The largest digit in the number 569 is : 5 .
# //    
# /////////////////////////////////////////////////////////////////
#####################################################################