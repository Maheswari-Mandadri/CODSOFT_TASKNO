def get_response(user_input):
    user_input=user_input.lower().strip()
    if user_input in ["hello","hi","hey"]:
        return ("Bot:Hello! How can I help you?")
    elif "how are you?" in user_input:
        return("Bot:I'm doing great! Thanks for Asking")
    elif "what's your name" in user_input:
        return("Bot: I am a Rule-Based AI ChatBot")    
    elif "what is Ai?" in user_input:
        return ("Bot:AI stands for Artificial Intelligence.It enables machines to perform tasks that normally require human intelligence")
    else:
        return "Sorry,I dont understand that.please try another question"    