#####################################################
#######################################
####################
# /*
#     Algorithm
#
#     START
#         Accept number as iNum
#         Calculate sum of all digits of iNum
#         Divide original iNum by the sum of digits
#         If remainder is 0, it is a Harshad number
#     STOP
# */
####################
#######################################
#####################################################

class CheckHarshadLogic:

    ##  Private characteristics of class
    iNum : int = 0

    #   Parameterized constructor 
    def __init__( self , iNumber : int ):

        self.iNum = iNumber

        # ////////////////////////////////////////////////////////
        # //
        # //  Function Name : sum_digits()
        # //  Description :   It is used to calculate the sum of digits in a given number  
        # //  Author :        Tushar vikas bhore
        # //  Date :          13/04/2026
        # //
        # ///////////////////////////////////////////////////////

    def sum_digits( self ):

        """The method is used to claculate the sum of the digits in the given number"""

        iNumber : int = self.iNum
        iSum : int = 0
        iDigit : int = 0

        while( iNumber != 0 ):

            iDigit = iNumber % 10

            iSum = iSum + iDigit

            iNumber = iNumber // 10

        return iSum
    
    ###########################
    #   End Of sum_digits
    ###########################


        ##################################################################
        #/////////////////////////////////////////////////////////////////
        # //
        # //  Function Name : is_harshad()
        # //  Description :   It is used to check whether a number is Harshad or not         
        # //  Author :        Tushar vikas bhore
        # //  Date :          14/04/2026
        # //
        # /////////////////////////////////////////////////////////////////
        ###################################################################

    def is_harshad( self ):

        """The method is used to check the given number is harshad or not"""

        iSumOfDigit  : int = 0
        iSumOfDigit = self.sum_digits()

        iNumber  : int = self.iNum

        return ( ( iNumber % iSumOfDigit ) == 0 )
    
    ###########################
    #   End Of is_harshad
    ###########################

##################################################
##########
#######
###
##          End Of Class CheckHarshadLogic
###
#######
##########
##################################################

class CheckHarshad:

    @staticmethod
    def main():

        iNum : int = 0

        print( "Enter the number to check is it harshad or not :\t" )
        
        try:
                

            iNum = int( input() )

            if( iNum <= 0 ):

                print( "Error : Please provide valid input." )
                
                return
        
            calobj = CheckHarshadLogic( iNum )

            bRet : bool = calobj.is_harshad()

            if( bRet == True ):

                print( f"The entered number { iNum } is an harshad number.")

            else:

                print( f"The entered number { iNum } is not an harshad number.")

        except ValueError:

            print( "Invalid value.Please provide valid value only in number." )

        ###############################################################
        #####
        #######       End Of main()
        #####
        ###############################################################

    #############################################
    ###
    ####        End Of Class CheckHarshad
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

##############################################################
####################################################################
####
##
#
###     TestCase 1 :
##                    Enter the number to check is it harshad or not :
##                          27
#                       The entered number 27 is an harshad number.
###
##      TestCase 2 :
#                    Enter the number to check is it harshad or not :
###                         24
##                      The entered number 24 is an harshad number.
#
###
##
#
###
##
#
###################################################################
################################################################