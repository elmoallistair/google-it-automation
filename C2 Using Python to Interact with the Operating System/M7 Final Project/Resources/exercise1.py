#!/usr/bin/env python3

import re

line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
# Output: <_sre.SRE_Match object; span=(29, 57), match='ticky: INFO: Created ticket '>

line = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"
re.search(r"ticky: ERROR: ([\w ]*) ", line)
# Output: <_sre.SRE_Match object; span=(29, 65), match='ticky: ERROR: Error creating ticket '>