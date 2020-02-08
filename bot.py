import telebot
import time

bot_token = '1038832449:AAHG2kCCqUecwUW_1vn36FfC6kQg1lbvI7I'

bot = telebot.TeleBot(token=bot_token)

def find_at(msg):
    for text in msg:
        if '@' in text:
            return text


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome, My name is EduBot created to help you learn \n if you need help on how to command me, please select "/help" To start now, kindly Type your matric number starting with @ for Example @mat1121122.')


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'Hello, this is an interactive Bot created with the aim of helping you learn anytime with quiz. To start, simply select "/start". You can also check available course by selecting "/course"')


@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def at_answer(message):
    texts =  message.text.split()
    at_text = find_at(texts)

    bot.reply_to(message,'So nice to meet you. Please select /course to start learning right now'.format(at_text[1:]),)


@bot.message_handler(commands=['course'])
def send_welcome(message):
    bot.reply_to(message, 'These are the available courses you can learn on this Bot\n /comp1 Introduction to computer \n /comp2 Cyber Security \n so which would you have me load for you righ now? \n remember you can always select /course to select another.')


@bot.message_handler(commands=['comp1'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome to Introduction to Computer \n Course Outline \n 1.What is a computer  \n 2.Your Personal Computer Hardware \n 3.The Processor and Memory \n 4.Internet and Networking \n /startcomp1')


@bot.message_handler(commands=['startcomp1'])
def send_welcome(message):
    bot.reply_to(message, 'What is a computer \n A computer is a machine that can be programmed to accept data (input), process it into useful information (output), and store it away (in a secondary storage device) for safekeeping or later reuse. ... Input devices accept data in a form that the computer can use; they then send the data to the processing unit.  \n /startcomp2')



@bot.message_handler(commands=['startcomp2'])
def send_welcome(message):
    bot.reply_to(message, ' Your Personal Computer Hardware \n The input device, in this case, is a keyboard, which you use to type in the original essay and any changes you want to make to it. All computers, large and small, must have a central processing unit within the personal computer housing. The central processing unit under the direction of the word processing software accepts the data you input through the keyboard. Processed data from your personal computer is usually output in two forms: on a screen and eventually by a printer. As you key in the essay on the keyboard, it appears on the screen in front of you. After you examine the essay on the screen, make changes, and determine that it is acceptable, you can print the essay on the printer. Your secondary storage device in this case is a diskette, a magnetic medium that stores the essay until it is needed again. \n /startcomp3')


@bot.message_handler(commands=['startcomp3'])
def send_welcome(message):
    bot.reply_to(message, ' Your Personal Computer Hardware \n The input device, in this case, is a keyboard, which you use to type in the original essay and any changes you want to make to it. All computers, large and small, must have a central processing unit within the personal computer housing. The central processing unit under the direction of the word processing software accepts the data you input through the keyboard. Processed data from your personal computer is usually output in two forms: on a screen and eventually by a printer. As you key in the essay on the keyboard, it appears on the screen in front of you. After you examine the essay on the screen, make changes, and determine that it is acceptable, you can print the essay on the printer. Your secondary storage device in this case is a diskette, a magnetic medium that stores the essay until it is needed again. \n /startcomp4')


@bot.message_handler(commands=['startcomp4'])
def send_welcome(message):
    bot.reply_to(message, ' The Processor and Memory \n In a computer the processor is the center of activity. The processor, as we noted, is also called the central processing unit (CPU). The central processing unit consists of electronic circuits that interpret and execute program instructions, as well as communicate with the input, output, and storage devices. \n /compquiz')


@bot.message_handler(commands=['compquiz'])
def send_welcome(message):
    bot.reply_to(message, 'Hello, now that you are done with the four outlines for this course, its time to test if you really understand. \n To start the quiz select /compquiz \n To take the course again select /comp1 ')


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
