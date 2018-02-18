from typing import Union, Any

_store = {

}


def set_(
        name,
        obj
) -> None:
    _store[name] = obj


def get_(
        name
) -> Union[Any, None]:
    return _store.get(name)