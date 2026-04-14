#####################################################
# /*                                                        
#     Algorithm
#
#     START
#         Accept number as iNum
#         Reverse the digits of iNum
#         Compare reversed number with original iNum
#         If they match, it is a Palindrome
#     STOP
# */
#
#####################################################

class CheckPalindromeLogic :

    def reverse_number( self , iNum : int ) :

        """The method is used to reverse the given number."""

        iTempNum : int = 0
        iTempNum : int = iNum

        iRevNum : int = 0
        
        iDigit : int = 0

        ##  Business logic to reverse the number
        while( iTempNum != 0 ):

            iDigit = iTempNum % 10

            iRevNum = iRevNum * 10 + iDigit

            iTempNum = iTempNum // 10

        return iRevNum
    
    ###     ___ End Of reverse_number() ___     ###

    def is_Palindrome( self , iNumber : int ):

        """The method is used to check the given number is palindrome or not."""

        iRevNum = self.reverse_number( iNumber )

        return ( iRevNum == iNumber )
        
    ###     ___ End Of is_palindrome() ___     ###


##########################################
###
####    End Of Class CheckPalindromeLogic
###
##########################################

class CheckPalindrome :

    @staticmethod
    def main():

        iNum : int = 0

        print( "Enter the number to check is it palindrome or not :\t")

        try:

            iNum = int( input() )
            bRet : bool  = False

            #   Input Validation
            if( iNum <= 0 ):

                print( "Error : Please provide the positive and non zero number only." )

                return

            cplobj = CheckPalindromeLogic()

            bRet = cplobj.is_Palindrome( iNum ) 

            if( bRet == True ):

                print( f"The entered number is { iNum } and it is palindrome number." )

            else :

                print( f"The entered number is { iNum } and it is not palindrome number." )

        except ValueError:

            print( "Invalid input.Please provide the valid input" )

    #__________ End of main() __________#

##### _______ ####   End Of Class CheckPalindrome ______ ####_______#####


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


#################################################################
###
##      TestCase    1 :
#           Enter the number to check is it palindrome or not :
###              121
##          The entered number is 121 and it is palindrome number.
#
###     TestCase    2 :
##        
#           Enter the number to check is it palindrome or not :
###              123654
##          The entered number is 123654 and it is not palindrome number.
#
###     TestCase    3 :
##
#          Enter the number to check is it palindrome or not :
#               s4
###        Invalid input.Please provide the valid input
##
#
##################################################################