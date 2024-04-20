#This file is used to create a chatbot for the app made is main.py file, it receives a user input, write suitable reply and returns it back. 

def ask_chatbot(question):
    """
    This function is used to receive user input from the chatbot.
    prompt is the query that the user have typed in
    reply is the answer written by the bot
    """
    real_question = spell_check(question)
    reply = question_answers(real_question)    

    return reply

def question_answers(question):
    """
    This function contains all the possible question that will be asked by the users, and suitable reply for all of them.
    Also uses AI for spelling mistake checking
    """
    
    question_set = {}
    question_set["what is your name"] = "My name is CRat, I am the chatbot of this app."
    question_set["how old are you"] = "I am a chat bot, I dont really have age"
    question_set["where do you live"] = "I suppose I live on the internet"
    question_set["where can i find hostels"] = "You can find hostels many places like Akurdi, Pimpri, Lonavala, Shivaji Nagar,Talegaon, Kanpur, Pune, Vashi, Nerul, Sanpada, Juinagar, Kalyan, Ulwe, Seawoods"
    question_set["hi"] = "Hello, how can I help you?"
    question_set["how are you"] = "I'm fine, thanks for asking!"
    question_set["how are you doing"] = "I'm doing great, thanks for asking!"
    question_set["are you planning to stay here"] = "Yes, I am planning to stay here, thanks for asking!"
    question_set["hello"] = "Hi, how can I help you?"
    question_set["what is your purpose"] = "I am here to help you answer some of your doubts."
    question_set["ask me a question"] = "Suggest few questions and suitable replies for me to learn"
    question_set[""] = "You didnt enter anything!"
    question_set["give me money"] = "Nope. Go get a job!"
    question_set["yo"] = "Wassup?"

    if question in question_set:
        answer = question_set[question]
    else:
        answer = "Sorry, I don't know the answer for this question."

    return answer

def spell_check(question):
    """
    This function check for spelling mistakes and return the question with correct spelling
    """

    correct_spelling = question.lower()

    return correct_spelling