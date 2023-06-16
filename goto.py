class UnknownLabelException(Exception):
    """
    `goto("non-existent_label")` was called.
    """
    __slots__ = ();

    pass;

class Goto(BaseException):
    """
    Consider using `goto` (notice
    the lowercase) instead.

    Requested jump to other block.
    Can only be used in blocks.

    It is actually a exception which
    need to be raised. 
    """
    __slots__ = ("label", );

    def __init__(self, label: str):
        assert(isinstance(label, str));
        self.label = label;

class Labeller():
    """
    Consider using pre-initialised instance `label`.
    
    Singleton. Use as decorator on blocks:
    ```python
    @label
    def loop():
        print("I am true Chad");
        goto("loop");
    ```

    When this object is garbage-collected, it
    checks if there were jumps to non-existent labels.
    """
    __slots__ = ("__blocks", "__pending", );
    
    def __init__(self):
        self.__blocks = [];
        self.__pending = None;

    """
    Use as decorator.
    """
    def __call__(self, fn):
        label = fn.__name__;
        block = (label, fn);

        self.__blocks.append(block);

        if(self.__pending is None or self.__pending == label):
            self.__pending = None;
            self.__execute(block);

        return fn;

    def __execute(self, block):
        while True:
            res = self.__execute_fn(block[1]);

            if(res is None):
                next = self.__find_next(block[0]);

                if(next is not None):
                    block = next;
                else:
                    return;
            else:
                next = self.__find(res);

                if(next is not None):
                    block = next;
                else:
                    self.__pending = res;
                    return;

    def __find_next(self, label: str):
        have_found = False;

        for block in self.__blocks:
            if(have_found):
                return block;

            if(block[0] == label):
                have_found = True;

        return None;

    def __find(self, label: str):
        for block in self.__blocks:
            if(block[0] == label):
                return block;

        return None

    @staticmethod
    def __execute_fn(fn):
        try:
            fn();
        except Goto as goto:
            return goto.label;
        else:
            return None;

    """
    Checks if there were jumps to non-existent labels
    """
    def __del__(self):
        if(self.__pending is not None):
            raise UnknownLabelException(
                "Requested jump to non-existent "
                f"label, {self.__pending !r}"
            );

label = Labeller();

def goto(label: str):
    """
    Jump to other block. Can only be used
    in blocks.
    """
    raise Goto(label);

__all__ = ("label", "goto", );
