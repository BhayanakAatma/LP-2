# Simple Customer Interaction Chatbot



def greet():

    print("Chatbot: Welcome! How can I assist you today?")





def farewell():

    print("Chatbot: Thank you for chatting with us. Have a great day!")





def process_input(user_input):

    if "order" in user_input:

        print("Chatbot: Sure! Please provide your order details.")

        # Process order details

        print("Chatbot: Your order has been placed successfully.")

    elif "shipping" in user_input:

        print("Chatbot: Our standard shipping time is 3-5 business days.")

    elif "payment" in user_input:

        print("Chatbot: We accept all major credit cards and PayPal.")

    elif "return" in user_input:

        print("Chatbot: Please refer to our return policy on our website.")

    elif "bye" in user_input:

        farewell()

        return False

    else:

        print("Chatbot: I'm sorry, I didn't understand. Can you please rephrase?")



    return True





def start_chat():

    greet()

    chatting = True

    while chatting:

        user_input = input("User: ")

        chatting = process_input(user_input)





# Start the chatbot

start_chat()