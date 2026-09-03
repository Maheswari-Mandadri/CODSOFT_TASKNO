def get_response(user_input):
    user_input=user_input.lower()
    if user_input in ["hello","hi","hey"]:
        return ("Bot:Hello! How can I help you?")
    elif "how are you?" in user_input:
        return("Bot:I'm doing great! Thanks for Asking")
    elif user_input=="what's your name" :
        return("Bot: I am a Rule-Based AI ChatBot")    
    elif user_input=="what is ai?":
        return ("Bot:AI stands for Artificial Intelligence.It enables machines to perform tasks that normally require human intelligence")
    elif user_input=="what is python?":
        return "python is a popular programming language"
    elif user_input=="who are you?":
        return "I am a simple chatbot"
    elif user_input=="bye":
        return "Goodbye! Have a nice day"
    elif user_input=="who created python":
        return "python was created by Guido van Rosum"
    elif user_input=="thank you":
        return "you're welcome!"
    else:
        return "Sorry,I dont understand that.please try another question"
print("chatbot:Hello I am a simple chatbot.")
while True:
    user_input=input("you:")
    if user_input.lower()=="bye":
        print("chatbot:",get(user_input))
        break
    print("chatbot:",get_response(user_input))        
