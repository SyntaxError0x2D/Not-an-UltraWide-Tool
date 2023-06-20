import os

#checks if the file is there function
def isFile() -> bool:
    if "nuwt-settings.ini" not in os.listdir(): return(False)
    return(True)

#read function
def readSettings() -> dict:
    with open("nuwt-settings.ini") as file:
        line_ = file.readline()
        settings: dict = {"res" : None, "move_to" : None, "scaling" : None} 
        while line_:

            if line_[0] == "#" or line_ == "\n": pass

            else:
                line_ = line_.replace("\n", "").replace(" ", "")
                if (prefix := line_.split("=")[0]) in settings:
                    conents = line_.split("=")[1]

                    if prefix in ["res", "move_to"]:
                        conents = [int(r) for r in conents.split(",")]
                    elif prefix == "scaling":
                        if "%" in conents:
                            conents = int(conents[:-1]) / 100
                        else: conents = float(conents)
                    
                    settings[prefix] = conents

            line_ = file.readline()
        
        return(settings)
    
def warn_noFile():
    with open("Eror.log", "w+") as file:
        file.write("File was not found.")
