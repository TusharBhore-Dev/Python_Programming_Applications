################################################
###############################
# /*
#     Algorithm
#
#     START
#         Accept number as iNum
#         Calculate cube of iNum
#         Count digits in iNum
#         Compare last digits of cube with iNum
#         If they match, it is Triomorphic
#     STOP
# */
###############################
################################################

class CheckTrioMorphicLogic:

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
        # //  Date :          15/04/2026
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
        ##########      Method Name :   is_triomorphic()
        #######         
        #####           Description :   It is used to check the given number is automorphic or not
        ###
        ###             Author      :   Tushar Vikas Bhore.
        #####
        #######         Date        :   15th April 2026
        #########
        ############
        ##########################################################################################

    def is_triomorphic( self ):

        """The method is used to check the given number is triomorphic or not."""

        iCountDig : int = self.CountDigit()

        iNumber : int = self.iNum
        iNumCube : int = iNumber * iNumber * iNumber
        iLastDigOfNum : int = 0
        iLastDigOfCube : int = 0
        iDigit : int = 0

        for i in range( 1 , iCountDig + 1 ):

            iDigit = iNumber % 10

            iLastDigOfNum = iLastDigOfNum * 10 + iDigit

            iNumber = iNumber // 10

            iDigit = iNumCube  % 10

            iLastDigOfCube = iLastDigOfCube * 10 + iDigit

            iNumCube = iNumCube // 10


        return ( iLastDigOfNum == iLastDigOfCube )

        #######################################
        ##
        ##  End Of is_triomorphic()
        ##
        #######################################
        

    #######################################
    ##
    ##  End Of Class CheckTriomorphicLogic
    ##
    #######################################

class CheckTriomorphic:

    def main():

        iNum : int = 0

        print( "Enter the number to check is it triomorphic or not :\t" )
        
        try:
                

            iNum = int( input() )

            if( iNum <= 0 ):

                print( "Error : Please provide valid input." )
                
                return
        
            calobj = CheckTrioMorphicLogic( iNum )

            bRet : bool = calobj.is_triomorphic()

            if( bRet == True ):

                print( f"The entered number { iNum } is an triomorphic number.")

            else:

                print( f"The entered number { iNum } is not an triomorphic number.")

        except ValueError:

            print( "Invalid value.Please provide valid value only in number." )

        ###############################################################
        #####
        #######       End Of main()
        #####
        ###############################################################

    #############################################
    ###
    ####        End Of Class CheckTriomorphic
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
# //            Enter the number to check is it triomorphic or not :
# //                625
# //            The entered number 625 is an triomorphic number.
# //
# //        TestCase : 2
# //
# //            Enter the number to check is it triomorphic or not :
# //                25
# //            The entered number 25 is an triomorphic number.
# //
# //        TestCase : 3
# //            
# //            Enter the number to check is it triomorphic or not :
# //                kj
# //            Invalid value.Please provide valid value only in number.
# //
# /////////////////////////////////////////////////////////////////
#####################################################################



        
