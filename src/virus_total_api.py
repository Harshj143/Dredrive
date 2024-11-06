# virus total malware scanning script
import requests
import time
import json
from os import listdir
from os.path import isfile, join, normpath
import hashlib
import re


class scanp2():
    # enter your private key here from virus total
    key = 'd93b0f6a1af0866169bc2e123813bfb62be34462305d5f6f6e2a1738e07023aa'
    def get_files(self):
        current_path = normpath("temp\\temp")
        return [join(current_path, f) for f in listdir(current_path) if isfile(join(current_path, f))]

    def get_hashes(self):
        files = self.get_files()
        list_of_hashes = []
        for each_file in files:
            hash_sha256 = hashlib.sha256()
            with open(each_file, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_sha256.update(chunk)
            list_of_hashes.append('${}$\n'.format(hash_sha256.hexdigest()))
        return list_of_hashes

    def write_hashes(self):
        hashes = self.get_hashes()
        with open('hash_list.txt', 'w') as f:
            for sha256_hash in hashes:
                f.write(sha256_hash)
        self.send_hashes()

    def send_hashes(self):
        file = open("hash_list.txt", 'r')
        hashlist = re.findall(r'\$(.*)\$', file.read())
        file.close()
        print(hashlist)
        for hash in hashlist:
            self.VT_Request(hash)
            time.sleep(40)

    # Scanning files against Virus Total API
    def VT_Request(self, hash):
        params = {'apikey': self.key, 'resource': hash}
        url = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params)
        json_response = url.json()
        x = str(json_response)
        x = x.replace("'", '"')
        x = x.replace("False", '"False"')
        x = x.replace("True", '"True"')
        x = x.replace("None", '"None"')

        parsed = json.loads(x)
        y = json.dumps(parsed, indent=4, sort_keys=True)

        print("\n")
        response = int(json_response.get('response_code'))
        if response == 0:
            print(y + "\n\n" + hash + ' is not in Virus Total')
        elif response == 1:
            positives = int(json_response.get('positives'))
            total = int(json_response.get('total'))
            permalink = str(json_response.get('permalink'))
            if positives == 0:
                print(y + "\n\n" + hash + ' is not malicious')

            else:
                file = open("scanlog.txt", 'a')
                file.write("\nHash: {" + hash + "}")
                print(y + "\n" + hash + ' is malicious')
                file.write("\nFlagged by: " + str(positives)+"/"+str(total))
                print('Found malicious in ' + str(positives) + ' of total ' + str(total) + ' results')
                file.write("\nReport Link: <a href=\"" + str(permalink) + "\"> Link </a>\n")
                file.write("\n*************************\n")
                print('Link: '+ permalink)
                file.close()
        else:
            print(y + "\n\n" + hash + ' could not be searched. Please try again later.')


# running the program
if __name__ == '__main__':
    obj = scanp2()
    obj.write_hashes()