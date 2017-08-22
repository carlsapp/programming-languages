"""
This file contains what we are going to call a Super Object ... an object that implements almost every feature that a
Python object can implement.
"""
import logging

logger = logging.getLogger(__name__)
logger.handlers = []  # Clear any existing handlers
logger_console_handler = logging.StreamHandler()
# If you want to add indentation to your prints, do something like this:
#  logger_console_handler.setFormatter(logging.Formatter('  %(message)s'))
logger.addHandler(logger_console_handler)
logger.setLevel(logging.DEBUG)


class SuperObject(object):  # Try replacing object with something else, like int, and see how the functions are called
    def __init__(self, *args, **kwargs):
        super(SuperObject, self).__init__(*args, **kwargs)

    def __add__(self, other):
        # Called when doing this: SuperObject + other
        logger.debug("SuperObject.__add__(%s)" % str(other))
        return super(SuperObject, self).__add__(other)

    def __sub__(self, other):
        # Called when doing this: SuperObject - other
        logger.debug("SuperObject.__sub__(%s)" % str(other))
        return super(SuperObject, self).__sub__(other)

    def __mul__(self, other):
        # Called when doing this: SuperObject * other
        logger.debug("SuperObject.__mul__(%s)" % str(other))
        return super(SuperObject, self).__mul__(other)

    def __matmul__(self, other):
        # New in Python 3.5
        # Called when doing this: SuperObject @ other
        logger.debug("SuperObject.__matmul__(%s)" % str(other))
        return super(SuperObject, self).__matmul__(other)

    def __truediv__(self, other):
        # New in Python 3
        # Called when doing this: SuperObject / other
        logger.debug("SuperObject.__truediv__(%s)" % str(other))
        return super(SuperObject, self).__truediv__(other)

    def __div__(self, other):
        # Deprecated in Python 3, replaced with truediv
        # Called when doing this: SuperObject / other
        logger.debug("SuperObject.__div__(%s)" % str(other))
        return super(SuperObject, self).__div__(other)

    def __floordiv__(self, other):
        # Called when doing this: SuperObject // other
        logger.debug("SuperObject.__floordiv__(%s)" % str(other))
        return super(SuperObject, self).__floordiv__(other)

    def __mod__(self, other):
        # Called when doing this: SuperObject % other
        logger.debug("SuperObject.__mod__(%s)" % str(other))
        return super(SuperObject, self).__mod__(other)

    def __divmod__(self, other):
        # Called when doing this: divmod(SuperObject, other)
        logger.debug("SuperObject.__divmod__(%s)" % str(other))
        return super(SuperObject, self).__divmod__(other)

    def __pow__(self, other):
        # Called when doing this: SuperObject ** other
        logger.debug("SuperObject.__pow__(%s)" % str(other))
        return super(SuperObject, self).__pow__(other)


'''
Still To Do:
object.__lshift__(self, other)
object.__rshift__(self, other)
object.__and__(self, other)
object.__xor__(self, other)
object.__or__(self, other)
and more ...
'''