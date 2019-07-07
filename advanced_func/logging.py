# Some practise Logging with files
#
# Quick side note about loggers: 
# #     - Everytime running this code the new logging appending to .txt
# #     i. PRO: if logging info starts upon a crash you can track
# #     ii. CON: text file can grow large if appending info regularly.

import logging
filename='log.txt'
'''
DEBUG
INFO
WARNING
ERROR
CRITICAL
'''
# By default loggers are configured to WARNING level
logger = logging.getLogger('books')

# Default logger level is to Warning 
logger.info("I'm hidden!")
logger.warning("But this will.")

# Format the logger 
logging.basicConfig(
                    format="%(asctime)s  %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s", 
                    datefmt= "%m-%d-%Y %H:%M:%S",
                    level=logging.DEBUG, 
                    filename=filename   )

# Retry and see all messages
logger.debug("Now you may see me!")
logger.info("This will.")
logger.warning("Me too")
logger.error("Same")
logger.critical("I obviously do. Im the most prioritized.")

logger = logging.getLogger('books.database')
