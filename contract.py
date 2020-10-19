"""
Second homework assignment in the course "Python".

Created by Emdin Grigory.
"""


class ContractError(Exception):
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
Any = object()


def contract(arg_types=None, return_type=None, raises=None):
    """
    Check argument types and return type.

    Args:
        arg_types: types for arguments.
        return_type: return type.
        raises: types of exceptions that the function can throw.

    Returns:
        decorator.

    Raises:
            ContractError: types don't match.
    """
    def decorator(func):
        def wrapped(*args, **kwargs):
            if arg_types is not None:
                all_args = args + tuple(kwargs.values())
                if len(all_args) != len(arg_types):
                    raise ContractError
                for step, cur_type in enumerate(arg_types):
                    if cur_type == Any:
                        continue
                    if not isinstance(all_args[step], cur_type):
                        raise ContractError
            try:
                ret = func(*args, **kwargs)
            except Exception as err:
                if isinstance(err, raises):
                    raise err
                else:
                    raise ContractError
            else:
                if return_type is not None:
                    if not (return_type == Any or isinstance(ret, return_type)):
                        raise ContractError
                return ret

        return wrapped

    return decorator
