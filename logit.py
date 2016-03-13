import logging

def logging_test():
	logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s  %(levelname)s %(message)s',
                    filename='example.log')
	byte_string = '\xc3\xb4'
	unicode_string = "\xc3\xb4"
	logging.debug(': Starting to send Emails.')
	logging.info(': Sending Email to test@screenmagic.com.'+unicode_string)
	logging.warning(': Things don\'t seem going well.')
	logging.error(': Email to test@screenmagic.com failed.\n')

if __name__ == "__main__":
    logging_test()