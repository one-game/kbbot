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
        pass

    def get_response(self, question, user_id="__global"):
        
        pass



if __name__ == "__main__":
    app_init()
    app_run()