"""
For the latest version of this file, visit https://github.com/carlsapp/programming-languages/.

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

CLASS_NAME = "SuperObject"  # We could use self.__class__.__name__, but then we would mess up the flow


# The name (SuperObject) appears under the attribute SuperObject.__name__
# You can access the SuperObject class object at super_object_instance.__class__
class SuperObject(object):  # Try replacing object with something else, like int, and see how the functions are called
    """This is the string in triple quotes directly below the class name. After instantiating an object, this string
    is available in the .__doc__ attribute and also accessible when doing help(super_object_instance)."""
    # Instance Creation
    def __new__(cls, *args, **kwargs):
        logger.debug("%s.__new__(cls=%s, args=%s, kwargs=%s)" % (CLASS_NAME, cls, args, kwargs))
        return SuperObject.__base__.__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        logger.debug("%s.__init__(args=%s, kwargs=%s)" % (CLASS_NAME, args, kwargs))
        super(SuperObject, self).__init__(*args, **kwargs)

    def __del__(self):
        logger.debug("%s.__del__()" % CLASS_NAME)
        super(SuperObject, self).__del__()

    # Attribute Access https://docs.python.org/3/reference/datamodel.html#customizing-attribute-access
    def __setattr__(self, name, value):
        logger.debug("%s.__setattr__(key='%s', value=%s)" % (CLASS_NAME, name, value))
        return super(SuperObject, self).__setattr__(name, value)

    def __getattr__(self, name):
        logger.debug("%s.__getattr__(name='%s')" % (CLASS_NAME, name))
        # A Python object doesn't implement __getattr__
        return super(SuperObject, self).__getattr__(name)

    def __getattribute__(self, name):
        logger.debug("%s.__getattribute__(name='%s')" % (CLASS_NAME, name))
        # A Python object doesn't implement __getattr__
        return super(SuperObject, self).__getattribute__(name)

    def __delattr__(self, name):
        # This gets called when you execute 'del ObjDataModel().name'
        logger.debug("%s.__delattr__(name='%s')" % (CLASS_NAME, name))
        return super(SuperObject, self).__delattr__(name)

    def __dir__(self):
        logger.debug("%s.__dir__()" % CLASS_NAME)
        # Interestingly, Python doesn't provide a way for you to call the default object __dir__ method if you're
        #  using your own __dir__ function. Check out Objects\object.c:_dir_object() in the Python source code for more
        #  details.
        return []

    # String functions
    def __repr__(self):
        logger.debug("%s.__repr__()" % CLASS_NAME)
        return super(SuperObject, self).__repr__()

    def __str__(self):
        logger.debug("%s.__str__()" % CLASS_NAME)
        return super(SuperObject, self).__str__()

    # Operator Overloads
    def __add__(self, other):
        # Called when doing this: SuperObject + other
        logger.debug("%s.__add__(%s)" % (CLASS_NAME, other))
        return super(SuperObject, self).__add__(other)

    def __sub__(self, other):
        # Called when doing this: SuperObject - other
        logger.debug("%s.__sub__(%s)" % (CLASS_NAME, other))
        return super(SuperObject, self).__sub__(other)

    def __mul__(self, other):
        # Called when doing this: SuperObject * other
        logger.debug("%s.__mul__(%s)" % (CLASS_NAME, other))
        return super(SuperObject, self).__mul__(other)

    def __matmul__(self, other):
        # New in Python 3.5
        # Called when doing this: SuperObject @ other
        logger.debug("%s.__matmul__(%s)" % (CLASS_NAME, other))
        return super(SuperObject, self).__matmul__(other)

    def __truediv__(self, other):
        # New in Python 3
        # Called when doing this: SuperObject / other
        logger.debug("%s.__truediv__(%s)" % (CLASS_NAME, other))
        return super(SuperObject, self).__truediv__(other)

    def __div__(self, other):
        # Deprecated in Python 3, replaced with truediv
        # Called when doing this: SuperObject / other
        logger.debug("%s.__div__(%s)" % (CLASS_NAME, other))
        return super(SuperObject, self).__div__(other)

    def __floordiv__(self, other):
        # Called when doing this: SuperObject // other
        logger.debug("%s.__floordiv__(%s)" % (CLASS_NAME, other))
        return super(SuperObject, self).__floordiv__(other)

    def __mod__(self, other):
        # Called when doing this: SuperObject % other
        logger.debug("%s.__mod__(%s)" % (CLASS_NAME, other))
        return super(SuperObject, self).__mod__(other)

    def __divmod__(self, other):
        # Called when doing this: divmod(SuperObject, other)
        logger.debug("%s.__divmod__(%s)" % (CLASS_NAME, other))
        return super(SuperObject, self).__divmod__(other)

    def __pow__(self, other):
        # Called when doing this: SuperObject ** other
        logger.debug("%s.__pow__(%s)" % (CLASS_NAME, other))
        return super(SuperObject, self).__pow__(other)

    def __lshift__(self, other):
        # Called when doing this: SuperObject << other
        logger.debug("%s.__lshift__(%s)" % (CLASS_NAME, other))
        return super(SuperObject, self).__lshift__(other)

    def __rshift__(self, other):
        # Called when doing this: SuperObject >> other
        logger.debug("%s.__rshift__(%s)" % (CLASS_NAME, other))
        return super(SuperObject, self).__rshift__(other)

    def __and__(self, other):
        # Called when doing this: SuperObject & other
        logger.debug("%s.__and__(%s)" % (CLASS_NAME, other))
        return super(SuperObject, self).__and__(other)

    def __xor__(self, other):
        # Called when doing this: SuperObject ^ other
        logger.debug("%s.__xor__(%s)" % (CLASS_NAME, other))
        return super(SuperObject, self).__xor__(other)

    def __or__(self, other):
        # Called when doing this: SuperObject ^ other
        logger.debug("%s.__or__(%s)" % (CLASS_NAME, other))
        return super(SuperObject, self).__or__(other)


'''
Still To Do:
__call__
__getitem__
__missing__
__setitem__
__delitem__
__iter__
__reversed__
__bytes__
__format__
__hash__
__bool__
__lt__
__le__
__eq__
__ne__
__gt__
__ge__
__get__
__set__
__delete__
__set_name__
__slots__
__init_subclass__
__prepare__
__instancecheck__
__subclasscheck__
__len__
__length_hint__
__contains__
__radd__
__rsub__
__rmul__
__rmatmul__
__rtruediv__
__rfloordiv__
__rmod__
__rdivmod__
__rpow__
__rlshift__
__rrshift__
__rand__
__rxor__
__ror__
__iadd__
__isub__
__imul__
__imatmul__
__itruediv__
__ifloordiv__
__imod__
__ipow__
__ilshift__
__irshift__
__iand__
__ixor__
__ior__
__neg__
__pos__
__abs__
__invert__
__complex__
__int__
__float__
__round__
__index__
__enter__
__exit__
__await__
__aiter__
__anext__
__aenter__
__aexit__
and maybe more ...
'''


def main():
    """In this main(), we will illustrate how the Python data model is called."""
    logger_console_handler.setFormatter(logging.Formatter('  %(message)s'))

    print("Creating a SuperObject instance by executing 'my_super_instance = SuperObject()")
    my_super_instance = SuperObject()

    print("\nSetting an attribute with 'my_super_instance.my_attr = 4'")
    my_super_instance.my_attr = 4

    print("\nAccessing the attribute with 'my_super_instance.my_attr'")
    my_super_instance.my_attr

    print("\nAccessing a non-existent attribute with 'my_super_instance.my_non_existent_attr'")
    try:
        my_super_instance.my_non_existent_attr
    except Exception as e:
        # logger.debug(repr(e))
        pass


if __name__ == "__main__":
    main()