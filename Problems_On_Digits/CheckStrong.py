########################################################
#######################################
#####################
# /*
#     Algorithm
#
#     START
#         Accept number as iNum
#         Extract each digit from the number
#         Calculate factorial of each extracted digit
#         Sum the factorials of all digits
#         Compare the sum with original iNum
#     STOP
# */
#####################
#######################################
########################################################

class CheckStrongLogic :

    #   Private Characteristics
    __iNum : int = 0

    #   Parameterized constructor
    def __init__( self , iNumber : int ):

        self.__iNum = iNumber

    ## __ End Of Constructor __ ##

    @staticmethod
    def calc_factorial( iNum : int ) :

        """The method is used to calculate the factorial of number."""

        iFact : int = 1

        for i in range( 1 , iNum + 1 ):
            
            iFact = iFact * i

        return iFact
    
    ### ____  End of calc_factorial()  ____  ###

    def is_strong( self ) :

        """The method is used to check if the number is strong number or not"""

        iNumber : int = self.__iNum

        iDigit : int = 0
        iSumOfFactorialsOfDigs : int = 0

        ##  Business Logic

        while( iNumber != 0 ) :

            iDigit = iNumber % 10

            iSumOfFactorialsOfDigs = iSumOfFactorialsOfDigs + self.calc_factorial( iDigit )

            iNumber = iNumber // 10

        return ( iSumOfFactorialsOfDigs == self.__iNum )
    
    ### ____  End of is_strong()  ____  ###

###################################
#
### End Of Class CheckStrongLogic
#
###################################


class CheckStrong :

    @staticmethod
    def main():

        iNum : int = 0

        print( "Enter the number to check is it strong number or not :\t")

        try:

            iNum = int( input() )
            bRet : bool  = False

            #   Input Validation
            if( iNum <= 0 ):

                print( "Error : Please provide the positive and non zero number only." )

                return

            cslobj = CheckStrongLogic( iNum )

            bRet = cslobj.is_strong() 

            if( bRet == True ):

                print( f"The entered number is { iNum } and it is strong number." )

            else :

                print( f"The entered number is { iNum } and it is not strong number." )

        except ValueError:

            print( "Invalid input.Please provide the valid input" )

    #__________ End of main() __________#

##### _______ ####   End Of Class CheckStrong ______ ####_______#####


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


#############################################################################
###
##      TestCase 1 :
#
###         Enter the number to check is it strong number or not :
##              145
#           The entered number is 145 and it is strong number.
###
##      TestCase 2 :
#           Enter the number to check is it strong number or not :
###             123
##          The entered number is 123 and it is not strong number.
#
##############################################################################



