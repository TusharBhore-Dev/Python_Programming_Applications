####################################################
#
#     Algorithm
#
#     START 
#           Accept number as No
#           Iterate from 1 to the num and
#           if num is divisible then its factor
#           Display the factor 
#     STOP
# 
###################################################

# /////////////////////////////////////////////////////////////////
# //
# //  Function Name : DisplayFactors
# //  Description :   It is used to display the factors        
# //  Output :        Factors of entered number
# //  Author :        Tushar vikas bhore.
# //  Date :          24/03/2025
# //
# /////////////////////////////////////////////////////////////////

def DisplayFactors( iNo ):

    print( "The factors of the number ", iNo ," are as follow : " )
    for i in range( 1 , iNo + 1 ):

        if( iNo % i == 0 ):

            print(i)

#################################################################
#####
###
#       Entry Point Function Of Application
###
#####
#################################################################

def main():

    iNum = 0

    print( "Enter the number : " )
    iNum = int ( input() )

    if( iNum <= 0 ):

        print( "Error : Please enter the non zero and positive values only" )
        return
    
    DisplayFactors( iNum )

#    // End of main


##################################
#   Starter for the main function
##################################

if __name__ == "__main__":

    main()

