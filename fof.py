#!/usr/bin/python

# for reference:
# https://github.com/fluxer/kde-workspace/commit/780dc422b1d8794c59cd9eb7a246f0d532d3649f

import sys, time

fofstring = '''\n
\n
Fiction or Fact\n
by\n
Someone V. Bored\n
\n
\n
Episode I\n
\n
Timmy: Hey, Mr. Sudo! I found a gun over there.\n
Can I use it to shoot Bob?\n
\n
Mr. Sudo: Sure, kid.\n
Just give me your last name.\n
\n
Timmy: Thompson! Timmy Thompson!\n
\n
Mr. Sudo: Go on.\n
\n
\n
\n
Episode II\n
Tommy: Hey, Officer! I found a knife over there.\n
Can I use it to stab Donny?\n
\n
Officer: Absolutely.\n
However, I require your first name.\n
Should you not want to tell it to me, tell me your father first name instead.\n
\n
Tommy: Hmm.. Zack Thompson!\n
\n
Officer: Proceed.\n
\n
\n
\n
Cast:\n
Timmy: %s Hacks\n
Tommy: %s Hakz\n
Mr. Sudo: %s\n
Officer: %s\n
''' % (sys.argv[3].capitalize(), sys.argv[3].capitalize(), sys.argv[4], sys.argv[5])

cursescolumns = int(sys.argv[1])
curseslines = int(sys.argv[2])

def printcenter(sstring):
    istringlen = len(sstring)
    print('%s%s' % (' ' * (int(cursescolumns / 2) - int(istringlen / 2)), sstring))

print(' ' * cursescolumns * curseslines)
for sline in fofstring.splitlines():
    printcenter(sline)
    time.sleep(0.5)