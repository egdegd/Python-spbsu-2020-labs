"""
Second homework assignment in the course "Python".

Created by Emdin Grigory.
"""


class ContractError(Exception):
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
Any = object


def check_type(arg_type):
    """
    Check whether pair is a argument and type.

    Args:
        arg_type: pair of argument and type.

    Raises:
        ContractError: if argument have other type.
    """
    if not isinstance(arg_type[0], arg_type[1]):
        raise ContractError()


def check_types(args, arg_types):
    """
    Check argument types.

    Args:
        args: arguments.
        arg_types: types.

    Raises:
        ContractError: if arguments have other types.
    """
    if arg_types is not None:
        if len(args) != len(arg_types):
            raise ContractError()
        list(map(check_type, zip(args, arg_types)))


def check_return_type(ret, return_type):
    """
    Check return type.

    Args:
        ret: return value.
        return_type: type of return value.

    Raises:
        ContractError: if return value have other type.
    """
    if return_type is not None:
        if not isinstance(ret, return_type):
            raise ContractError()


def check_raises(func, raises, args):
    """
    Check raises checks raises for the given exception.

    Args:
        func: function that can raise exception.
        raises: possible exception.
        args: args for the function.

    Raises:
        ContractError: if exception is not in raises.
        Exception: if function raise exception.

    Returns:
        function value.
    """
    if raises is not None:
        try:
            return func(*args)
        except Exception as err:
            if isinstance(err, raises):
                raise err
            raise ContractError() from err
    return func(*args)


def contract(arg_types=None, return_type=None, raises=None):
    """
    Check argument types and return type.

    Args:
        arg_types: types for arguments.
        return_type: return type.
        raises: types of exceptions that the function can throw.

    Returns:
        decorator.
    """

    def decorator(func):
        def wrapped(*args):  # noqa: WPS430
            check_types(args, arg_types)
            ret = check_raises(func, raises, args)
            check_return_type(ret, return_type)
            return ret

        return wrapped

    return decorator
