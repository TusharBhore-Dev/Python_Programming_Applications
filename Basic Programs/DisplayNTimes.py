#################################################################
#####
###
#       Entry Point Function Of Application
###
#####
#################################################################

def main():

    sString = ""

    print( "Enter the string to display : " )
    sString = str ( input() )

    iLimit = 0

    print( "Enter how many times to display the entered string : " )
    iLimit = int ( input() )

    for i in range( iLimit ):

        print( sString )


#    // End of main


##################################
#   Starter for the main function
##################################

if __name__ == "__main__":

    main()

