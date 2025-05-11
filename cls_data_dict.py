from collections import UserDict

class DataDict(UserDict):
    def __init__(self, *args, _locked=False, _validators=None, **kwargs):
        self._locked = _locked
        self._validators = _validators or {}
        init_data = dict(*args, **kwargs)
        wrapped_data = {k: self._wrap(v) for k, v in init_data.items()}
        super().__init__(wrapped_data)

    def _wrap(self, value):
        if isinstance(value, dict):
            return DataDict(value, _locked=self._locked, _validators=self._validators)
        elif isinstance(value, list):
            return [self._wrap(v) for v in value]
        else:
            return value

    def _unwrap(self, value):
        if isinstance(value, DataDict):
            return value.to_dict()
        elif isinstance(value, list):
            return [self._unwrap(v) for v in value]
        else:
            return value

    def __setitem__(self, key, value):
        if self._locked:
            raise TypeError("This DataDict is immutable.")
        if key in self._validators:
            if not self._validators[key](value):
                raise ValueError(f"Validation failed for key: {key}")
        super().__setitem__(key, self._wrap(value))

    def __setattr__(self, name, value):
        if name in {'data', '_locked', '_validators'}:
            super().__setattr__(name, value)
        else:
            self[name] = value

    def __getattr__(self, name):
        try:
            return self.data[name]
        except KeyError:
            raise AttributeError(f"'DataDict' object has no attribute '{name}'")

    def __dir__(self):
        return list(self.data.keys()) + list(super().__dir__())

    def to_dict(self):
        return {k: self._unwrap(v) for k, v in self.data.items()}

    def get_path(self, path, default=None, sep='.'):
        parts = path.split(sep)
        current = self
        for part in parts:
            try:
                current = current[part]
            except (KeyError, TypeError):
                return default
        return current

    def set_path(self, path, value, sep='.'):
        if self._locked:
            raise TypeError("This DataDict is immutable.")
        parts = path.split(sep)
        current = self
        for part in parts[:-1]:
            if part not in current or not isinstance(current[part], DataDict):
                current[part] = DataDict(_locked=self._locked, _validators=self._validators)
            current = current[part]
        current[parts[-1]] = value

    def lock(self):
        self._locked = True
        for value in self.data.values():
            if isinstance(value, DataDict):
                value.lock()

    def unlock(self):
        self._locked = False
        for value in self.data.values():
            if isinstance(value, DataDict):
                value.unlock()
