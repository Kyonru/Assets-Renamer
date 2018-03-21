import commands
a = commands.getstatusoutput('ls -l | grep ^- | wc -l')

if (int(a[1]) == 6):
    print 'Nice job!'
else:
    raise Exception('Please, try again')