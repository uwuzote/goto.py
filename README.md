# `goto.py`

## For chads

Have you ever felt anger, because
you have to write in soy languages,
not chad c?

Now you can cope with it, introducing
`goto` syntax in Python programming language:

```python
from goto import *;

@label
def init():
    global i;
    i = 0;
@label
def loop():
    global i;
    print("%d: Hello, World!" % i);
    i = i + 1;
    goto("loop", i <= 10);
@label
def end():
    print("Done!");
```

---

For motivation see [`./motivation.md`](./motivation.md).

For examples see [`./example-complex-loop.py`](./example-complex-loop.py),
[`./example-example-nonexistent-label.py`](./example-nonexistent-label.py).

---

Thanks [@Tsoding](https://github.com/tsoding) for inspiration.

For real-world use consider other implementations
of goto in Python:
 * [python-goto by snoack](https://github.com/snoack/python-goto),
 * [goto for Python by Richie Hindle](http://entrian.com/goto/).