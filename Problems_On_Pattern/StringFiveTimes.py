
# /////////////////////////////////////////////////////////////////
# //
# //  Function Name : DisplayStr()
# //  Description :   It is used to display the string five times. 
# //  Input :         string 
# //  Output :        string displayed five times
# //  Author :        Tushar vikas bhore.
# //  Date :          30/03/2025
# //
# /////////////////////////////////////////////////////////////////

def DisplayStr( sString ):

    print( "The expected output is as follow : " )

    i = 0
    for i in range( 5 ):
        print( sString )
        
        #   End of DisplayStr

#################################################################
#####
###
#       Entry Point Function Of Application
###
#####
#################################################################

def main():

    sString = ""

    print( "Enter the string  to display five times : " ,end = "\t" )
    sString = ( input() )
    
    DisplayStr( sString )

#    // End of main


################################################
####
###
#       Starter Function For The APPLICATION
###
####
################################################

if __name__ == "__main__":
    
    main()