import requests

class Questions_data:
    def __init__(self):
        pass

    def add_questions(self):
        response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
        question_data = response.json()

        try:
            question_data = question_data['results']
            return question_data
        except KeyError:
            print("error occured while fetching data")


