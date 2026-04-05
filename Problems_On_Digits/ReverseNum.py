class ReveseNumLogic:
        
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
        # //  Function Name : ReverseNum()
        # //  Description :   It is used to reverse the number         
        # //  Author :        Tushar vikas bhore
        # //  Date :          05/04/2026
        # //
        # ///////////////////////////////////////////////////////

    def ReverseNum( self ):

        iTempNum = 0
        iRevNum = 0
    
        iTempNum = self.iNum        #   //  Copied static characteristics to dont affect the original val

        while( iTempNum != 0 ):

            iDigit = iTempNum % 10

            iRevNum = iRevNum * 10 + iDigit     #   Logic to reverse the num

            iTempNum = iTempNum // 10       #   uSed floor division to get actual int without decimals
    
        return iRevNum
    
    ###############################################################
    ###
    ##
    #       End Of ReverseNum()
    ##
    ###
    ###############################################################
    
###############################################################
###
##
#       End Of Class ReveseNumLogic
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

        print( "Enter the number:\t" )
        
        try:
            
            iNum = int( input() )

            #// Input Validation
            if( iNum <= 0 ):

                print("Error : Please provide non zero and positive values only.")

                return
            

            sobj = ReveseNumLogic( iNum )
            iRet = sobj.ReverseNum()

            print( "The entered number is : " ,iNum )
            print( "The reversed number is : " ,iRet )


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
# //
# //  Testcases successfully handled by the application
# //
# //      TestCase 1 : 
# //
# //         Enter the number:
# //            1234
# //            The entered number is :  1234
# //            The reversed number is :  4321
# //
# //      TestCase 2 :
# //         Enter the number:
# //            dd
# //            Invalid input. Please enter a number again.
# //
# /////////////////////////////////////////////////////////////////
#####################################################################