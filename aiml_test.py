# -*- coding: utf-8 -*-
import aiml
import sys
import os
import jieba
 
def get_module_dir(name):
    path = getattr(sys.modules[name], '__file__', None)
    if not path:
        raise AttributeError('module %s has not attribute __file__' % name)
    return os.path.dirname(os.path.abspath(path))
 
 
# alice_path = get_module_dir('aiml') + '/alice'
# #切换到语料库所在工作目录
# os.chdir(alice_path)
os.chdir("./config/")

mybot = aiml.Kernel()
# alice.learn("startup.xml")
# alice.respond('LOAD ALICE')
# if os.path.isfile("mybot_brain.brn"):
#     mybot.bootstrap(brainFile="mybot_brain.brn")
# else:
#     mybot.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
#     mybot.saveBrain("mybot_brain.brn")
mybot.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
 
while True:
    message = raw_input("Enter your message >> ")
    message = message.decode("gbk") #.encode("utf-8")
    #message = " ".join(jieba.lcut(message))
    message = " ".join(message)
    welcome_string = u" 你好世界"
    mybot.setPredicate("welcome", welcome_string)
    print message
    if message == "quit":
        exit()
    elif message == "save":
        mybot.saveBrain("bot_brain.brn")
    else:
        bot_response = mybot.respond(message)
        bot_response = bot_response.replace(" ", "")
        print mybot._sessions
        # Do something with bot_response
        print bot_response.decode("utf-8").encode("gbk")