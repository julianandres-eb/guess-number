class Question:
    title = ""
    answers = []
    key = ""
    reiterable = ""

    def __init__(self, title, answers, key, reiterable):
        self.title = title
        self.answers = answers
        self.key = key
        self.reiterable = reiterable

    def addAnswer(self, answer):
        self.answers.append(answer)

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def setAnswers(self, answers):
        self.answers = answers

    def getAnswers(self):
        return self.answers

    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key

    def getReiterable(self):
        return self.reiterable

    def setReiterable(self, reiterable):
        self.reiterable = reiterable