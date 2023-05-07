import os
import telebot
from dotenv import load_dotenv
#loading API key
load_dotenv()

API_KEY = os.getenv('API_KEY')
#bot creation
bot = telebot.TeleBot(API_KEY)


#starting message of the bot
@bot.message_handler(commands=['start', 'Start'])
def instructions(message):
    bot.send_message(message.chat.id, "Hi!, This is Darwin...I'm here to help you")
    bot.send_message(message.chat.id, "see few commands to chat with me")
    bot.send_message(message.chat.id, "click here ---> /list to see commands")

#list of commands after pressing the /list command
@bot.message_handler(commands=['list', 'List', 'LIST'])
def listCommands(message):
    bot.send_message(message.chat.id, "To get notes click here---> /notes \nTo get Templates click here---> /templates \nTo get Lab Manuals click here---> /lab \n ")
    

#Asking subject to get notes
@bot.message_handler(commands=['notes', 'Notes'])
def notes(message):
    bot.reply_to(message, "choose your subject")
    bot.send_message(message.chat.id, "Mobile Application Development---> /mad")
    bot.send_message(message.chat.id, "Machine Learning---> /ml")
    bot.send_message(message.chat.id, "Intrusion Detection System---> /ids")
    bot.send_message(message.chat.id, "Software Testing Methodologies---> /stm")
    bot.send_message(message.chat.id, "Robotics & Automation---> /RnA")

#Asking the unit number if MAD selected
@bot.message_handler(commands=['mad', 'Mad', 'MAD'])
def madNotes(message):
    bot.reply_to(message, "which unit?")
    bot.send_message(message.chat.id, "unit1---> /mad_unit1")
    bot.send_message(message.chat.id, "unit2---> /mad_unit2")
    bot.send_message(message.chat.id, "unit3---> /mad_unit3")
    bot.send_message(message.chat.id, "unit4---> /mad_unit4")
    bot.send_message(message.chat.id, "unit5---> /mad_unit5")

#Funtion to send unit1 notes
@bot.message_handler(commands=['mad_unit1'])
def madUnit1(message):
    madUnit1 = open('mad/mad_unit1.pdf', 'rb')
    bot.send_message(message.chat.id, 'Here is your unit 1 notes')
    bot.send_document(message.chat.id, madUnit1)

#Funtion to send unit2 notes
@bot.message_handler(commands=['mad_unit2'])
def madUnit2(message):
    madUnit2 = open('mad/mad_unit2.pdf', 'rb')
    bot.send_message(message.chat.id, 'Here is your unit 2 notes')
    bot.send_document(message.chat.id, madUnit2)

#Funtion to send unit3 notes
@bot.message_handler(commands=['mad_unit3'])
def madUnit3(message):
    madUnit3 = open('mad/mad_unit3.pdf', 'rb')
    bot.send_message(message.chat.id, 'Here is your unit 3 notes')
    bot.send_document(message.chat.id, madUnit3)

#Funtion to send unit4 notes
@bot.message_handler(commands=['mad_unit4'])
def madUnit4(message):
    madUnit4 = open('mad/mad_unit4.pdf', 'rb')
    bot.send_message(message.chat.id, 'Here is your unit 4 notes')
    bot.send_document(message.chat.id, madUnit4)

#Funtion to send unit5 notes
@bot.message_handler(commands=['mad_unit5'])
def madUnit5(message):
    madUnit5 = open('mad/mad_unit5.pdf', 'rb')
    bot.send_message(message.chat.id, 'Here is your unit 5 notes')
    bot.send_document(message.chat.id, madUnit5)
#mad notes section completed


#Asking unit number if ML selected
@bot.message_handler(commands=['ml', 'ML', 'Ml'])
def mlNotes(message):
    bot.reply_to(message, "which unit?")
    bot.send_message(message.chat.id, "unit1---> /ml_unit1")
    bot.send_message(message.chat.id, "unit2---> /ml_unit2")
    bot.send_message(message.chat.id, "unit3---> /ml_unit3")
    bot.send_message(message.chat.id, "unit4---> /ml_unit4")
    bot.send_message(message.chat.id, "unit5---> /ml_unit5")

#Funtion to send unit1 notes
@bot.message_handler(commands=['ml_unit1'])
def mlUnit1(message):
    mlUnit1 = open('ml/ml_unit1.pdf', 'rb')
    bot.send_message(message.chat.id, 'Here is your unit 1 notes')
    bot.send_document(message.chat.id, mlUnit1)

#Funtion to send unit2 notes
@bot.message_handler(commands=['ml_unit2'])
def mlUnit2(message):
    mlUnit2 = open('ml/ml_unit2.docx', 'rb')
    bot.send_message(message.chat.id, 'Here is your unit 2 notes')
    bot.send_document(message.chat.id, mlUnit2)

#Funtion to send unit3 notes
@bot.message_handler(commands=['ml_unit3'])
def mlUnit3(message):
    mlUnit3 = open('ml/ml_unit3.pdf', 'rb')
    bot.send_message(message.chat.id, 'Here is your unit 3 notes')
    bot.send_document(message.chat.id, mlUnit3)

#Funtion to send unit4 notes
@bot.message_handler(commands=['ml_unit4'])
def mlUnit4(message):
    mlUnit4 = open('ml/ml_unit4.pdf', 'rb')
    bot.send_message(message.chat.id, 'Here is your unit 4 notes')
    bot.send_document(message.chat.id, mlUnit4)

#Funtion to send unit5 notes
@bot.message_handler(commands=['ml_unit5'])
def mlUnit5(message):
    mlUnit5 = open('ml/ml_unit5.pdf', 'rb')
    mlUnit05 = open('ml/ml_unit05.pdf', 'rb')
    bot.send_message(message.chat.id, 'Here is your unit 5 notes')
    bot.send_document(message.chat.id, mlUnit5)
    bot.send_message(message.chat.id, 'Wait...')
    bot.send_document(message.chat.id, mlUnit05)
#machine learning section completed

#Asking unit number if IDS selected
@bot.message_handler(commands=['ids', 'IDS', 'Ids'])
def mlNotes(message):
    bot.reply_to(message, "which unit?")
    bot.send_message(message.chat.id, "unit1---> /ids_unit1")
    bot.send_message(message.chat.id, "unit2---> /ids_unit2")
    bot.send_message(message.chat.id, "unit3---> /ids_unit3")
    bot.send_message(message.chat.id, "unit4---> /ids_unit4")
    bot.send_message(message.chat.id, "unit5---> /ids_unit5")

    #ToDo: 1, 2, 3 units are not available

@bot.message_handler(commands=['ids_unit1', 'ids_unit2', 'ids_unit3'])
def idsUnit123(message):
    bot.reply_to(message, 'sorry! currently unavailable. We will upgrade our database soon')

#Funtion to send unit4 notes
@bot.message_handler(commands=['ids_unit4'])
def idsUnit4(message):
    idsUnit4 = open('ids/ids_unit4.docx', 'rb')
    bot.send_message(message.chat.id, 'Here is your unit 4 notes')
    bot.send_document(message.chat.id, idsUnit4)

#Funtion to send unit5 notes
@bot.message_handler(commands=['ids_unit5'])
def idsUnit5(message):
    idsUnit5 = open('ids/ids_unit5.docx', 'rb')
    bot.send_message(message.chat.id, 'Here is your unit 5 notes')
    bot.send_document(message.chat.id, idsUnit5)




#ToDo: Need to add ids notes present ids notes are not available


#Asking the unit number if RnA selected
@bot.message_handler(commands=['RnA', 'rna', 'RNA'])
def RnANotes(message):
    bot.reply_to(message, "which unit?")
    bot.send_message(message.chat.id, "unit1---> /RnA_unit1")
    bot.send_message(message.chat.id, "unit2---> /RnA_unit2")
    bot.send_message(message.chat.id, "unit3---> /RnA_unit3")
    bot.send_message(message.chat.id, "unit4---> /RnA_unit4")
    bot.send_message(message.chat.id, "unit5---> /RnA_unit5")


#Funtion to send unit1 notes
@bot.message_handler(commands=['RnA_unit1'])
def RnAUnit1(message):
    RnAUnit1 = open('rna/RnA_unit1.pdf', 'rb')
    bot.send_message(message.chat.id, 'Here is your unit 1 notes')
    bot.send_document(message.chat.id, RnAUnit1)

#Funtion to send unit2 notes
@bot.message_handler(commands=['RnA_unit2'])
def RnAUnit2(message):
    RnAUnit2 = open('rna/RnA_unit2.pdf', 'rb')
    bot.send_message(message.chat.id, 'Here is your unit 2 notes')
    bot.send_document(message.chat.id, RnAUnit2)

#Funtion to send unit3 notes
@bot.message_handler(commands=['RnA_unit3'])
def RnAUnit3(message):
    RnAUnit3 = open('rna/RnA_unit3.pdf', 'rb')
    bot.send_message(message.chat.id, 'Here is your unit 3 notes')
    bot.send_document(message.chat.id, RnAUnit3)

#Funtion to send unit4 notes
@bot.message_handler(commands=['RnA_unit4'])
def RnAUnit4(message):
    RnAUnit4 = open('rna/RnA_unit4.pdf', 'rb')
    bot.send_message(message.chat.id, 'Here is your unit 4 notes')
    bot.send_document(message.chat.id, RnAUnit4)

#Funtion to send unit5 notes
@bot.message_handler(commands=['RnA_unit5'])
def RnAUnit5(message):
    bot.reply_to(message, 'sorry! currently unavailable. We will upgrade our database soon')



#ToDo: Need other another three units notes (subject:R&A)

#Asking the unit number if stm selected
@bot.message_handler(commands=['stm', 'STM', 'Stm'])
def stmNotes(message):
    bot.reply_to(message, "which unit?")
    bot.send_message(message.chat.id, "unit1---> /stm_unit1")
    bot.send_message(message.chat.id, "unit2---> /stm_unit2")
    bot.send_message(message.chat.id, "unit3---> /stm_unit3")
    bot.send_message(message.chat.id, "unit4---> /stm_unit4")
    bot.send_message(message.chat.id, "unit5---> /stm_unit5")

#Funtion to send unit1 notes
@bot.message_handler(commands=['stm_unit1'])
def stmUnit1(message):
    stmUnit1 = open('stm/stm_unit1.pptx', 'rb')
    bot.send_message(message.chat.id, 'Here is your unit 1 notes')
    bot.send_document(message.chat.id, stmUnit1)

#Funtion to send unit2 notes
@bot.message_handler(commands=['stm_unit2'])
def stmUnit2(message):
    stmUnit2 = open('stm/stm_unit2.pptx', 'rb')
    bot.send_message(message.chat.id, 'Here is your unit 2 notes')
    bot.send_document(message.chat.id, stmUnit2)

#Funtion to send unit3 notes
@bot.message_handler(commands=['stm_unit3'])
def stmUnit3(message):
    stmUnit3 = open('stm/stm_unit3.pptx', 'rb')
    bot.send_message(message.chat.id, 'Here is your unit 3 notes')
    bot.send_document(message.chat.id, stmUnit3)

#ToDo: need more 2 units to be added (subject : STM)

#Function to send unit 4,5
@bot.message_handler(commands=['stm_unit4', 'stm_unit5'])
def stmUnit45(message):
    bot.reply_to(message, 'sorry! currently unavailable. We will upgrade our database soon')

#for Lab Manuals
@bot.message_handler(commands=['lab', 'Lab', 'LAB'])
def labManuals(message):
    bot.reply_to(message, "choose subject...")
    bot.send_message(message.chat.id, "MAD---> /madManual \nML---> /mlManual")

#sending MAD manual
@bot.message_handler(commands=['madManual'])
def madManual(message):
    madManual = open('madManual/madManual.pdf', 'rb')
    bot.send_message(message.chat.id, "Here is your manual")
    bot.send_document(message.chat.id, madManual)

#sending ML manual
@bot.message_handler(commands=['mlManual'])
def mlManual(message):
    mlManual = open('mlManual/mlManual.pdf', 'rb')
    bot.send_message(message.chat.id, "Here is your manual")
    bot.send_document(message.chat.id, mlManual)

#section if templates selected

#choosing template

@bot.message_handler(commands=['templates'])
def templates(message):
    bot.reply_to(message, 'choose templates')
    bot.send_message(message.chat.id, 'assignment---> /assignment \napp development---> /appdev')

#sending assignment template
@bot.message_handler(commands=['assignment', 'Assignment'])
def assignmentTemplate(message):
    assignmentTemplate = open('booklet/AssignmentTemplate.pdf', 'rb')
    bot.send_message(message.chat.id, "Here is your template")
    bot.send_document(message.chat.id, assignmentTemplate)

#sending app development forms
@bot.message_handler(commands=['appdev'])
def appdev(message):
    AbstractSubmissionForm = open('booklet/AbstractSubmissionForm.pdf', 'rb')
    
    bot.send_message(message.chat.id, "Here are your forms")
    bot.send_document(message.chat.id, AbstractSubmissionForm)




bot.polling()