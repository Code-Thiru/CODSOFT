import datetime
import random

def rule_based_chatbot():
    print("Chatbot: Hello! I’m a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there! How can I help you today?")
        
        elif "how are you" in user_input:
            print("Chatbot: I’m just a bunch of code, but I’m doing great! What about you?")
        
        elif "your name" in user_input:
            print("Chatbot: I'm ChatBot, your friendly chatbot!")
        
        elif "help" in user_input:
            print("Chatbot: You can ask me simple questions like 'time', 'joke', 'how are you', or say 'bye' to exit.")
        
        elif "time" in user_input:
            now = datetime.datetime.now().strftime("%H:%M")
            print(f"Chatbot: The current time is {now}.")
        
        elif "date" in user_input:
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            print(f"Chatbot: Today’s date is {today}.")
        
        elif "joke" in user_input:
            jokes = [
                "Why don’t scientists trust atoms? Because they make up everything!",
                "Why did the computer go to the doctor? It had a virus!",
                "What do you call a bear with no teeth? A gummy bear!"
            ]
            print(f"Chatbot: {random.choice(jokes)}")
        
        elif "thank" in user_input:
            print("Chatbot: You're welcome! Happy to help.")
        
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a nice day.")
            break
        
        else:
            print("Chatbot: I'm not sure how to respond to that. Try asking for 'help'.")
            


rule_based_chatbot()
