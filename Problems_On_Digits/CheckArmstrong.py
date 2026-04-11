class CheckArmstrongLogic:

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
        # //  Date :          11/04/2026
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
        ##########      Method Name :   isArmstrong()
        #######         
        #####           Description :   It is used to check the given number is armstrong or not
        ###
        ###             Author      :   Tushar Vikas Bhore.
        #####
        #######         Date        :   11th April 2026
        #########
        ############
        ##########################################################################################

    def isArmstrong( self ):

        """The method is used to check the given number is armstrong or not."""

        iCount : int = self.CountDigit( )
        
        iNumber : int = self.iNum
        fSum : float = 0.0
        iDigit  : int = 0

        while( iNumber != 0 ):

            iDigit = iNumber % 10

            ### Used built in pow function to calculate the power
            fSum = fSum + pow( iDigit , iCount )

            iNumber = iNumber // 10

        return ( self.iNum == fSum )

class CheckArmstrong:

    def main():

        iNum : int = 0

        print( "Enter the number to check is it armstrong or not :\t" )
        
        try:
                

            iNum = int( input() )

            if( iNum <= 0 ):

                print( "Error : Please provide valid input." )
                
                return
        
            calobj = CheckArmstrongLogic( iNum )

            bRet : bool = calobj.isArmstrong()

            if( bRet == True ):

                print( f"The entered number { iNum } is an armstong number.")

            else:

                print( f"The entered number { iNum } is not an armstong number.")

        except ValueError:

            print( "Invalid value.Please provide valid value only in number." )

        ###############################################################
        #####
        #######       End Of main()
        #####
        ###############################################################

    #############################################
    ###
    ####        End Of Class CheckArmstrong
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
# //            Enter the number to check is it armstrong or not :
# //                556
# //            The entered number 556 is not an armstong number.
# //
# //    
# //        TestCase : 2
# //
# //            Enter the number to check is it armstrong or not :
# //                5bbj
# //            Invalid value.Please provide valid value only in number.
# //
# //        TestCase : 3
# //            
# //            Enter the number to check is it armstrong or not :
# //                153
# //            The entered number 153 is an armstong number.
# //
# /////////////////////////////////////////////////////////////////
#####################################################################



        
