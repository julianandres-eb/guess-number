import csv, os, json

class question:
    title = ""

    def __init__(self, title):
        self.setTitle(title)

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def createQuestions():
        #with open(os.getcwd() + "/thinker/core/questions/listQuestions.csv", 'r') as JSON:
        #    dict = json.load(JSON)

        # Now you can use it like dictionary
        # For example:

        #print(dict["username"])



        # Create Questions from File
        # - Read file and generate a list
        file = open(os.getcwd() + "/thinker/core/questions/listQuestions.csv", 'r')
        reader = csv.reader(file)
        print(reader[0])
        allQuestions = [row for row in reader]

        questionsToReturn = []

        # - Fullfill question objects with title
        for q in allQuestions:
            questionsToReturn.append(question(q[0], ""))

        return questionsToReturn
