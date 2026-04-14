##############################################
#############################################################
# /*
#     Algorithm
#
#     START
#         Accept number as iNum
#         Initialize sum to 0 and product to 1
#         Extract each digit from the number
#         Add the digit to sum and multiply it with product
#         If sum equals product, it is a Spy number
#     STOP
# */
#############################################################
##############################################

class CheckSpyLogic :

    def sum_of_digits( self , iNumber : int ) :

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

    def calc_product_of_digs( self , iNumber : int ) :

        """The method is used to calculate the product of digits in the given number"""

        iDigit : int = 0
        iProduct : int = 1

        iTempNum : int = iNumber

        #   Business logic to calculate product of digits
        while( iTempNum != 0 ):

            iDigit = iTempNum % 10 

            iProduct = iProduct * iDigit

            iTempNum = iTempNum // 10

        return iProduct
        
    # _________ End Of calc_product_of_digs() _________ #

    def is_spy( self , iNum : int ) :

        iSumOfDigs = self.sum_of_digits( iNum )
        iProductOfDigs = self.calc_product_of_digs( iNum )

        return( iSumOfDigs == iProductOfDigs )
    
    # _________ End Of is_spy() _________ #

class CheckSpy :

    @staticmethod
    def main():

        iNum : int = 0

        print( "Enter the number to check is it spy or not :\t")

        try:

            iNum = int( input() )
            bRet : bool  = False

            #   Input Validation
            if( iNum <= 0 ):

                print( "Error : Please provide the positive and non zero number only." )

                return

            cslobj = CheckSpyLogic()

            bRet = cslobj.is_spy( iNum ) 

            if( bRet == True ):

                print( f"The entered number is { iNum } and it is spy number." )

            else :

                print( f"The entered number is { iNum } and it is not spy number." )

        except ValueError:

            print( "Invalid input.Please provide the valid input" )

    #__________ End of main() __________#

##### _______ ####   End Of Class CheckSpy ______ ####_______#####


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
###                     Enter the number to check is it spy or not :
##                          123
#                       The entered number is 123 and it is spy number.
###
##      TestCase 2 :
#                       Enter the number to check is it spy or not :
###                         129
##                      The entered number is 129 and it is not spy number.
#
###     TestCase 3 :
##
#                       Enter the number to check is it spy or not :
###                         5d
##                      Invalid input.Please provide the valid input
#
##############################################################################