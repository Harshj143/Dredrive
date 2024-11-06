import subprocess

class scanp1():
    # Method to start Clam AV and transfer virus files to .\tmp\tmp directory
    def csav_run(self, pathtof):

        # Clear tmp
        rmdir = subprocess.Popen('rmdir /s temp\\temp', stdin=subprocess.PIPE, shell=True)
        rmdir.stdin.write(b"y\n")
        rmdir.stdin.flush()
        stdout, stderr = rmdir.communicate()
        self.printLine(stdout)
        mkdir = subprocess.Popen('mkdir temp\\temp', shell=True, stdout=subprocess.PIPE)
        self.printLine(mkdir.communicate())

        # Make command to be passed into subprocess
        cmd = 'clam\clamav\clamscan.exe --recursive --move=temp\\temp '
        cmd = cmd + pathtof
        print(cmd)
        scanpro = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        out = scanpro.communicate()

        print(type(out))
        print(out)
        #self.printLine(scanpro.communicate().decode("utf-8"))

    # Print output to command line method
    def printLine(self, err):
        print(err)


if __name__ == "__main__":
    obj = scanp1()
    obj.csav_run("E:")
