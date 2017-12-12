# trail_medical_survey

# Introduction:-
This is a short project and has done with minimal prototype for the given requirement. 

	a) CSVFileReader class in csv_file_process.py:
			CSVFileReader class helps in reading the given sample file and extract the data into the dictionary.
			
	b) ProbabilityRecord Class
			ProbabilityRecord class helps in holding and computing the cumulative values for the given questionaries.
			
	c) BooleanFactor Class
			BooleanFactor class helps to work on the input criteria from the survey['T','F','U']
			
	d) RawInputCommand Class
			RawInputCommand class helps to loop on the questions and gather the inputs from the users and displays the survey results. 
			

What can you expect:
	Hooray !!! Quite happy at least the basic things work ;-)
	a) Reads the sampling file and convert into a dictionary objects.
	b) Using the Dictionary objects try to do some computation for each questionaries and summation of the trails information
	c) Try to compute approximate get acceptance rate based on the given samples.
	d) Selection of choices are given to be selected for each questionaries 
	e) Keeping the base acceptance rate as 24 and try to compute the incremental based on the value inputted as False or True or undefined value.
	f) Metric is done on lot of assumption to keep within the percentile. So basically using the T values most of the time against unless undefined is inputted.
	h) OOPS, DRY principle are used whereever possible in a pythonic way.
	
What could have been better:
       Well !!!! lot of things but within the expected time frame I couldnt do much.;-(
	a) Metrics are inconsisent, might be better to implemented with better algorithm like using some Sampling methods.
	b) It would have been better to store survey details and used it for future.
	c) Improve exception handling.
	d) Unable to do boundary testings. 
	e) Common definitions are missing.
	f) Exception in the sample file is not handled currently ignoring the 'Y' value noticed at last minute.


# Improvements:
	a) Computing on Sampling values with any probability theorms or algorithm in a Metric class should be put in place.
	b) Cardinality of the objects on sampling data would improve the robustness and scalability for the survey if given object is stored better according to the real functionality requirement.
	c) Stated with BDD or TDD implementation for the given problem but discontinued.
	

# Test Cases:
	a) CSVFilereader class
	b) ProbabilityRecord Class
	c) BooleanFactor Class
	d) missing TODO RawInputCommand


# Instructions to install, configure, and to run the programs


# Install python 2.7

# Configure:
untar the given file you should see the below files.
	prototype_test
		----> main.py
		----> testsuite.py
		----> Readme.txt
		----> trialsurvey.csv
		----> trialsurvey  
			  ------> __init__.py
			  ------> prob_trail.py
			  ------> csv_file_process.py
			  ------> ra_input.py
			 -------> commondef.py
			 -------> metric_stats.py

# Run:
#	python main.py  ---> to run the simple survey
#	python testsuite.py  --> to run the simple test


