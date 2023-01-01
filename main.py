# import all the gbo-gbo-ti-gbo
from requests import *
from telegram import *
from telegram.ext import *

# set variables
BOT_API = "1982666554:AAE_SP3hvjRTVPAloOfitpExyb0tTpSbIGA"
updater = Updater (BOT_API, use_context=True)
dp = updater.dispatcher
randompeopleurl = "https://thispersondoesnotexist.com/image"
randomimageurl = "https://picsum.photos/200"
likes = 0
dislikes =0


# show that the bot has started
print ("Bot started...")

# start command
def start (update: Update, context: CallbackContext):
    # this will create the Keyboard
    buttons = [[KeyboardButton ("Random Image")], [KeyboardButton ("Random Person")]]
    # this will send a message
    context.bot.send_message (chat_id = update.effective_chat.id, text = f"Hello {update.effective_chat.username} or should i call you {update.effective_chat.first_name} and Welcome", reply_markup = ReplyKeyboardMarkup (buttons))

# handle messages from the user
def messageHandler(update: Update, context: CallbackContext):
    # get the images if the user selects any of the options
    if "Random Person" in update.message.text:
        image = get(randompeopleurl).content

    if "Random Image" in update.message.text:
        image = get(randomimageurl).content

    # post the image
    if image:
        context.bot.sendMediaGroup (chat_id = update.effective_chat.id, media = [InputMediaPhoto (image, caption = "")])

# add emojis so the user can like or dislike - using InlineKeyboardButtons
# callback_data explains the emojis
        buttons = [[InlineKeyboardButton ("👍", callback_data="like")], [InlineKeyboardButton ("👎", callback_data="dislike")]]
        context.bot.send_message (chat_id = update.effective_chat.id, reply_markup = InlineKeyboardMarkup (buttons), text = "Did you like this image?")

# a function to handle all the queries
def queryhandler (update, context):
    query = update.callback_query.data
    
    # call the global variables - likes and dislikes
    global likes, dislikes

    if "like" in query:
        likes += 1
    if "dislike" in query:
        dislikes += 1

    print (f"likes => {likes} and dislikes => {dislikes}")

# add the handlers
dp.add_handler(CommandHandler ("start", start))
dp.add_handler(CallbackQueryHandler (queryhandler))
dp.add_handler (MessageHandler (Filters.text, messageHandler))

# start the bot
updater.start_polling()
updater.idle()

#NOTE: It is possible to allow ONLY selected usernames to be able to like or dislike images?
