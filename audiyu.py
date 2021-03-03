__author__ = "evilDeimos()"
__date__ = "21 December - 2020" 

import PyPDF2
import pikepdf
import time
import sys
import threading
from gtts import gTTS
from pygame import mixer
from tqdm import tqdm


def audiyu():
    print("""
    
        ___             ___            
       /   | __  ______/ (_)_  ____  __
      / /| |/ / / / __  / / / / / / / /
     / ___ / /_/ / /_/ / / /_/ / /_/ / 
    /_/  |_\__,_/\__,_/_/\__, /\__,_/  
                        /____/         

    Welcome to Audiyu! Thank you for trusting us!
    =============================================
    What you want to do today?
    
    1) Decrypt and remove PDF's password
    2) PDF to Mp3 converter
    3) Music player
    4) Manual
    
    (choose 1,2,3,..)
    """)

    choose = input("")

    # PDF Decryptor
    if choose == '1':
        def pdfpass(input, passwor):
            with pikepdf.open(input, password=passwor) as pf:
                num_pages = len(pf.pages)
                print(f"Total pages: {num_pages}")
                pf.save(file[0:-4] + "-dec.pdf")


        file = input("File: ")
        passwd = input("Password: ")

        pdfpass(file, passwd)
        back = input('Back to home? (y/n) ')
        if back == 'y':
            audiyu()
        elif back == 'n':
            print("See you again!")
            time.sleep(1)
            quit()
        else:
            print('Please insert the right syntax!')
            quit()


    # PDF to MP3
    elif choose == '2':
        pdfName = input('File: ')

        # Open PDF and count tha pages

        pdf_file = open(pdfName, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdf_file)
        pages = pdfReader.numPages
        textList = []

        fromPage = input('From page: ')
        fromPage_indexed = int(fromPage) - 1
        endPoint = input('Custom endpoint(1) or the rest of the PDF(2)? (1 or 2) ')
        if endPoint == '1':
            untilPage = input('Until page: ')
            untilPage_indexed = int(untilPage)

        elif endPoint == '2':
            untilPage_indexed = pages

        else:
            print('please insert the right syntax')
            quit()

        mp3Name = input('Mp3 Name (without the .mp3 extension): ')

        # Extracting text data

        for i in tqdm(range(fromPage_indexed, untilPage_indexed)):
            try:
                page = pdfReader.getPage(i)
                textList.append(page.extractText())
            except:
                pass

        # Convert multiline text to a single line

        textString = " ".join(textList)
        bahasa = 'en'


        # GTS

        def GTS():
            nama = mp3Name + '.mp3'
            audiyu = gTTS(text=textString, lang=bahasa, slow=False)
            audiyu.save(nama)


        # Loading animation

        def animate():
            nama = mp3Name + '.mp3'
            chars = "/—\|"
            for char in chars:
                sys.stdout.write('\r' + 'loading..' + char)
                time.sleep(.1)
                sys.stdout.flush()


        theProc = threading.Thread(name='process', target=GTS)
        theProc.start()
        while theProc.is_alive():
            animate()
        back = input('\nBack to home? (y/n) ')
        if back == 'y':
            audiyu()
        elif back == 'n':
            print("See you again!")
            time.sleep(1)
            quit()
        else:
            print('Please insert the right syntax!')
            quit()


    # Music Player
    elif choose == '3':

        mixer.init()
        song = input('Mp3 File: ')
        mixer.music.load(song)
        mixer.music.set_volume(1)
        mixer.music.play()

        while True:

            print("Press 'p' to pause\nPress 'r' to resume\nPress 'e' to exit\nThen, press enter")
            xixi = input("  ")

            if xixi == 'p':
                mixer.music.pause()
            elif xixi == 'r':
                mixer.music.unpause()
            elif xixi == 'e':
                mixer.music.stop()
                break
            else:
                print(':)')
                pass
        back = input('Back to home? (y/n) ')
        if back == 'y':
            audiyu()
        elif back == 'n':
            print("See you again!")
            time.sleep(1)
            quit()
        else:
            print('Please insert the right syntax!')
            quit()


    # Manual
    elif choose == '4':
        print("""
        Welcome to Audiyu manual!
        So here is the complete how to- documentation to guide you to use this software
        
        I. Decrypt and remove PDF's password
            
            Basically this feature is going to remove your pdf's password forever. 
        So you won't need to insert the password over and over again. This feature
        meant to make your day easier, writer not responsible about the misleading 
        of Audiyu's usage.
        
        Example of usage:
        0. Install the required library through 'pip install -r requirements.txt'
        1. Start the program, open cmd or other command liner on that folder and 
           type 'python audiyu.py'
        2. Choose number 1 and press enter
        3. Insert the file name complete with the extension (.pdf), make sure it's 
           a pdf file and in the same folder with Audiyu
        4. Enter the password, it will show you the total page and check your folder,
           there will be a new pdf file with the same pdf's name but has a 'dec' name
        5. You can rename it later.
        
        II. PDF to Mp3 converter
        
            This feature has ability to convert PDF into a Mp3, so you can get a 
        audiobook version of your pdf for free. Currently the supported languange 
        is english. Later on, we will provide more languange. The speech machine is
        using a google translate's library (gTTS or google text to speech). As you 
        know that gTTS will convert text to speech, so first thing before convert it
        is to extract each word in the pdf file. 
        
        Example of usage:
        0. Install the required library through 'pip install -r requirements.txt'
        1. Start the program, open cmd or other command liner on that folder and 
           type 'python audiyu.py'
        2. Choose number 2 and press enter
        3. Insert the file name complete with the extension (.pdf), make sure it's 
           a pdf file and in the same folder with Audiyu. MAKE SURE IT'S NOT ENCRYPTED
        4. Insert the starting point of the PDF
        5. You'll need to choose custom endpoint or the rest of the page. If you want
           custom endpoint press 1 and press enter, if you want the rest of the book 
           than press 2 and enter. If you choose to, skip to step 7.
        6. Insert the custom endpoint. Make sure it's a number
        7. Insert the name of the Mp3 File, no need to type the .mp3 extension
        8. Please wait patiently until the program is done.
        
        III. Music Player
        
            To be honest this third feature is only a just for fun project because
        it's so simple to code and we believe that users will use another music player.
        So, don't complain lol.
        
        Example of usage:
        0. Install the required library through 'pip install -r requirements.txt'
        1. Start the program, open cmd or other command liner on that folder and 
           type 'python audiyu.py'
        2. Choose number 3 and press enter
        3. Insert the .mp3 file. Make sure you write the .mp3 extension
        4. The audio file will automatically played
        5. press 'p' and enter to pause, press 'r' and enter to resume, and press 
           'e' and enter to exit
        
        IV. Conclusion
        
            Audiyu is suitable for people that more comfortable to hearing than reading.
        Audiyu is suitable for people that more comfortable to not spend any money :D.
           
        ***Step zero only require 1 time only
        """)
        back = input('Back to home? (y/n) ')
        if back == 'y':
            audiyu()
        elif back == 'n':
            print("See you again!")
            time.sleep(1)
            quit()
        else:
            print('Please insert the right syntax!')
            quit()

    else:
        print('Please insert the right syntax!')
        quit()

audiyu()