from goto import label, goto;

@label
def init():
    global n, i;
    n = 0
    i = n
@label
def loop():
    global i;

    if(i >= 10):
        print();
        goto("end");

    print(i, end = " ");
    i += 1;

    goto("loop");
@label
def end():
    global n, i;

    n -= 1;
    i = n;
    print(f"\n :: {n}\n");

    goto("loop");
