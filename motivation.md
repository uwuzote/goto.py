# Motivation

Let's say we have following code:
```python
for i in range(2, 10):
    print(f"{i}: Hello, World!")

print("Done!")
```
But we want to be chads and
write our code in more chad way:

```python
i = 2;

while i < 10:
    print(f"{i}: Hello, World!")

    i += 1

print("Done!")
```

But the most chad way to do
so is using goto syntax:
```python
label init:
    i = 2
label loop:
    goto out, i <= 10 # Conditional jump
    print(f"{i}: Hello, World!")
    i += 1
    goto loop
label out:
    print("Done!")
```

Unfortunately, python doesn't support
goto syntax natively

But you can mimic it easily:
```python
from goto import label, goto;

@label
def init():
    global i;
    i = 2;
@label
def loop():
    global i;
    raise goto("out", i >= 10);

    print(f"{i}: Hello, World!");
    i += 1;

    raise goto("loop");
@label
def out():
    print("Done!");
```
