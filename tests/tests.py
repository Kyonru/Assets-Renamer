import commands
a = commands.getstatusoutput('ls -l | grep ^- | wc -l')

if (int(a[1]) == 10):
    print 'Nice job!'
else:
    raise Exception('Please, try again')