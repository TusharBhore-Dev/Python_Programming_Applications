
class CheckNeonLogic :

    @staticmethod
    def sum_of_digits( iNumber : int ):

        """The method is used to calculate the sum of digits of given number"""

        iDigit : int = 0
        iSum : int = 0

        #   Business logic to calculate the sum of digits 
        while( iNumber != 0 ):

            iDigit = iNumber % 10

            iSum = iSum + iDigit

            iNumber = iNumber // 10

        return iSum

    #__________ End of sum_of_digits() __________#

    def is_neon( self , iNum ):

        """The method is used to check the number is neon or not"""
        
        iNumSqre : int = 0
        iNumSqre = iNum * iNum

        iSumDigOfSqre : int = 0
        iSumDigOfSqre = self.sum_of_digits( iNumSqre )

        return( iNum == iSumDigOfSqre )

    #__________ End of is_neon() __________#

##### _______ ####   End Of Class CheckNeonLogic ______ ####_______#####

class CheckNeon :

    @staticmethod
    def main():

        iNum : int = 0

        print( "Enter the number to check is it neon or not :\t")

        try:

            iNum = int( input() )
            bRet : bool  = False

            #   Input Validation
            if( iNum <= 0 ):

                print( "Error : Please provide the positive and non zero number only." )

                return

            cnlobj = CheckNeonLogic()

            bRet = cnlobj.is_neon( iNum ) 

            if( bRet == True ):

                print( f"The entered number is { iNum } and it is neon number." )

            else :

                print( f"The entered number is { iNum } and it is not neon number." )

        except ValueError:

            print( "Invalid input.Please provide the valid input" )

    #__________ End of main() __________#

##### _______ ####   End Of Class CheckNeon ______ ####_______#####


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

##############################################################
####################################################################
####
#
###     TestCase 1 : Enter the number to check is it neon or not :
##                      9
#                    The entered number is 9 and it is neon number.
###
##
#
###     TestCase 2 : Enter the number to check is it neon or not :
##                      dbjk
#                    Invalid input.Please provide the valid input
###
##
#
###
##      TestCase 3 : Enter the number to check is it neon or not :
#                       5
###                  The entered number is 5 and it is not neon number.
##
#
###################################################################
################################################################

