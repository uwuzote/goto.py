from goto import label, goto;

@label
def init():
    global n, i;
    n = 0
    i = n
@label
def loop():
    global i;
    goto("end", i >= 10);

    print(i, end = " ");
    i += 1;

    goto("loop");
@label
def end():
    global n, i;

    n -= 1;
    i = n;
    print(f"\n\n :: {n}\n");

    goto("loop");
