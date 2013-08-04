#Going through .epk files for Snap!
import sys
import os
import zipfile
import ConfigParser
d_filled = []
extension = sys.argv[1]
config = ConfigParser.ConfigParser()
epk = zipfile.ZipFile('%s.epk' % extension)
epk.extract('%s.py' % extension)
epk.extract('%s.conf' % extension)
config.read('%s.conf' % extension)
os.remove('%s.conf' % extension)
print "%s v%s by %s" % (config.get('info', 'name'),config.get('info', 'version'),config.get('info','author'))

#checking for dependencies
for d in config.get('dependencies', 'dependencies').split(', '):
    try:
        __import__(d)
    except:
        print "Dependency %s not installed." % d
        d_filled.append(False)
    else:
        print "Dependency %s is installed!" % d
        d_filled.append(True)
if all(x == d_filled[0] for x in d_filled):
    print "All dependencies installed."
else:
    print "Please install dependencies before continuing."
    quit()
