import random

def load_data(file_path):
    intents = {}
    responses = {}

    with open(file_path, 'r') as f:
        for line in f:
            intent_name, keywords_and_responses = line.strip().split('|')
            keywords, responses_list = keywords_and_responses.split(':')
            intents[intent_name] = keywords.split(',')
            responses[intent_name] = responses_list.split(',')

    return intents, responses

def match_intent(user_input, intents):
    user_input = user_input.lower()
    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in user_input:
                return intent
    return None

def get_response(user_input, responses):
    intent = match_intent(user_input, intents)
    return random.choice(responses.get(intent, ["I'm sorry, I didn't understand."]))

if __name__ == "__main__":
    intents, responses = load_data('data.txt')

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        response = get_response(user_input, responses)
        print("Chatbot:", response)
