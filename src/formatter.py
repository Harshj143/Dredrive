import subprocess


class formatter():
    def rewrite_script(self, i, name):
        print("Entered script")
        if i == 1:
            with open("src/diskpart_script.txt",'w') as file:
                file.write('select disk 2\n')
                file.write('clean\n')
                file.write('convert mbr\n')
                file.write('create partition primary\n')
                file.write('format quick fs=NTFS label='+name+'\n')
                file.write('assign letter=E')
        else:
            with open("src/diskpart_script.txt",'w') as file:
                file.write('select disk 2\n')
                file.write('clean\n')
                file.write('convert gpt\n')
                file.write('create partition primary\n')
                file.write('format quick fs=FAT32 label='+name+'\n')
                file.write('assign letter=E')
        print("Completed writing to script")

        self.format_usb()

    def format_usb(self):
        print("Process to format USB started . . .")
        subprocess.run(["diskpart", "/s", "src/diskpart_script.txt"])
