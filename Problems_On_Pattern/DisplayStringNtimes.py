
# /////////////////////////////////////////////////////////////////
# //
# //  Function Name : DisplayStringNTimes()
# //  Description :   It is used to display the string n times. 
# //  Input :         int , string 
# //  Output :        string displayed n times
# //  Author :        Tushar vikas bhore.
# //  Date :          30/03/2025
# //
# /////////////////////////////////////////////////////////////////

def DisplayStringNTimes( iLim , sString ):

    print( "The expected output is as follow : "  , end = "\n\n" )

    i = 0

    for i in range( 0 , iLim ):

        print( sString )

# End of DisplayStringNTimes() 


#################################################################
#####
###
#       Entry Point Function Of Application
###
#####
#################################################################

def main():

    sStr = ""
    iLimit = 0

    print( "Enter the string you want to display :\t" )
    sStr = str( input () )
    
    print( "Enter how many times you want to display the string :\t" )
    iLimit = int( input() )

    if iLimit < 0 :

        print( "Error : Please provide a valid nonzero and positive limit only." )
        return
    
    DisplayStringNTimes( iLimit , sStr )

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

#End of starter funtion

###########################################################
###########################################################
################################
#
#       TestCases Successfully Handled By The Application
#
########
##########  TestCase 1 :
########
#
# Enter the string you want to display :
# Jay Ganesh...
# Enter how many times you want to display the string :
# 11
# The expected output is as follow :
#
# Jay Ganesh...
# Jay Ganesh...
# Jay Ganesh...
# Jay Ganesh...
# Jay Ganesh...
# Jay Ganesh...
# Jay Ganesh...
# Jay Ganesh...
# Jay Ganesh...
# Jay Ganesh...
# Jay Ganesh...
#
########
##########  TestCase 2 :
########
# 
# Enter the string you want to display :
# Heii Tushar is here
# Enter how many times you want to display the string :
# 5
# The expected output is as follow :
#
# Heii Tushar is here
# Heii Tushar is here
# Heii Tushar is here
# Heii Tushar is here
# Heii Tushar is here
#
########
##########  TestCase 3 :
########
#
#  Enter the string you want to display :
# Python
# Enter how many times you want to display the string :
# -5
# Error : Please provide a valid nonzero and positive limit only.
#
########
##########  TestCase 4 :
########
#
# Enter the string you want to display :
# Tushar
# Enter how many times you want to display the string :
# 0
# The expected output is as follow :
#
#
#
#################################
##########################################################
##########################################################