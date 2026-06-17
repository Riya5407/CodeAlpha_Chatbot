def chatbot_response():
    print("========= Welcome to the Chatbot! =========")

    while True:
        user = input("You: ").strip().lower()

        if user == "hello":
            print("Chatbot: Hi!\n")

        elif user == "how are you":
            print("Chatbot: I'm fine, thanks!\n")

        elif user == "what's your name":
            print("Chatbot: My name is CodeAlpha Chatbot.\n")

        elif user == "thank you":
            print("Chatbot: You're welcome!\n")

        elif user == "bye":
            print("Chatbot: Goodbye!\n")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.\n")

chatbot_response()