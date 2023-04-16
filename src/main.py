from PIL import Image
import os
import sys
import messages


##############################################################################################################
##############################################################################################################

def check_paths(src, dst, srcfrmt, destfrmt):
    if src[-1] != "/":
        src = src+"/"
    if dst[-1] != "/":
        dst = dst+"/"

    if not os.path.exists(src):
       print("The Source Path you've entered does not Exist.")
       exit()

    is_abs = os.path.exists(dst)
    #print(os.path.exists(dst))

    if not os.path.exists(dst):
       if not is_abs:
          print("The Destination Path you've entered does not Exist. Hence, Creating it...")
          os.mkdir(dst)
          dst = f"{os.getcwd()}/{dst}"
          print(f"The Converted Images will be Stored in -> {dst}")
    else:
       # The Path Provided Exists
       dst = dst
       srcfrmt = srcfrmt.lower()
       destfrmt = destfrmt.lower()

    return src, dst, srcfrmt, destfrmt


##############################################################################################################
##############################################################################################################

def convert_images(source, destination, init_file_format, final_file_format):
   for file in os.scandir(source):
      if file.name.endswith(f'.{init_file_format}'):
         img_name= file.name
         img = Image.open(f"{source}{img_name}")
         print(f"Converting -> {img_name}")
         clean_name = os.path.splitext(img_name)
         img.save(f"{destination}{clean_name[0]}.{final_file_format}", f"{final_file_format}")
   print("Done !")
   return 0


##############################################################################################################
##############################################################################################################


def main():
   if len(sys.argv) == 1:
        messages.print_help()
        sys.exit(0)
   elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
        messages.help_message()
        sys.exit(0)

   if len(sys.argv) >= 3:
    try:
        source, destination, init_file_format, final_file_format = check_paths(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        print(f"-------------------------------------------------------------\nSource: {source}\nDestination: {destination}\nInitial File Format: {init_file_format}\nFinal File Format: {final_file_format}-------------------------------------------------------------\n\n")

        convert_images(source, destination, init_file_format, final_file_format)
        messages.print_thanks()

    except:
        messages.print_help()    

   else:
     messages.print_help()


##############################################################################################################
##############################################################################################################


if __name__ == "__main__":
   main()
