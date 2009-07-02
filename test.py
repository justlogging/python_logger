from justlogging import Justlogging

l = Justlogging("4b87b1a839180ad196cbcaedbeb16c47", 'apache')
if l.log('Woot') == True:
  print 'woot'
else: 
  print 'meh'