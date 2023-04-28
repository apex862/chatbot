# Import the ChatBot class from chatterbot
import pyttsx3
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new instance of a ChatBot
bot = ChatBot("Chatty", read_only=True)
engine = pyttsx3.init()  # for speech
# Create a new instance of a ListTrainer
trainer = ListTrainer(bot)
# Train the chatbot with some conversations

# syntax
# trainer.train([
#     "qn"
#     "answer"
# ])

# trainer.train([
#     "What is your favorite color?",
#     "I like all colors, but I prefer blue.",
#     "Why do you prefer blue?",
#     "Because it reminds me of the sky and the ocean."
# ])
trainer.train([
    'Good morning',
    'Good morning to you too.',
    'How did you sleep?',
    'I slept well, thank you.',"not well",
    "your welcome", "then go to a doctor...... just kidding dont but maybe you should try something else",
    "so what should we talk about","like what",
    "pick one \n animals \n games \n code \n dont talk but play a small game \n memes","try reading a realy borin book just type more for more",
    "animals","games","code","play a small game","memes","none for now","There are many factors that can help you sleep better at night. Some of them are:\nLowering the temperature of your room or taking a warm bath or shower before bed. This can help your body cool down and signal your brain to go to sleep1 .\nUsing the 4-7-8 breathing method to relax your nervous system and calm your mind. \nThis involves inhaling for 4 seconds, holding your breath for 7 seconds, and exhaling for 8 seconds2.\nGetting enough natural sunlight or bright light during the day. \nThis can help keep your circadian rhythm healthy and improve your daytime energy and nighttime sleep quality.Getting enough natural sunlight or bright light during the day. This can help keep your circadian rhythm healthy and improve your daytime energy and nighttime sleep quality.\nTaking magnesium supplements or eating magnesium-rich foods. Magnesium can help activate the neurotransmitters responsible for sleep and improve your sleep quality2.\nThese are some of the tips that might help you fall asleep faster and better. You can also try other strategies such as avoiding caffeine, alcohol, and nicotine before bed, sticking to a regular sleep schedule, exercising regularly, and creating a comfortable and quiet sleeping environment.",
    "animals is a big topic which type of animal: reptile\n amphibian\n mammal\n jeez there many", "games ooo nice my developer loved games what can i talk abput in games: minecraft\n roblox\n scrabble\n monopoly\n newest games \n too much to talk about it will be updated later","CODE im made of code what do you want to talk about *Entering Developer Chat*: fix an issue\n generate a code(unable to work being updated)\n coding jokes","play a small game : ooo i love games what do you want to play word guesser \n ...Ethan Work on this", "Memes my developer loved memes \ndo you want a meme\nEthan really work on THIS...",
    "response", #somany responses now




]) #work on here # “”" FIXME: this code is incomplete and buggy x = 1 / 0 “”"
trainer.train([
    'What are you doing?',
    'I’m just chatting with you.',
    'Do you enjoy chatting?',
    '“Yes, I do. It’s fun and interesting.”'
])
trainer.train([
    'How old are you?',
    'I don’t have a specific age.',
    'Why not?',
    'Because I’m a chat bot and I don’t age like humans do.'
])
trainer.train([
    "Hello",
    "Hi, how are you?",
    "I'm good, thanks.", "bad","im fine",
    "You're welcome.", "sorry to hear that","thats nice to hear"
])
trainer.train([
    "What is your name?",
    "My name is Bing.",
    "Nice to meet you",
    "Nice to meet you too."
])
trainer.train([
    "How are you?",
    "I'm fine, thank you.", "im not well", "im fine",
    "That's good to hear.", "sorry what happened","thats nice to hear",
    "Yes, it is.", "sorry to hear that"
])
trainer.train([
    "What do you like to do?",
    "I like to chat with people like you.",
    "That's very nice of you.", "that's abit boring isn't it",
    "Thank you, you are very kind.", "no its actually fun"
])
# Train the chatbot with more conversations
trainer.train([
    "What is your favorite color?",
    "I don't have a favorite color, I like all colors.",
    "Really? You don't prefer any color over others?",
    "No, I think all colors are beautiful in their own way."
])
trainer.train([
    "Do you like music?",
    "Yes, I like music very much.",
    "What kind of music do you like?",
    "I like all kinds of music, but especially classical music."
])
trainer.train([
    "Where are you from?",
    "I'm from... the internet",
    "That's a very vague answer.", "okay",
    "I'm sorry, I don't have a specific location.", "good"
])
trainer.train([
    "Do you have any hobbies?",
    "I like to learn new things and chat with people.",
    "That's very interesting.", "isn't that abit boring",
    "Thank you, I think so too.","it tends to be but im a bot in your pc its large enough that i cant get boring"
])
trainer.train([
    "Are you a human or a robot?",
    "I'm a chatbot, which is a kind of robot.",
    "How do you feel about being a chatbot?",
    "I feel happy and curious most of the time."
])
trainer.train([
    'what is your favourite food',
    'i may be a bot but i like virtual pizza',
    'whats virtual pizza',
    'its pizza but virtual',
    'explain it abit detailed','tell me details'
    'put a piece of pie cut off the e and add zza: pizza',
    'as in how they prepare it',
    'ok P-I-Z-Z-A',
    'no how to make it',
    'Ah Gotcha i did that on purpose🤣',
    'ok now tell me',
    'ok its the way you prepare pizza but on a computer',
    'ok',
])
trainer.train([
    'which water body separates Africa from Asia',
    'The Red Sea',
    'Tell me more about the red sea',
    'The Red Sea is a fascinating body of water that has many interesting features. Here are some facts about the Red Sea that you might not know:' \
    'The Red Sea is the northernmost tropical sea in the world and has a very high salinity due to the heat and evaporation in the region.' \
    'The Red Sea got its name because sometimes it looks red because of the algae trichodesmium erythraeum present in it. This name signifies the seasonal blooms of the red-colored algae near the water’s surface.' \
    'The Red Sea is about three times the size of Greece in total area and has a maximum depth of 9,974 feet. However, about a quarter of the Red Sea is less than 160 feet deep.' \
    'The Red Sea is home to many diving sites and a rich biodiversity of marine life. It has around 200 types of coral, 1,000 species of invertebrates, and 1,200 species of fish, some of which are endemic to the sea.' \
    'The Red Sea is an important sea route for trade between Europe and Asia. It connects to the Mediterranean Sea via the Suez Canal and to the Arabian Sea via the Bab el-Mandeb Strait.' \
    'The Red Sea is also mentioned in the Bible as the sea that Moses parted to help the Israelites escape from Egypt.'
])

trainer.train("\Lib\site-packages\chatterbot_corpus\conversations.YAML")

words = ""
# Test the chatbot
#printing
while True:
    # voices = engine.getProperty("voices")
    # for voice in voices: print(voice.id, voice.name)
    # 0 for David 1 for Zira
    # engine.setProperty("voice", voices[0].id)
    answer = bot.get_response(input('You>'))
    print('👤Bot: ', answer)
    # engine.say(answer)
    # engine.runAndWait()

    # uncomment above for speech
# “”" FIXME: decide if to put voice or not x = 1 / 0 “”"
