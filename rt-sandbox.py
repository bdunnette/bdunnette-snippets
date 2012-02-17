import sys
import logging

from rtkit.resource import RTResource
from rtkit.authenticators import BasicAuthenticator
from rtkit.errors import RTResourceError
from rtkit import set_logging

set_logging('debug')
logger = logging.getLogger('rtkit')

resource = RTResource('http://rt.cla.umn.edu/REST/1.0/', sys.argv[1], sys.argv[2], BasicAuthenticator)

try:
    response = resource.get(path='search/ticket?query=Owner=%s&user=%s&pass=%s' % (sys.argv[1], sys.argv[1], sys.argv[2]))
    for r in response.parsed:
	for t in r:
            logger.info(t)

except RTResourceError as e:
    logger.error(e.response.status_int)
    logger.error(e.response.status)
    logger.error(e.response.parsed)
