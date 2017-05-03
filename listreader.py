class ListReader:
    lines = []

    def __init__(self):
        filepath = "wildmagictext.txt"
        file = open(filepath)
        text = file.read()
        self.lines = text.splitlines()

    def getlist(self):
        return self.lines
