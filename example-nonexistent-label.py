from goto import label, goto;

"""
This example shows how goto tracks
jumps to non-existent labels.
This will end with (roughtly):
```
Exception ignored in: <function Labeller.__del__ at 0x000000000000>
Traceback (most recent call last):
  File "/path/to/goto.py", line 000, in __del__
goto.UnknownLabelException: Requested jump to non-existent label: 'nowhere'
```
"""

@label
def leads_to_nowhere():
	goto("nowhere");
