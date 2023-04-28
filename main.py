import re
import long_responses as long
def message_probability(user_message, recognised_words, single_response=False, required_words=()):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # calculates the percent of recognised words in a user message_certainty
    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break


    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

# Responses-------------------------------------------------------------------------------------------------------------
def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal  highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

# responses__________________________________________________________________________
    response('Hello §! What would you like to do',  ['hello', 'hi', 'sup', 'hey', 'heyo'], single_response=False)
    response('I\'m doing fine, and you?',  ['how', 'are' , 'you', 'doing' ], required_words = ['how'])
    response('i cant generate images i am not made with opencv', ['generate', 'an', 'image', 'create', 'make'], required_words=['image'])
    response('Thank you!',  ['i', 'love' , 'code' , 'this', 'software', 'like'], required_words=['software','like' ])

    # responses located in other file
    response(long.HWAM, ['how', 'are', 'windows', 'made', 'tell', 'me', 'window'], required_words=['how', 'windows', 'made'])
    response(long.R_EATING, ['what', 'do', 'you', 'like', 'to', 'eat' ], required_words=['you', 'eat'])
    response(long.GMACIC, ['generate', 'for', 'me', 'a', 'code', 'in', 'c'], required_words=['code', 'c', 'generate'])
    response(long.IDLTS, ['i','dont', 'like', 'this', 'software', 'app', 'theres', 'a', 'problem'], required_words=['problem','this ','software'])
    response(long.ToSlow, [ '/','prob' ,'is' , 'you', 'are', 'too','slow','operate', 'very'], required_words=['slow', 'operate', '/', 'prob', 'is:'])
    response(long.givwrongres, ['/','prob' ,'is' , 'you', 'give', 'wrong', 'answers'],required_words=['/', 'prob', 'is:', 'you', 'wrong', 'answers'])
    response(long.randbigwords, ['i', 'see', 'random', 'big', 'words', 'on', 'the', 'screen'], required_words=['words', 'i'])



    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # for debugging un comment above to see why it prints a value

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

# test response system
while True:
    print('©Bot: ' + get_response(input('§You: ')))