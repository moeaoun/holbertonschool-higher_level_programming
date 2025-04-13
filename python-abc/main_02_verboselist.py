#!/usr/bin/env python3
from task_02_verboselist import VerboseList

vl = VerboseList([1, 2, 3])
vl.append(4)         # ➜ Added [4] to the list.
vl.extend([5, 6])    # ➜ Extended the list with [2] items.
vl.remove(2)         # ➜ Removed [2] from the list.
vl.pop()             # ➜ Popped [6] from the list.
vl.pop(0)            # ➜ Popped [1] from the list.

