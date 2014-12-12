PickAx Password Finder
======================

A PAX file is an encrypted image format, where Blowfish is used as the encryption algorithm. The tool, called Pick Ax, was developed by Smaller Animals, but it's not accessible anymore from the original website (http://www.smalleranimals.com/pickaxe.htm), but you can find it here:
http://windows.softwareweb.com/download-file/100581616/freeware/pick-ax-1.0/

The image header signature is:
"PAX" (0x50 0x41 0x58) in the first 3 bytes.

I made a script, which can simply try passwords from a wordlist (or you can specify a single one) against a given image. It requires _ISource50.dll, which contains a function to check for the password, it's downloadable from Smaller Animal's website:
http://www.smalleranimals.com/isource.htm
http://www.smalleranimals.com/zips/ImgSource5/isource50.zip

Usage
=====

```
pickaxpwfinder.py [options]

Options:
  -h, --help            show this help message and exit
  -p PASSWORD, --password=PASSWORD
                        Password to try
  -d DICTIONARY, --dictionary=DICTIONARY
                        Specify dictionary (wordlist)
  -f FILE, --file=FILE  Chose PAX file to crack
```

I also made an encrypted image to play with (can be found under samples), the password is "password".