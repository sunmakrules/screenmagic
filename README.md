ScreenMagic Assignment Solution


logit.py --> generates a log file 'example.log'

create_log.sh --> script to run the 'logit.py' to automate log generation.

parse_log.py --> parses the 'example.log' file and creates 'parsedlog.csv' file in csv format.
		 Also, generates and prints the report.

The log statement format is:<datetime> : <log level> : <log message>

The log file 'example.log' will have DEBUG, INFO, WARNING and ERROR log levels.

The report is of the below format.
Date Errors Warnings
2016-03-13 1236 2650


Advancements:
1. The log messages can have unicode characters also. Your code should be able to handle that.
2. The code will execute correctly even when log file is getting written at run time by some other processes. You can test this by executing 'parse_log.py' while 'create_log.sh' is in execution.


Note:
Execute the code -- python parse_log.py (Python version >=3.0)
Followed pep8 coding standards
No external library has been used.
