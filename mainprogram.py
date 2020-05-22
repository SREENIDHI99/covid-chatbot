import random
botname=("covid-helper")
name=input("enter ur name")
GREETING_INPUTS = ["hello", "hi", "greetings","gm" ,"good morning","good afternoon","ga","hola"]
GREETING_RESPONSES = ["hi", "hey" , "hi there", "hello","hellllo","wassup"]
SENDOFF_RESPONSES=["bye","take care"]
SENDOFF_INPUTS=["tq","thankq","I am so blessed"]
Bcovid_questions=[["what is covid","tell me the base of covid birth"]]
Bcovid_answer=open("bqueres.txt","r")
Scovid_questions=["what are symptoms of covid","symptoms related to covid"]
Scovid_answer=open("squeres.txt","r")
Vcovid_question=["is there a vaccine for covid","what is the vaccination for covid"]
Vcovid_answer=open("vqueres.txt","r")
Pcovid_question=["what are necessary precautions for covid","how to get rid of covid","how to avoid covid"]
Pcovid_answer=open("pqueres.txt","r")
def greeting(sent):
            return random.choice(GREETING_RESPONSES)
def sendoff(Sent):
            return random.choice(SENDOFF_RESPONSES)
def bque(sent):
    print(Bcovid_answer.read())
def sque(sent):
    print(Scovid_answer.read())
def vque(sent):
    print(Scovid_answer.read())
def pque(sent):
    print(Scovid_answer.read())
        
flag=True
print("hiee!!this is ur medi bot")
while(flag==True):
    user_response=input()
    user_response=user_response.lower()
    if(user_response in (GREETING_INPUTS)):
        bot_response=(greeting(user_response))
        print(bot_response)
    print("I am glad that you choosed me.I can be your friendly doctor")
    print("how can i help u to solve ur health issues")
    flag=False
while(flag==False):
     user_response=input()
     user_response=user_response.lower()
     if(user_response in (Bcovid_questions)):
         bot_response=(bque(user_response))
     if(user_response in (Scovid_questions)):
         bot_response=(sque(user_response))
     if(user_response in (Vcovid_questions)):
         bot_response=(vque(user_response))
     if(user_response in (Pcovid_questions)):
         bot_response=(pque(user_response))
if(user_response in(SENDOFF_INPUTS)):
    bot_response=(sendoff(user_response))
    print(bot_response)
