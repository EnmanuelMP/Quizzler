import os
import json
import requests
from dotenv import find_dotenv, load_dotenv


def generate_questions():
    dotenv_file:str = find_dotenv()
    load_dotenv(dotenv_file)
    URL:str = os.getenv("URL")
    PARAMETERS:dict = json.loads(os.getenv("PARAMETERS"))

    response = requests.get(URL, params=PARAMETERS).json()
    question_data = response["results"]
    return question_data

if __name__ == '__main__':
    print(generate_questions())