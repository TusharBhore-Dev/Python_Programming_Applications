################################################
###############################
# /*
#     Algorithm
#
#     START
#         Accept number as iNum
#         Calculate square of iNum
#         Count digits in iNum
#         Extract last 'n' digits of square
#         Compare extracted digits with iNum
#     STOP
# */
###############################
################################################

class CheckAutomorphicLogic:

    ##//#   Private Characteristics 
    
    iNum : int = 0

    ##  Parameterized Constructor
    def __init__( self , iNum : int ):

        self.iNum = iNum

        # ////////////////////////////////////////////////////////
        # //
        # //  Function Name : CountDigit()
        # //  Description :   It is used to count the digits in a given number  
        # //  Author :        Tushar vikas bhore
        # //  Date :          13/04/2026
        # //
        # ///////////////////////////////////////////////////////

    def CountDigit( self ):

        """The method is used to count the digits in the number."""

        iCount : int = 0
        iTempNum = self.iNum
        iDigit : int = 0

        while( iTempNum != 0 ):

            iDigit = iTempNum % 10

            iCount = iCount + 1

            iTempNum = iTempNum // 10       #   uSed floor division to get actual int without decimals
    
        return iCount
    
        ###############################################################
        ###
        ##
        #       End Of CountDigit()
        ##
        ###
        ###############################################################
        

        #########################################################################################
        ############
        ##########      Method Name :   isAutomorphic()
        #######         
        #####           Description :   It is used to check the given number is automorphic or not
        ###
        ###             Author      :   Tushar Vikas Bhore.
        #####
        #######         Date        :   13th April 2026
        #########
        ############
        ##########################################################################################

    def isAutomorphic( self ):

        """The method is used to check the given number is automorphic or not."""

        iCountDig : int = self.CountDigit()

        iNumber : int = self.iNum
        iNumSqre : int = iNumber * iNumber
        iLastDigOfNum : int = 0
        iLastDigOfSqre : int = 0
        iDigit : int = 0

        for i in range( 1 , iCountDig + 1 ):

            iDigit = iNumber % 10

            iLastDigOfNum = iLastDigOfNum * 10 + iDigit

            iNumber = iNumber // 10

            iDigit = iNumSqre  % 10

            iLastDigOfSqre = iLastDigOfSqre * 10 + iDigit

            iNumSqre = iNumSqre // 10


        return ( iLastDigOfNum == iLastDigOfSqre )

        #######################################
        ##
        ##  End Of isAutomorphic()
        ##
        #######################################
        

    #######################################
    ##
    ##  End Of Class CheckAutomorphicLogic
    ##
    #######################################

class CheckAutomorphic:

    def main():

        iNum : int = 0

        print( "Enter the number to check is it automorphic or not :\t" )
        
        try:
                

            iNum = int( input() )

            if( iNum <= 0 ):

                print( "Error : Please provide valid input." )
                
                return
        
            calobj = CheckAutomorphicLogic( iNum )

            bRet : bool = calobj.isAutomorphic()

            if( bRet == True ):

                print( f"The entered number { iNum } is an automorphic number.")

            else:

                print( f"The entered number { iNum } is not an automorphic number.")

        except ValueError:

            print( "Invalid value.Please provide valid value only in number." )

        ###############################################################
        #####
        #######       End Of main()
        #####
        ###############################################################

    #############################################
    ###
    ####        End Of Class CheckAutomorphic
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
# //            Enter the number to check is it automorphic or not :
# //                625
# //            The entered number 625 is an automorphic number.
# //    
# //        TestCase : 2
# //
# //            Enter the number to check is it automorphic or not :
# //                6
# //            The entered number 6 is an automorphic number.
# //
# //        TestCase : 3
# //            
# //            Enter the number to check is it automorphic or not :
# //                kj
# //            Invalid value.Please provide valid value only in number.
# //
# /////////////////////////////////////////////////////////////////
#####################################################################



        
