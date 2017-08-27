import  urllib
# 1) Read text
# 2) Check text

def read_text():
    quotes = open("E:\Python\PycharmProjects\Python_Learner\movie_quotes.txt.txt")
    content = quotes.read()
    print(content)
    quotes.close()
    check_profanity(content)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("No Curse Words!")
    else:
        print("Unable to scan!")

read_text()
