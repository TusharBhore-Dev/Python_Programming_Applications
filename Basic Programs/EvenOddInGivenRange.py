
# /////////////////////////////////////////////////////////////////
# //
# //  Function Name : DisplayEvenOddInRange
# //  Description :   It is used to display even or odd numbers in range  
# //  Input :         int , int         
# //  Output :        Even and odd numbers in range
# //  Author :        Tushar vikas bhore.
# //  Date :          24/03/2025
# //
# /////////////////////////////////////////////////////////////////

def DisplayEvenOddInRange( iStr , iEnd ):

    print( "The even numbers in given range are as follow : " , end = "\n" )

    for i in range( iStr , iEnd + 1 ):

        if ( i % 2 == 0 ):

            print( i , end = "\t" )

    print( end = "\n")
    
    print( "The odd numbers in given range are as follow : " , end = "\n" )

    for i in range( iStr , iEnd + 1 ):

        if ( i % 2 != 0 ):

            print( i , end = "\t" )

#################################################################
#####
###
#       Entry Point Function Of Application
###
#####
#################################################################

def main():

    iStart = 0
    iEnd = 0

    print( "Enter the starting point of the range : " )
    iStart = int ( input() )

    print( "Enter the ending point of the range : " )
    iEnd = int ( input() )

    if( iStart >= iEnd or iStart < 0 or iEnd < 0 ):

        print( "Error : Please enter the positive and valid range only." )
    
        return
    
    DisplayEvenOddInRange( iStart , iEnd )

#    // End of main


##################################
#   Starter for the main function
##################################

if __name__ == "__main__":

    main()
