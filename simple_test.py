import blynklib
##############################################
# Obtained from the app or server admin page #
##############################################
BLYNK_AUTH = 'YOUR_API_KEY_HERE'



####################################
# initialize Blynk in this script. #
####################################

## blynk = blynklib.Blynk(BLYNK_AUTH, server='server_ip_address', port='8080')

############################################
# IF USING A LOCAL OR SELF HOSTED SERVER   #
# UNCOMMENT the line ABOVE and COMMENT the #
# line BELOW				   #
############################################

blynk = blynklib.blynk(BLYNK_AUTH)

###################################################################
# Generic event handler will print the value from                 #
# control device (Phone, tablet, etc) from widget attached to "V0"#
###################################################################

@blynk.handle_event('write V0')  # Waiting to read data -  written to V0 -
def generic_input(pin, value):   # What we want to do with the data
    msg = "Virtual Pin Number {0} Value: {1}".format(pin, value) # Formatted message that the device  will print
    print(msg) # Print the message

# Run forever or until keyboard interrupt.
while True:
    blynk.run()
