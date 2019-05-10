import csv

filename = "/home/jagadru/PycharmProjects/eventbrite/bin/thinker/core/questions/listQuestions.csv"

class question:
    title = ""
    response = ""

    def __init__(self, title, response):
        self.setTitle(title)
        self.setResponse(response)

    def setTitle(self, title):
        self.title = title

    def setResponse(self, response):
        self.response = response

    def getTitle(self):
        return self.title

    def getResponse(self):
        return self.response

    def createQuestions():
        # Create Questions from File

        # - Read file and generate a list
        file = open(filename, 'r')
        reader = csv.reader(file)
        allQuestions = [row for row in reader]

        questionsToReturn = []

        # - Fullfill question objects with title
        for q in allQuestions:
            questionsToReturn.append(question(q[0], ""))

        return questionsToReturn
