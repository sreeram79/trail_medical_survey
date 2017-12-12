import os,sys

class RawInputCommand:
    '''
     TODO: would be better if not hardcoded here and use the cardinality between the boolean_factor types and define in commondef class.
    '''
    __indicator ={'1':'F','2':'T','3':'U'}
    '''
     TODO: would be better if not hardcoded the question and not using any type of class association with probability_record Class.
          to achieve the consistency in association and adding a new types it would be better to create a questioniare class associated with
	  probabilityrecord.
    '''
    __expected={'pregnant':'are you pregnant?',
                'smoke':'do you smoke?',
                'blood_pressure':'do you have high blood pressure?',
                'chemotherapy':'have you ever had chemotherapy?',
                'previous_trial':'have you previously participated in a clinical trial?'
               }
    '''
       Initiliase still_true as false because this will be instantiated every time when a new question is asked
    '''
    def __init__(self):
        self.still_true =False
    '''
       Rum command function below gets the question type and metrics to show the progress of the probability everytime when a question is asked.

    '''
    def run_command(self, question, average, metrics):
       print("Based on exisitng data the acceptance rate for the clinical trial would be {}%  your acceptance rate would be {}".format(average, metrics))
       while not self.still_true:
           print '+'*100
           print '+'*100
           print ("Question : {}").format(self.__expected[question])
           print '1. False'
           print '2. True'
           print '3. would like to skip'
           number = raw_input("select your choice by entering 1 or 2 or 3 only: ")
           self.still_true = number.isdigit() and True if number in self.__indicator else False
       return self.__indicator[number]
