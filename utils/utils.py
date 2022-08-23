from PIL import Image

class ImgToAscii:

    # Takes image name
    def __init__(self, img_name, width):
        self.img_name = img_name 
        # ASCII chars. You can change this if you want. first index is black, last index is white.
        self.ascii_chars = ['#', '#', '%', '%', '$', '$', '^','^', '-', ',', '.']
        # Base width for resizing
        self.base_width = width


    # Resizes Image and converts to grayscale
    def convert(self, img): 
        self.aspect_ratio = self.base_width / img.size[0]
        self.height = self.aspect_ratio * img.size[1]
        self.img = img.resize((int(self.base_width), int(self.height)))
        print(f"\nContinuing with size {self.base_width}x{int(self.height)}\n")
        return self.img.convert(mode="L")

    # Converts image to ASCII and saves it on a txt file.
    def process_img(self):
        try:
            # Opens image and converts to RGBA so images without background would work.
            with Image.open(f"./images/{self.img_name}").convert("RGBA") as image:
                self.im = self.convert(image)
                self.pixl = self.im.getdata()

            self.newpix = [self.ascii_chars[pix//25] for pix in self.pixl]

            self.text = ''
            self.count = 0

            for i in self.newpix:
                self.text += i
                self.count += 1
                if self.count == self.base_width:
                    self.text += '\n'
                    self.count = 0
            
            with open('converted.txt', 'w') as self.txt:
                self.txt.write(self.text)
                print("\033[0;92m" + 'Done! ASCII characters in converted.txt file.' + "\033[0;37m")
        
        except FileNotFoundError:
            print("\033[0;31m" + "Image not found. Make sure it's in images folder and you typed the name correctly with the file extension" + "\033[0;37m")