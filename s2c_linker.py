import os, json

class s2c_mission():
    def __init__(self):
        self.missionid=""
        self.scenes={}
        self.populate()

    def populate(self):
        for i in range(5):
            scene = s2c_scenes(i)
            scene.populate()
            self.scenes[i] = scene

    def print_mission(self):
        print("Mission ID: "+self.missionid)
        for i in self.scenes:
            self.scenes[i].print_scenes()


class s2c_scenes():
    def __init__(self,sceneid):
        self.sceneid=sceneid
        self.scenebenumber=""
        self.files={}

    def populate(self):
        for i in range(4):
            file = s2c_file(i)
            self.files[i] = file
            
    def print_scenes(self):
        print("Scene ID: ")
        print(self.sceneid)
        for i in self.files:
            self.files[i].print_file()

class s2c_file():

    def __init__(self,idx):
        self.idx=idx

    def print_file(self):
        print("File Index:")
        print(self.idx)

class s2c_linker():

    def __init__(self):
        self.config = None 
        self.read_configuration("./config.json")
        self.mission = s2c_mission()

    def read_configuration(self,config_file):
        if os.path.isfile(config_file) and os.access(config_file, os.R_OK):
            with open(config_file, "r") as jsonfile:
                self.config = json.load(jsonfile)
            jsonfile.close()

    def show_configuration(self):
        print(self.config["sleep"])
        self.mission.print_mission()

if __name__ == "__main__":
    S2C = s2c_linker()
    S2C.show_configuration()