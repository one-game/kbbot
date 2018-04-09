# -*- coding: utf-8 -*-
import aiml
import sys
import os
#import jieba

def app_init():
    '''
      app global init.
    '''
    pass

def app_run():
    '''
      app main entrance
    '''

    while True:
        message = raw_input("Enter your message >> ")
        print message
    pass

class KBBot(object):
    '''
      Bot Class defination
    '''

    def __init__(self):
    	self._bot = aiml.Kernel()
    	self._bot.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
        pass

    def get_response(self, question, user_id="__global"):
        
        #todo: preprocess question

        #todo: parse question
        parse_result = self._bot.respond(question, user_id)

        self._bot.setPredicate("question_parsed", 1)
        #todo: to answer the question
        answer = self._bot.respond(question, user_id)
        #todo: post process the answer

        pass



if __name__ == "__main__":
    app_init()
    app_run()