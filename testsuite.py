import os, sys, random, unittest
import trialsurvey.csv_file_process
from trialsurvey.csv_file_process import CSVFileReader
from trialsurvey.prob_trail import ProbabilityRecord
from trialsurvey.ra_input import RawInputCommand
from trialsurvey.prob_trail import BooleanFactor

class TestCSVFileReader(unittest.TestCase):

    def setUp(self):
        self.file= 'trialsurvey.csv'
        
    '''
	check whether the file exist
    '''
    def test_readfile(self):
        # make sure the file exists in the folder
	file_loc= os.path.join(os.path.dirname(trialsurvey.csv_file_process.__file__),'..',self.file)
        self.assertTrue(os.path.exists(file_loc),"{} File doesn't exists".format(file_loc))
    '''
	failure case
    '''
    def test_readfilefailure(self):
        # make sure the file exists in the folder
	with self.assertRaises(SystemExit):
           CSVFileReader(None)

    '''
	Check the header list is matching
    '''
    def test_checkheaderlistmatching(self):
        # make sure the file exists in the folder
        expected_field = ['blood_pressure', 'chemotherapy', 'previous_trial', 'smoke', 'pregnant']
	csvfile = CSVFileReader(self.file)
        self.assertEqual(csvfile.get_headerlist(),expected_field)

    '''
	Check the acceptance rate expected rate is matching current give rate may not be standard rate all the time but
	as sampling for the moment so using it.
    '''
    def test_checkacceptancerate(self):
        # make sure the file exists in the folder
        expected_value = 24
	csvfile = CSVFileReader(self.file)
        self.assertEqual(csvfile.get_acceptancerate(),expected_value)   


class TestBooleanFactor(unittest.TestCase):
    def setUp(self):
        self.name = 'F'
	self.count = 0
   
    '''
	check whether the boolean factor object created name matches
    '''
    def test_booleanfactorname(self):
        # check the booleanfactor exist
	bfactor = BooleanFactor('F')
        self.assertEqual(bfactor.get_name(),self.name)
    '''
	check whether the file exist
    '''
    def test_checkincrementer(self):
        # check the booleanfactor incrementer works
	bfactor = BooleanFactor('F')
        self.assertEqual(bfactor.get_count(),self.count)
	self.count += 1
	bfactor.increment()
	self.assertEqual(bfactor.get_count(),self.count)

class TestProbabilityRecord(unittest.TestCase):
    def setUp(self):
        self.name='blood_pressure'
        self.boolean_ids = [BooleanFactor(value) for value in ['T','F','U']]
   
    '''
	check whether the Probability record object created name matches
    '''
    def test_booleanfactorname(self):
        # check the booleanfactor exist
	blood_pressure = ProbabilityRecord('blood_pressure')
        self.assertEqual(blood_pressure.get_name(),self.name)
    '''
	check whether the file exist
    '''
    def test_checkincrementer(self):
        # check the booleanfactor incrementer works
	blood_pressure = ProbabilityRecord('blood_pressure')
 	blood_pressure.increment('F')
	test_dict={'blood_pressure': {'U': 0, 'T': 0, 'F': 1}}
	self.assertEqual(blood_pressure.get_probability_record(),test_dict)

class TestRawInputCommand(unittest.TestCase):
   #TODO
   pass

if __name__ == '__main__':
    unittest.main()
