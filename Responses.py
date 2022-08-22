from datetime import datetime
import Constants
from bs4 import BeautifulSoup
from googlesearch import search
import requests


def sample_responses(user_message):
    free_days = ["sunday", "monday", "thursday", "friday", "Saturday"]
    busy_days = ["tuesday", "wednesday"]
    list_input = user_message.split(" ")

    if user_message in ("hy", "hello", "hi"):
        return "hey, how's it going"

    elif user_message in ("who are you", "who are you?"):
        return "i am StudentAssistBot"

    elif user_message in free_days:
        return "its your free day!!"

    elif user_message in busy_days:
        if user_message == "tuesday":
            return "english at 17:00 - 20:00, no more ZOOM"

        elif user_message == "wednesday":
            return "english at 13:00 - 16:00, no more ZOOM"

    elif user_message in ("what is the date", "what is the date?", "time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y ,%H:%M:%S")
        return str(date_time)

    elif list_input[0] == "average:":
        return calc_average(list_input[1:])

    elif list_input[0] == "search:":
        return Search_online(" ".join(list_input[1:]))

    elif list_input[0] == "wiki:":
        birth = wiki_search(" ".join(list_input[1:]))
        if birth is None:
            return "I didn't find anything about " + " ".join(list_input[1:])
        return "born in: " + birth

    return "i did not understand you"


def calc_average(lst):
    temp_lst = lst
    new_lst = []
    my_sum = 0
    divide = 0

    if len(temp_lst) % 2 == 1:
        return "you entered grades not in the right format !!"

    for i in temp_lst:
        new_lst.append(float(i))

    for i in range(len(new_lst) // 2):
        my_sum += new_lst[i * 2] * new_lst[(i * 2) + 1]
        divide += new_lst[(i * 2) + 1]

    return "your average grade is: " + str(my_sum / divide)


def Search_online(my_str):
    lst = []
    what_to_search = my_str
    for j in search(what_to_search, tld='com', num=10, stop=10, pause=2, verify_ssl=False):
        lst.append(str(j))
    return str("\n\n".join(lst))


def to_upper(user_query):
    my_lst = user_query.split(" ")
    return " ".join(["".join([str(y).upper() if x == 0 else str(y) for x, y in enumerate(i)]) for i in my_lst])


def wiki_search(user_query):
    user_query_upper = to_upper(user_query)

    URL = "https://en.wikipedia.org/wiki/" + user_query_upper

    headers = Constants.headers

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = str(soup.find_all(text=""))
    my_lst = result.split(" ")
    for i, j in enumerate(my_lst):
        if 'births' in j.lower():
            if 'title="Category:' in my_lst[i + 1]:
                return my_split(my_lst[i + 1])


def my_split(my_str):
    new_res = []
    temp = False
    for i in my_str:
        if i == ':':
            temp = True
        elif temp:
            new_res.append(i)

    return "".join(new_res)
