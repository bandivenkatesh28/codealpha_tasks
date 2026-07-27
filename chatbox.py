def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("🤖 Chatbot: Hi!")

        elif user == "how are you":
            print("🤖 Chatbot: I'm fine, what about you")
            
        elif user == "fine":
            print("🤖 Chatbot:  That's great..")
            
 
        elif user == "what is your name":
            print("🤖 Chatbot: My name is Robot")

        elif user == "who created you":
            print("🤖 Chatbot: I was created using Python.")

        elif user == "bye":
            print("🤖 Chatbot: Goodbye!")
            break

        else:
            print("🤖 Chatbot: Sorry, I don't understand that.")

chatbot()