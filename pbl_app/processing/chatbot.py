#This file is used to create a chatbot for the app made is main.py file, it receives a user input, write suitable reply and returns it back. 

import json

LEARN = False
Q = None

def load_knowledge(filename):
    try:
        with open(filename, "r") as file:
            data = file.read()
            if not data:
                return {}
            return json.loads(data)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_knowledge(filename, knowledge):
    with open(filename, "w") as file:
        json.dump(knowledge, file, indent=4)

def ask_chatbot(prompt):
    global LEARN
    global Q
    knowledge_file = "pbl_app\\knowledge.json"
    knowledge = load_knowledge(knowledge_file)
    
    user_input = prompt.strip().lower()
    if user_input == "":
        reply = "You didn't enter anything!"
    elif user_input in knowledge and Q == None:
        reply = knowledge[user_input]
    elif LEARN == False and user_input not in knowledge:
        reply =  "I'm not sure how to respond to that. Please teach me the answer of it\n Type idk if you dont know."
        LEARN = True
        if prompt != "wo bu zhi dao":
            Q = prompt
    elif prompt.lower() == "wo bu zhi dao" and LEARN == True:
        knowledge[Q] = "I'm not sure about the answer, will be updated soon."
        save_knowledge(knowledge_file, knowledge)
        reply = "Thanks for letting me know using the secret command!"
        LEARN = False
        Q = None      
    elif prompt.lower() not in ["idk", "i dont know", "im not sure", "im not sure about the answer", "i dont know the answer"] and LEARN == True:
        knowledge[Q] = prompt
        reply = "Thanks for letting me know!"
        save_knowledge(knowledge_file, knowledge)
        LEARN = False
        Q = None
    else:
        reply = "Thanks for telling me!"
        LEARN = False
        Q = None

    return reply


