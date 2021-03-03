        ___             ___            
       /   | __  ______/ (_)_  ____  __
      / /| |/ / / / __  / / / / / / / /
     / ___ / /_/ / /_/ / / /_/ / /_/ / 
    /_/  |_\__,_/\__,_/_/\__, /\__,_/  
                        /____/
> Evil Deimos | 3/3/2021

# Table Of Content

- [Overview](#overview)
- [Installation](#installation)
- [Basic Usage](#basic-usage)
- [About Project](#about-project)

# Overview

###  **I. Decrypt and remove PDF's password**

​	Basically this feature is going to remove your pdf's password forever. So you won't need to insert the password over and over again. This feature meant to make your day easier, writer not responsible about the misleading of Audiyu's usage.

### **II. PDF to Mp3 converter**

​	This feature has ability to convert PDF into a Mp3, so you can get a audiobook version of your pdf for free. Currently the supported languange is english. Later on, we will provide more languange. The speech machine is using a google translate's library (gTTS or google text to speech). As you know that gTTS will convert text to speech, so first thing before convert it is to extract each word in the pdf file. 

### **III. Music Player**

To be honest this third feature is only a just for fun project because it's so simple to code and we believe that users will use another music player.

# Installation

1. Make sure you already have python installed in your machine
2. `pip install -r requirements.txt`
3. `python audiyu.py`

# [Basic Usage](#basic-usage)

###  **I. Decrypt and remove PDF's password**

1. Start the program, `python audiyu.py`
2. Choose number 1 and press enter
3. Insert the file name complete with the extension (.pdf), make sure it's a pdf file and in the same folder with Audiyu
4. Enter the password, it will show you the total page and check your folder,
      there will be a new pdf file with the same pdf's name but has a 'dec' name
5. You can rename it later.

### **II. PDF to Mp3 converter**

1. Start the program, `python audiyu.py`

2. Choose number 2 and press enter
3. Insert the file name complete with the extension (.pdf), make sure it's a pdf file and in the same folder with Audiyu. MAKE SURE IT'S NOT ENCRYPTED
4. Insert the starting point of the PDF. 
5. You'll need to choose custom endpoint or the rest of the page. If you want custom endpoint press 1 and press enter, if you want the rest of the book than press 2 and enter. If you choose to, skip to step 7.
6. Insert the custom endpoint. Make sure it's a number
7. Insert the name of the Mp3 File, no need to type the .mp3 extension
8. Please wait patiently until the program is done.

### **III. Music Player**

1. Start the program, `python audiyu.py`

2. Choose number 3 and press enter
3. Insert the .mp3 file. Make sure you write the .mp3 extension
4. The audio file will automatically played
5. press 'p' and enter to pause, press 'r' and enter to resume, and press 
    'e' and enter to exit



# About Project