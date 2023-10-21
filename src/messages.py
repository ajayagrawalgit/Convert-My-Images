import getpass

help_msg=f'''

██╗░░░██╗██╗░░██╗  ░█████╗░██╗░░██╗  ██╗
██║░░░██║██║░░██║  ██╔══██╗██║░░██║  ██║
██║░░░██║███████║  ██║░░██║███████║  ██║
██║░░░██║██╔══██║  ██║░░██║██╔══██║  ╚═╝
╚██████╔╝██║░░██║  ╚█████╔╝██║░░██║  ██╗
░╚═════╝░╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝  ╚═╝

You're running the tool in a wrong way, {getpass.getuser()} !
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Here's how you should try running the tool:
convertmyimages <source_path> <destination_path> <initial_format> <final_format>


'''

thanks_msg=f'''
-----------------------------------------------------------------------------------------
███████████████████████████████████████████████████████████████████████████████████████▀█
█─▄─▄─█─█─██▀▄─██▄─▀█▄─▄█▄─█─▄█─▄▄▄▄███▄─▄▄─█─▄▄─█▄─▄▄▀███▄─██─▄█─▄▄▄▄█▄─▄█▄─▀█▄─▄█─▄▄▄▄█
███─███─▄─██─▀─███─█▄▀─███─▄▀██▄▄▄▄─████─▄███─██─██─▄─▄████─██─██▄▄▄▄─██─███─█▄▀─██─██▄─█
▀▀▄▄▄▀▀▄▀▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▀▄▄▄▀▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀
-----------------------------------------------------------------------------------------
This has been a great ride {getpass.getuser()} :) Have a good one, buddy !   C i a o   !
-----------------------------------------------------------------------------------------

'''

help_msg_first=f'''

██████████████████████████████████████████████████████████████████████████████████████████████▀█████████████
█─▄▄▄─█─▄▄─█▄─▀█▄─▄█▄─█─▄█▄─▄▄─█▄─▄▄▀█─▄─▄─█▀▀▀▀▀██▄─▀█▀─▄█▄─█─▄█▀▀▀▀▀██▄─▄█▄─▀█▀─▄██▀▄─██─▄▄▄▄█▄─▄▄─█─▄▄▄▄█
█─███▀█─██─██─█▄▀─███▄▀▄███─▄█▀██─▄─▄███─███████████─█▄█─███▄─▄██████████─███─█▄█─███─▀─██─██▄─██─▄█▀█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▀▀▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▀▀▀▀▀▀▀▄▄▄▀▄▄▄▀▀▄▄▄▀▀▀▀▀▀▀▀▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀

Hello {getpass.getuser()},

Luckily there's nothing much to learn for using this tool. You just need one command to be able to use it.
Follow the syntax below and you'll be sorted 🤗

Syntax:
convertmyimages <source_path> <destination_path> <initial_format> <final_format>

Example:
1. convertmyimages /Users/ajay.agrawal/Downloads /Users/ajay.agrawal/Documents jpg png
2. convertmyimages /Users/ajay.agrawal/Downloads ConvertedImages png gif

Example No. 1 is pretty self-explanatory. It will convert all the Images of the extension '.jpg' stored in /Users/ajay.agrawal/Downloads and save the converted Images to /Users/ajay.agrawal/Documents
Example No. 2 is a little different. Here you can see that, The destination path is just a Name. Which may or may not be there on your present working directory. If it is present there, Offcourse the script will choose that as a destination path and even if it is not, the tool will create a directory of the name 'ConvertedImages' and save the Converted Images of /Users/ajay.agrawal/Downloads to ConvertedImages.

Don't worry ! Whatever is the case. Once you run the tool. You don't have to search for the location where the tool is saving the files as it'll provide you the path what it chooses to save the files.

I hope this tool serves exactly what you needed.

-----------------------------------------------------

Read the Complete Document on: https://github.com/ajayagrawalgit/Convert-My-Images
Support Me On: https://www.buymeacoffee.com/ajayagrawal
Cheers 🥂
'''


def print_help():
    print(help_msg)

def print_thanks():
    print(thanks_msg)

def help_message():
    print(help_msg_first)
