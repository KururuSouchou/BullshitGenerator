def read_json(fileName=""):
    import json
    if fileName != '':
        strList = fileName.split(".")
        if strList[len(strList)-1].lower() == "json":
            with open(fileName, mode='r', encoding="utf-8") as file:
                return json.loads(file.read())
