import os, json

class s2c_linker():

    def __init__(self):
        self.config = None 
        self.read_configuration("./config.json")

    def read_configuration(self,config_file):
        if os.path.isfile(config_file) and os.access(config_file, os.R_OK):
            with open(config_file, "r") as jsonfile:
                self.config = json.load(jsonfile)
            jsonfile.close()

    def show_configuration(self):
        print(self.config["sleep"])

if __name__ == "__main__":
    S2C = s2c_linker()
    S2C.show_configuration()