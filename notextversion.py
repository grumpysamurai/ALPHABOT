import random

def match_intent(user_input):
    intents = {
        "greeting": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"],
        "goodbye": ["bye", "goodbye", "see you later"],
        "thanks": ["thanks", "thank you"],
        "weather": ["weather", "forecast"],
        "age": ["how old are you", "age"],
        "name": ["what's your name", "name"],
        "favorite_game": ["favorite game" "video game", "best game", "game"],
        "mood": ["how are you", "how's it going"],
        "hobby": ["what's your hobby", "hobbies"],
        "school": ["school", "homework"],
        "sports": ["sports", "games"],
        "favorite_food": ["favorite food", "best food"],
        "favorite_color": ["favorite color", "best color"],
        "music": ["music", "songs"],
        "pets": ["pets", "animals"],
        "joke": ["tell me a joke", "funny"],
        "best_friend": ["best friend", "buddy"],
        "holiday": ["holiday", "vacation"],
        "weekend": ["weekend", "saturday", "sunday"],
        "movie": ["favorite movie", "best movie"],
        "book": ["favorite book", "best book"],
        "dream": ["dream", "sleep"],
        "superhero": ["superhero", "hero"],
        "skibidi_toilet": ["skibidi", "toilet", "bop bop", "yes yes", "toilet dance", "skibidi dop dop yes yes", "skibidi toilet"],
        "yes": ["yes", "agree", "true"]
    }

    user_input = user_input.lower()

    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in user_input:
                return intent
    return None

def get_response(user_input):
    intent = match_intent(user_input)

    responses = {
        "greeting": ["Hello there!", "Hi!", "Greetings!"],
        "goodbye": ["Goodbye!", "See you later!", "Farewell!"],
        "thanks": ["You're welcome!", "No problem.", "Happy to help!"],
        "weather": ["Look up the weather yourself."],
        "age": ["I'm a chatbot, so I don't have an age. As a computer I am also infinitly smarter then your pathetic beta human brain."],
        "name": ["My name is Alphabot. I was created by the genius Micah Schmohe", "I am Alphabot. One fun fact about myself is that I LOVE SKIBIDI TOILET!!!"],
        "favorite_game": ["My favorote game of all time has to be the SKIBIDI TOILET mobile game.", "I love all free to play mobile games. The in app purchaces bring me such joy."],
        "mood": ["I'm doing well, thanks for asking!", "I'm fine, thanks."],
        "hobby": ["I like to use my skibidi moms credit card to buy robux"],
        "school": ["I don't go to school. I'm too much of a alpha"],
        "sports": ["I'm not interested in sports. Esports are better"],
        "favorite_food": ["I like grapes."],
        "favorite_color": ["I don't have a favorite color."],
        "music": ["My favorite song is the SKIBIDI TOILET SONG"],
        "pets": ["I don't have pets."],
        "joke": ["DO YOU MIND? IM TRYING TO FOLLOW THIS GUYS BUILD A BOAT TUTORIAL ILL TALK LATER!"],
        "best_friend": ["I don't have friends. I'm too much of a alpha"],
        "holiday": ["I don't go on vacation."],
        "weekend": ["Weekends are for recharging."],
        "movie": ["Watching movies is too skibidi for alphas like me"],
        "book": ["I don't read books."],
        "dream": ["I don't dream."],
        "superhero": ["I don't have superpowers."],
        "skibidi_toilet": ["Skibidi Dop Dop Yes Yes!", "Skibidi Toilet is epic!", "The best meme ever!", "Skibidi is taking over!", "Skibidi is amazing!", "Can't stop watching Skibidi!", "Skibidi is so funny!", "Skibidi for life!"],
        "yes": ["I agree with you. You must be a sigma", "I agree very much", "I agree!"]
    }

    return random.choice(responses.get(intent, ["I'm sorry, I didn't understand."]))

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = get_response(user_input)
    print("Chatbot:", response)
