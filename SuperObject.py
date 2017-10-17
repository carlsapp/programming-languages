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


def create_super_object_class(base_class=int):
    """
    Creates a class object that's a SuperObject with base_class as the base class. Allows you to add Python data model
    logging to any base class.
    :param base_class: The class to use as the base class. Needs to be a class object.
    :return: A SuperObject class with base_class as the base.
    """
    CLASS_NAME = "SuperObject(%s)" % base_class.__name__  # We could use self.__class__.__name__, but then we would mess up the flow

    # The name (SuperObject) appears under the attribute SuperObject.__name__
    # You can access the SuperObject class object at super_object_instance.__class__
    class SuperObject(base_class):  # Try replacing object with something else, like int, and see how the functions are called
        """This is the string in triple quotes directly below the class name. After instantiating an object, this string
        is available in the .__doc__ attribute and also accessible when doing help(super_object_instance)."""
        # Instance Creation and Destruction
        def __new__(cls, *args, **kwargs):
            logger.debug("%s.__new__(cls=%s, args=%s, kwargs=%s)" % (CLASS_NAME, cls, args, kwargs))
            #our_class = type('SuperObject', (base_cls,), dict(cls.__dict__))
            #return base_cls.__new__(our_class, *args, **kwargs)
            return SuperObject.__base__.__new__(cls, *args, **kwargs)

        def __init__(self, *args, **kwargs):
            logger.debug("%s.__init__(args=%s, kwargs=%s)" % (CLASS_NAME, args, kwargs))
            super(SuperObject, self).__init__(*args, **kwargs)

        def __del__(self):
            logger.debug("%s.__del__()" % CLASS_NAME)
            super(SuperObject, self).__del__()

        # Attribute Access
        # https://docs.python.org/3/reference/datamodel.html#customizing-attribute-access
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

        # Attributes needed for built-in functions:
        #     dir()   __dir__
        #     repr()  __repr__
        #     str()   __str__
        #     abs()   __abs__
        #     bool()  __bool__
        #     int()   __int__
        #     float() __float__
        #     complex()  __complex__
        #     round() __round__
        #     divmod() __divmod__ __rdivmod__
        #     isinstance() __instancecheck__
        #     issubclass() __subclasscheck__
        #     len() __len__
        #     reversed() __reversed__
        #     hash() __hash__
        #     format() __format__
        def __dir__(self):
            logger.debug("%s.__dir__()" % CLASS_NAME)
            # Interestingly, Python doesn't provide a way for you to call the default object __dir__ method if you're
            #  using your own __dir__ function. Check out Objects\object.c:_dir_object() in the Python source code for more
            #  details.
            return []

        def __repr__(self):
            logger.debug("%s.__repr__()" % CLASS_NAME)
            return super(SuperObject, self).__repr__()

        def __str__(self):
            logger.debug("%s.__str__()" % CLASS_NAME)
            return super(SuperObject, self).__str__()

        def __abs__(self):
            logger.debug("%s.__abs__()" % CLASS_NAME)
            return super(SuperObject, self).__abs__()

        def __bool__(self):
            logger.debug("%s.__bool__()" % CLASS_NAME)
            return super(SuperObject, self).__bool__()

        def __int__(self):
            logger.debug("%s.__int__()" % CLASS_NAME)
            return super(SuperObject, self).__int__()

        def __float__(self):
            logger.debug("%s.__float__()" % CLASS_NAME)
            return super(SuperObject, self).__float__()

        def __complex__(self):
            logger.debug("%s.__complex__()" % CLASS_NAME)
            return super(SuperObject, self).__complex__()

        def __round__(self):
            logger.debug("%s.__round__()" % CLASS_NAME)
            return super(SuperObject, self).__round__()

        def __divmod__(self, other):
            """Called when doing this: divmod(SuperObject, other)"""
            logger.debug("%s.__divmod__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__divmod__(other)

        def __rdivmod__(self, other):
            """Called when doing this: divmod(other, SuperObject) and other doesn't implement __divmod__"""
            logger.debug("%s.__rdivmod__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__rdivmod__(other)

        def __instancecheck__(self, instance):
            logger.debug("%s.__instancecheck__(%s)" % (CLASS_NAME, instance))
            return super(SuperObject, self).__instancecheck__(instance)

        def __subclasscheck__(self, subclass):
            logger.debug("%s.__subclasscheck__(%s)" % (CLASS_NAME, subclass))
            return super(SuperObject, self).__subclasscheck__(subclass)

        def __len__(self):
            logger.debug("%s.__len__()" % CLASS_NAME)
            return super(SuperObject, self).__len__()

        def __reversed__(self):
            logger.debug("%s.__reversed__()" % CLASS_NAME)
            return super(SuperObject, self).__reversed__()

        def __hash__(self):
            logger.debug("%s.__hash__()" % CLASS_NAME)
            return super(SuperObject, self).__hash__()

        def __format__(self, format_spec):
            logger.debug("%s.__format__(%s)" % (CLASS_NAME, format_spec))
            return super(SuperObject, self).__format__(format_spec)

        # Operator Overloads
        # In Python, we can override all of these operators:
        #   Arithmetic Operators:
        #     +    __add__  __radd__  __pos__
        #     +=   __iadd__
        #     -    __sub__  __rsub__  __neg__
        #     -=   __isub__
        #     *    __mul__  __rmul__
        #     *=   __imul__
        #     **   __pow__  __rpow__
        #     **=  __ipow__
        #     @    __matmul__  __rmatmul__
        #     @=   __imatmul__
        #     /    __div__  __rdiv__
        #     /=   __idiv__
        #     //   __floordiv__  __rfloordiv__
        #     //=  __ifloordiv__
        #     %    __mod__  __rmod__
        #     %=   __imod__
        #   Bitwise Operators:
        #     ~    __invert__
        #     |    __or__  __ror__
        #     |=   __ior__
        #     &    __and__  __rand__
        #     &=   __iand__
        #     ^    __xor__  __rxor__
        #     ^=   __ixor__
        #     <<   __lshift__  __rlshift__
        #     <<=  __ilshift__
        #     >>   __rshift__  __rrshift__
        #     >>=  __irshift__
        #   Comparison Operators:
        #     <    __lt__
        #     <=   __le__
        #     >    __gt__
        #     >=   __ge__
        #     ==   __eq__
        #     !=   __ne__
        #   Array/Item Operators:
        #     []   __getitem__
        #     []=  __setitem__  __missing__  __delitem__
        #   Other Operators:
        #     ()   __call__
        #     in   __contains__
        #
        def __add__(self, other):
            """Called when doing this: SuperObject + other"""
            logger.debug("%s.__add__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__add__(other)

        def __radd__(self, other):
            """Called when doing this: other + SuperObject and other doesn't implement __add__"""
            logger.debug("%s.__radd__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__radd__(other)

        def __pos__(self):
            """Called when doing +SuperObject to make a positive version of SuperObject."""
            logger.debug("%s.__pos__()" % CLASS_NAME)
            return super(SuperObject, self).__pos__()

        def __iadd__(self, other):
            """Called when doing this: SuperObject += other"""
            logger.debug("%s.__iadd__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__iadd__(other)

        def __sub__(self, other):
            """Called when doing this: SuperObject - other"""
            logger.debug("%s.__sub__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__sub__(other)

        def __rsub__(self, other):
            """Called when doing this: other - SuperObject and other doesn't implement __sub__"""
            logger.debug("%s.__rsub__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__rsub__(other)

        def __neg__(self):
            """Called when doing -SuperObject to make a negative version of SuperObject."""
            logger.debug("%s.__neg__()" % CLASS_NAME)
            return super(SuperObject, self).__neg__()

        def __isub__(self, other):
            """Called when doing this: SuperObject -= other"""
            logger.debug("%s.__isub__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__isub__(other)

        def __mul__(self, other):
            """Called when doing this: SuperObject * other"""
            logger.debug("%s.__mul__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__mul__(other)

        def __rmul__(self, other):
            """Called when doing this: other * SuperObject and other doesn't implement __mul__"""
            logger.debug("%s.__rmul__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__rmul__(other)

        def __imul__(self, other):
            """Called when doing this: SuperObject *= other"""
            logger.debug("%s.__imul__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__imul__(other)

        def __pow__(self, other):
            """Called when doing this: SuperObject ** other"""
            logger.debug("%s.__pow__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__pow__(other)

        def __rpow__(self, other):
            """Called when doing this: other ** SuperObject and other doesn't implement __pow__"""
            logger.debug("%s.__rpow__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__rpow__(other)

        def __ipow__(self, other):
            """Called when doing this: SuperObject **= other"""
            logger.debug("%s.__ipow__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__ipow__(other)

        def __matmul__(self, other):
            """
            New in Python 3.5
            Called when doing this: SuperObject @ other
            :param other: The other matrix to multiple against this matrix
            :return: The result of matrix multiplication between this and other
            """
            logger.debug("%s.__matmul__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__matmul__(other)

        def __rmatmul__(self, other):
            """Called when doing this: other @ SuperObject and other doesn't implement __matmul__"""
            logger.debug("%s.__rmatmul__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__rmatmul__(other)

        def __imatmul__(self, other):
            """Called when doing this: SuperObject @= other"""
            logger.debug("%s.__imatmul__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__imatmul__(other)

        def __div__(self, other):
            # Deprecated in Python 3, replaced with truediv
            # Called when doing this: SuperObject / other
            logger.debug("%s.__div__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__div__(other)

        def __rdiv__(self, other):
            """Called when doing this: other / SuperObject and other doesn't implement __div__"""
            logger.debug("%s.__rdiv__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__rdiv__(other)

        def __idiv__(self, other):
            """Called when doing this: SuperObject /= other"""
            logger.debug("%s.__idiv__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__idiv__(other)

        def __truediv__(self, other):
            """
            New in Python 3
            Called when doing this: SuperObject / other
            """
            logger.debug("%s.__truediv__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__truediv__(other)

        def __floordiv__(self, other):
            """Called when doing this: SuperObject // other"""
            logger.debug("%s.__floordiv__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__floordiv__(other)

        def __rfloordiv__(self, other):
            """Called when doing this: other // SuperObject and other doesn't implement __floordiv__"""
            logger.debug("%s.__rfloordiv__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__rfloordiv__(other)

        def __ifloordiv__(self, other):
            """Called when doing this: SuperObject //= other"""
            logger.debug("%s.__ifloordiv__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__ifloordiv__(other)

        def __mod__(self, other):
            # Called when doing this: SuperObject % other
            logger.debug("%s.__mod__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__mod__(other)

        def __rmod__(self, other):
            """Called when doing this: other % SuperObject and other doesn't implement __mod__"""
            logger.debug("%s.__rmod__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__rmod__(other)

        def __imod__(self, other):
            """Called when doing this: SuperObject %= other"""
            logger.debug("%s.__imod__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__imod__(other)

        #   Bitwise Operators:
        #     ~    __invert__
        #     |    __or__  __ror__
        #     |=   __ior__
        #     &    __and__  __rand__
        #     &=   __iand__
        #     ^    __xor__  __rxor__
        #     ^=   __ixor__
        #     <<   __lshift__  __rlshift__
        #     <<=  __ilshift__
        #     >>   __rshift__  __rrshift__
        #     >>=  __irshift__
        def __invert__(self):
            """Called when doing ~SuperObject to invert all of the bits of SuperObject."""
            logger.debug("%s.__invert__()" % CLASS_NAME)
            return super(SuperObject, self).__invert__()

        def __or__(self, other):
            # Called when doing this: SuperObject | other
            logger.debug("%s.__or__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__or__(other)

        def __ror__(self, other):
            # Called when doing this: other | SuperObject and other doesn't implement __or__
            logger.debug("%s.__ror__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__ror__(other)

        def __ior__(self, other):
            # Called when doing this: SuperObject |= other
            logger.debug("%s.__ior__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__ior__(other)

        def __and__(self, other):
            # Called when doing this: SuperObject & other
            logger.debug("%s.__and__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__and__(other)

        def __rand__(self, other):
            # Called when doing this: other & SuperObject and other doesn't implement __and__
            logger.debug("%s.__rand__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__rand__(other)

        def __iand__(self, other):
            # Called when doing this: SuperObject &= other
            logger.debug("%s.__iand__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__iand__(other)

        def __xor__(self, other):
            # Called when doing this: SuperObject ^ other
            logger.debug("%s.__xor__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__xor__(other)

        def __rxor__(self, other):
            # Called when doing this: other ^ SuperObject and other doesn't implement __xor__
            logger.debug("%s.__rxor__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__rxor__(other)

        def __ixor__(self, other):
            # Called when doing this: SuperObject ^= other
            logger.debug("%s.__ixor__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__ixor__(other)

        def __lshift__(self, other):
            # Called when doing this: SuperObject << other
            logger.debug("%s.__lshift__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__lshift__(other)

        def __rlshift__(self, other):
            # Called when doing this: other << SuperObject and other doesn't implement __lshift__
            logger.debug("%s.__rlshift__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__rlshift__(other)

        def __ilshift__(self, other):
            # Called when doing this: SuperObject <<= other
            logger.debug("%s.__ilshift__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__ilshift__(other)

        def __rshift__(self, other):
            # Called when doing this: SuperObject >> other
            logger.debug("%s.__rshift__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__rshift__(other)

        def __rrshift__(self, other):
            # Called when doing this: other >> SuperObject and other doesn't implement __rshift__
            logger.debug("%s.__rrshift__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__rrshift__(other)

        def __irshift__(self, other):
            # Called when doing this: SuperObject >>= other
            logger.debug("%s.__irshift__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__irshift__(other)

        #   Comparison Operators:
        #     <    __lt__
        #     <=   __le__
        #     >    __gt__
        #     >=   __ge__
        #     ==   __eq__
        #     !=   __ne__
        def __lt__(self, other):
            """Called when doing this: SuperObject < other"""
            logger.debug("%s.__lt__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__lt__(other)

        def __le__(self, other):
            """Called when doing this: SuperObject <= other"""
            logger.debug("%s.__le__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__le__(other)

        def __gt__(self, other):
            """Called when doing this: SuperObject > other"""
            logger.debug("%s.__gt__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__gt__(other)

        def __ge__(self, other):
            """Called when doing this: SuperObject >= other"""
            logger.debug("%s.__ge__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__ge__(other)

        def __eq__(self, other):
            """Called when doing this: SuperObject == other"""
            logger.debug("%s.__eq__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__eq__(other)

        def __ne__(self, other):
            """Called when doing this: SuperObject != other"""
            logger.debug("%s.__ne__(%s)" % (CLASS_NAME, other))
            return super(SuperObject, self).__ne__(other)

        #   Array/Item Operators:
        #     []   __getitem__  __missing__
        #     []=  __setitem__  __delitem__
        def __getitem__(self, key):
            """Called when doing this: SuperObject[key]"""
            logger.debug("%s.__getitem__(%s)" % (CLASS_NAME, key))
            return super(SuperObject, self).__getitem__(key)

        def __missing__(self, key):
            """Called when doing this: SuperObject[key] and key doesn't exist"""
            logger.debug("%s.__missing__(%s)" % (CLASS_NAME, key))
            return super(SuperObject, self).__missing__(key)

        def __setitem__(self, key, value):
            """Called when doing this: SuperObject[key] = value"""
            logger.debug("%s.__setitem__(%s, %s)" % (CLASS_NAME, key, value))
            return super(SuperObject, self).__setitem__(key, value)

        def __delitem__(self, key):
            """Called when doing this: del SuperObject[key]"""
            logger.debug("%s.__delitem__(%s)" % (CLASS_NAME, key))
            return super(SuperObject, self).__delitem__(key)

        #   Other Operators:
        #     ()   __call__
        #     in   __contains__
        def __call__(self, *args, **kwargs):
            """Called when doing this: SuperObject(*args, **kwargs)"""
            logger.debug("%s.__call__(args=%s, kwargs=%s)" % (CLASS_NAME, args, kwargs))
            return super(SuperObject, self).__call__(*args, **kwargs)

        def __contains__(self, item):
            """Called when doing this: item in SuperObject"""
            logger.debug("%s.__contains__(%s)" % (CLASS_NAME, item))
            return super(SuperObject, self).__contains__(item)

    return SuperObject

'''
Still To Do:

Descriptors
https://docs.python.org/3/reference/datamodel.html#implementing-descriptors
__get__
__set__
__delete__
__set_name__

With Statement Context Managers
https://docs.python.org/3/reference/datamodel.html#with-statement-context-managers
__enter__
__exit__

Awaitable Objects
https://docs.python.org/3/reference/datamodel.html#awaitable-objects
__await__

Asynchronous Iterators
https://docs.python.org/3/reference/datamodel.html#asynchronous-iterators
__aiter__
__anext__

Asynchronous Context Managers
https://docs.python.org/3/reference/datamodel.html#asynchronous-context-managers
__aenter__
__aexit__

Everything Else:
__slots__
__init_subclass__
__prepare__
__length_hint__
__index__
__iter__
__bytes__
'''


def main():
    """In this main(), we will illustrate how the Python data model is called."""
    logger_console_handler.setFormatter(logging.Formatter('  %(message)s'))

    MySuperObject = create_super_object_class(int)
    print("Creating a SuperObject instance by executing 'my_super_instance = MySuperObject()")
    my_super_instance = MySuperObject()

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
