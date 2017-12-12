import os,sys
'''
BooleanFactor class keep tracking the probability of trails
'''
class BooleanFactor:
    '''
       Initiliase the name of the boolean factor and setting the counter to zero
    '''
    def __init__(self,name):
        self.name = name
        self.count = 0
    '''
       incrementing the counter
    '''
    def increment(self):
        self.count += 1
    '''
        get function to return the name of the boolean factor
    '''
    def get_name(self):
        return self.name
    '''
       get function to return the counter value for the boolean factor
    '''
    def get_count(self):
        return self.count

'''
probability_record class keep probability stats for each questions
'''
class ProbabilityRecord:
    '''
       would be better to use boolean_field in the common def class
    '''
    __boolean_fields=['T','F','U']
    '''
       Initiliase name of the question stats with the boolean type
    '''
    def __init__(self,name):
        self.name=name
        self.boolean_ids = [BooleanFactor(value) for value in self.__boolean_fields]
    '''
       Initiliase still_true as false because this will be instantiated every time when a new question is asked
    '''
    def get_name(self):
        return self.name
    '''
       Initiliase still_true as false because this will be instantiated every time when a new question is asked
    '''
    def increment(self,value):
        self.boolean_ids[self.__boolean_fields.index(value)].increment()
    '''
       Initiliase still_true as false because this will be instantiated every time when a new question is asked
    '''
    def get_probability_record(self):
        return {self.name:{ self.boolean_ids[self.__boolean_fields.index(value)].get_name(): self.boolean_ids[self.__boolean_fields.index(value)].get_count() for value in self.__boolean_fields}}
    '''
       Initiliase still_true as false because this will be instantiated every time when a new question is asked
    '''
    def get_metrics_based_on_boolean_fact(self,answer_type):
        return self.boolean_ids[self.__boolean_fields.index('T' if answer_type == 'F' else 'U' if answer_type == 'T' else 'U')].get_count()
