import os, sys, traceback
from trialsurvey.csv_file_process import CSVFileReader
from trialsurvey.prob_trail import ProbabilityRecord
from trialsurvey.ra_input import RawInputCommand

def main():
    try:
        filename = 'trialsurvey.csv'
	csvfile = CSVFileReader(filename)
	header_list=csvfile.get_headerlist()
	prob_list = [ProbabilityRecord(value) for value in header_list]
	for iter in csvfile.get_data(csvfile.get_row_count()):
	    for item,value in iter.items():
	        try:
	            prob_list[header_list.index(item)].increment(value)
	        except:
	            pass
        new_record = {}
        metrics = csvfile.get_acceptancerate()
        all_false = True
	for prob_iter in prob_list:
             ra = RawInputCommand()
             answer_value = ra.run_command(prob_iter.get_name(),csvfile.get_acceptancerate(),metrics)
             new_record.update({prob_iter.get_name():answer_value})
	     #TODO need to do a metric class to do more better computational
             metrics += prob_iter.get_metrics_based_on_boolean_fact(answer_value)
             if answer_value=='F' and all_false:
               all_false = True
	     else:
               all_false = False
        if all_false:
           print '+'*100
           print '+'*100
           print 'Based on information provided you will be invited for the Trials'
           print '+'*100
           print '+'*100  
        else:
           print '+'*100
           print '+'*100
           print ("Based on information provided your score for eligibility is around {}%").format(metrics)
           print '+'*100
           print '+'*100

         # also the new candidate record should be added to the existing file which logic is completely missing herel

    except KeyboardInterrupt:
        print "Shutdown requested...exiting"
    except Exception:
        traceback.print_exc(file=sys.stdout)
    finally:
	#TODO how to handle the exception cases which is not currently handled. I should have recalculated the probability as well
	#the logic incase of failure case should be completely different as well.
        # also the new candidate record should be added to the existing file which logic is completely missing here
        sys.exit(0)

if __name__ == "__main__":
    main()

