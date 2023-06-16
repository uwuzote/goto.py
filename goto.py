class UnknownLabelException(Exception): pass;

class Goto(BaseException):
    __slots__ = ("label", );

    def __init__(self, label: str):
        self.label = label;

goto = Goto;
del Goto;

class Labeller():
    __slots__ = ("__blocks", "__pending", );
    
    def __init__(self):
        self.__blocks = [];
        self.__pending = None;

    def __call__(self, fn):
        label = fn.__name__;
        block = (label, fn);

        self.__blocks.append(block);

        if(self.__pending is None or self.__pending == label):
            self.__pending = None;
            self.__execute(block);

        else:
            pass;

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
        except goto as goto_:
            return goto_.label;
        else:
            return None;

    def __del__(self):
        if(self.__pending is not None):
            raise UnknownLabelException(
                f"Unknown label: {self.__pending !r}"
            );

label = Labeller();
del Labeller;

__all__ = ("label", "goto", "UnknownLabelException", );
        