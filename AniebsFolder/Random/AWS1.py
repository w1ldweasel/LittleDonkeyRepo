

import json #The JSON module is mainly used to convert the python dictionary above into a JSON string that can be written into a file
import logging #with the logging module imported, you can use something called a “logger” to log messages that you want to see.
import urllib2 #urllib2 is a Python module for fetching URLs (Uniform Resource Locators). It offers a very simple interface, in the form of the urlopen function


#logger is used by most of the third-party Python libraries, so you can integrate your log messages with the ones from those libraries to produce a homogeneous log for your application. 
#With the logging module imported, you can use something called a “logger” to log messages that you want to see.
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#API Key that works with IFTTT to trigger a specific event which is created on the web service
maker_key = '1234567869'#deleted this and replaced with generic numbers as this is my personal API key

#event – AWS Lambda uses this parameter to pass in event data to the handler. This parameter is usually of the Python dict type. It can also be list, str, int, float, or NoneType type.
#context – AWS Lambda uses this parameter to provide runtime information to your handler. This parameter is of the LambdaContext type.
def lambda_handler(event, context):
    #The info() method of a Logger class used to Log an INFO message.This method is used to forward logs to all the registered output
    logger.info('Received event: ' + json.dumps(event)) #dumps() method converts dictionary object of python into JSON string data format
    maker_event = '%s-%s' % (event['serialNumber'], event['clickType']) #
    logger.info('Maker event: ' + maker_event)
    url = 'https://maker.ifttt.com/trigger/%s/with/key/%s' % (maker_event, maker_key)
    #The return value from urlopen() gives access to the headers from the HTTP server through the info() method, and the data for the remote resource via methods like read() and readlines(). 
    #Additionally, the file object that is returned by urlopen() is iterable
    f = urllib2.urlopen(url) 
    #If the end of the file has been reached, f.read() will return an empty string ('')
    response = f.read()
    f.close()
    logger.info('Event has been sent to IFTTT Maker channel')
    return response
