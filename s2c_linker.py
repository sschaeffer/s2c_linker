import os, json, pickle

class s2c_mission():
    def __init__(self, missionid):
        self.missionid=missionid
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
        print("Scene ID: %d" % self.sceneid)
        for i in self.files:
            self.files[i].print_file()

class s2c_file():

    def __init__(self,idx):
        self.idx=idx

    def print_file(self):
        print("File Index: %d" % self.idx)

class s2c_linker():

    def __init__(self):
        self.config = None 

    def read_configuration(self,config_file):
        self.mission = s2c_mission("SPS2K52")
        if os.path.isfile(config_file) and os.access(config_file, os.R_OK):
            with open(config_file, "r") as jsonfile:
                self.config = json.load(jsonfile)
            jsonfile.close()

    def show_configuration(self):
        if self.config == None:
            print("Sleep configuration not found")
        else:
            print("Sleep configuration: %d" % self.config["sleep"])
        self.mission.print_mission()

    def save_state(self):
        fileObj = open('./data.obj', 'wb')
        pickle.dump(self.mission,fileObj)
        fileObj.close()

    def load_state(self):
        fileObj = open('./data.obj', 'rb')
        self.mission = pickle.load(fileObj)
        fileObj.close()

if __name__ == "__main__":
    S2C = s2c_linker()
#    S2C.read_configuration()
#    S2C.show_configuration()
#    S2C.save_state()

    S2C.load_state()
    S2C.show_configuration()

    