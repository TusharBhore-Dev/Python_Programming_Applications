class ReveseDisplayNumLogic:
        
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
        # //  Function Name : ReverseDisplayNum()
        # //  Description :   It is used to reverse display all digits in a number         
        # //  Author :        Tushar vikas bhore
        # //  Date :          05/04/2026
        # //
        # //////////////////////////////////////////////////////////////////////////////

    def ReverseDisplayNum( self ):

        iTempNum = 0
    
        iTempNum = self.iNum        #   //  Copied static characteristics to dont affect the original val

        print("The entered number is : " , iTempNum )
        print("The reverse order of the digits is as follow :\n" )

        while( iTempNum != 0 ):

            iDigit = iTempNum % 10

            print( iDigit , end = "\t" )

            iTempNum = iTempNum // 10       #   uSed floor division to get actual int without decimals
    
    ###############################################################
    ###
    ##
    #       End Of ReverseDisplayNum()
    ##
    ###
    ###############################################################
    
###############################################################
###
##
#       End Of Class ReveseDisplayNumLogic
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

        print( "Enter the number:\t" )
        
        try:
            
            iNum = int( input() )

            #// Input Validation
            if( iNum <= 0 ):

                print("Error : Please provide non zero and positive values only.")

                return
            

            sobj = ReveseDisplayNumLogic( iNum )
            sobj.ReverseDisplayNum()

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
# //        Enter the number:
# //        12365
# //        The entered number is :  12365
# //        The reverse order of the digits is as follow :
#
# //                5       6       3       2       1
# //      TestCase 2 :
# //        Enter the number:
# //        sk4
# //        Invalid input. Please enter a number again.
# /////////////////////////////////////////////////////////////////
#####################################################################