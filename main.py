import string
import random
import os
import shutil
import requests

noneWorking = [0, 503, 4939, 4940, 4941, 12003, 5556, 5082]

userhome = os.path.expanduser('~')
desktop = userhome + '/Desktop/Pictures_From_IMGUR/'

if not os.path.exists(desktop):
    os.makedirs(desktop)

def main():
    while True:
        amount = int(''.join(random.choice('5' + '6') for _ in range(1)))
        if amount == 6:
            N = 3
            picture = str(''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(N)))
            picture2 = str(''.join(random.choice(string.digits + string.ascii_lowercase) for _ in range(N)))
            name = picture + picture2

            printsc = "http://i.imgur.com/" + "" + str(picture) + str(picture2) + ".jpg"
            line = str(name) + ".jpg"

            response = requests.get(printsc, stream=True)

            with open(desktop + line, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)

            size = os.path.getsize(desktop + line)

            if size in noneWorking:
                print ("[-] Invalid: " + str(name))
                os.remove(desktop + line)
            else:
                print ("[+] Valid: " + printsc)
        if amount == 5:
            N = 5

            picture = str(''.join(
                random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(N)))
            name = picture

            printsc = "http://i.imgur.com/" + "" + str(picture) + ".jpg"
            line = str(name) + ".jpg"

            response = requests.get(printsc, stream=True)

            with open(desktop + line, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)

            size = os.path.getsize(desktop + line)

            if size in noneWorking:
                print("[-] Invalid: " + str(name))
                os.remove(desktop + line)
            else:
                print("[+] Valid: " + printsc)


if __name__ == '__main__':
    main()
