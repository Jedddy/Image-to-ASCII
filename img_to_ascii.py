import os
from utils.utils import ImgToAscii

def main():
    print("""
    Made By: 
    .____.          ._.
    |    | ____   __| |
    |    |/ __ \ / __ | 
/\__|    \  ___// /_/ | 
\________|\_____>_____| 
              
        """)


    print("Image will get resized and then converted to ASCII.\n")
    print("Make sure image is in images folder.\n")
    # Takes image name from user input
    inp = input("Input Image Filename with extension: ")
    try:
        img_size = int(input("\nSize you want (ex. 50). Press Enter if you want default width.\n\nDefault is 50\n\nWidth size: "))
    except ValueError:
        img_size = 50
        print("\nWill now continue with default width. (50)\n")

    prcsr = ImgToAscii(inp, width=img_size)
    prcsr.process_img()
    

if __name__ == '__main__':
    try:
        os.mkdir('images')
    except FileExistsError:
        pass

    while True:
        main()
        inp = input('\nRestart? [y/n]: ')
        os.system('cls' if os.name == 'nt' else 'clear')
        if inp.lower() == 'n':
            break
        elif inp.lower() == 'y':
            continue
        else:
            print('Invalid response. Quitting Program.')
            break