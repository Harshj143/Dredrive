import subprocess

class hosting():
    #Defining IP address and ports
    ip = '192.168.1.40'
    port = '4747'
    flag = False
    #Method called to host files
    def hostFiles(self):
        cmd = 'python -u -m http.server ' + self.port + ' -b ' + self.ip + ' 2> logs.txt'
        print("Command: " + cmd)
        sp = subprocess.Popen(cmd, cwd='E:', shell=True, stdout=subprocess.PIPE)
        global i
        i = sp.pid
        print("Process ID: " + str(i))
        print(sp.communicate())


    #these methods can be called to set ip and port variables
    def setip(self, str):
        self.ip = str

    def setport(self, str):
        self.port = str

    #Terminate method to kill entire process on EXIT
    def stopHost(self):
        cmd = 'taskkill /f /pid ' + str(i)
        print("stopHost executed 1")
        subprocess.Popen(cmd, shell=True)
        print("stopHost executed 2")
        #os.killpg(os.getpgid(self.i), signal.SIGTERM)


if __name__ == "__main__":
    obj = hosting()
    obj.hostFiles()

#python -m http.server 4747 -b 192.168.1.41