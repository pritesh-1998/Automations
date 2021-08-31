import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".question-summary")
print(type(questions))

# everything is stored in a form of dictionary so to access it we need to use...
# print(questions[0].attrs)
# print(questions[0].get("id",0))
# print(questions[0].select(".question-hyperlink"))
#it will search for single element
#print(questions[0].select_one(".question-hyperlink").get_text())
#iterating to get all the questions from awebsite:-
count=1
for question in questions:
    print(count," ",question.select_one(".question-hyperlink").get_text())
    print("Votes = ",question.select_one(".vote-count-post").get_text())
    count=count+1