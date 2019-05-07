import csv
import random
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

def askForResponses(allQuestions, answers):

    digitsCorrect = False
    positionCorrect = False
    biggerCorrect = False
    lowerCorrect = False

    while digitsCorrect is False:
        digits = int(input(allQuestions[0].getTitle() + "?: "))
        if digits > 0:
            answers.append(digits)
            digitsCorrect = True

    while positionCorrect is False:
        position = random.randint(1, answers[0])
        number = int(input(allQuestions[1].getTitle() + " " + str(position) + "?: "))
        if number > 0:
            answers.append(position)
            answers.append(number)
            positionCorrect = True

    while biggerCorrect is False:
        number = random.randint(pow(10, answers[0] - 1), pow(10, answers[0]) - 1)
        response = input(allQuestions[2].getTitle() + " " + str(number) + " (y/n)?: ")

        if response is "y" or response is "n":

            if response is "y":
                answers.append(number)
                answers.append(1)
            else:
                answers.append(number)
                answers.append(0)

            biggerCorrect = True

    while lowerCorrect is False:
        number = random.randint(pow(10, answers[0] - 1), pow(10, answers[0]) - 1)
        response = input(allQuestions[3].getTitle() + " " + str(number) + " (y/n)?: ")

        if response is "y" or response is "n":

            if response is "y":
                answers.append(number)
                answers.append(1)
            else:
                answers.append(number)
                answers.append(0)

            lowerCorrect = True


class Questionaire:
    questions = []
    answers = []

    def __init__(self):
        self.initQuestionaire()

    def initQuestionaire(self):

        if len(self.questions) is 0:
            self.questions = createQuestions()

        # Ask the user for responses
        askForResponses(self.questions, self.answers)
        print(self.answers)
        return self.answers
