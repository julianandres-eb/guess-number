import csv

class question:
    title = ""
    response = ""

filename = "bin/thinker/core/questions/listQuestions.csv"

def initQuestions():

    file = open(filename, 'r')
    reader = csv.reader(file)
    allQuestions = [row for row in reader]
    print(allQuestions)
    # Create Questions from File

    # - Read file and generate a list
    # - Fullfill question objects with title

    # Ask the user for responses

    # Verify the answers

    # Create a dictionary with questions and answers and then return



    print("Algo")
    return 0