def main():
  import shelve

  s = shelve.open('drows.db')

  try:
  
    s['0'] = {1:'foo',2:'bar',3:'Lumberjack'}
    s['Hello']={'foo':'Hello','bar':'World','Lumberjack':'?'}
    s['Spam']= {'foo':'Spam','bar':'Eggs','Lumberjack':'?'}
  finally:
    s.close()

  s = shelve.open('drows.db')

  fargs = {}
  for item in s['0']:
    fname = s['0'][item]
  if fname in globals():
    fargs[fname] = {}
    from inspect import signature, _empty
    sig = signature(eval(fname))
    print("%s is a function with arguments %s" % (fname, sig))
    for param in sig.parameters.values():
      pname = param.name
      pdefault = param.default

      if pdefault is _empty:
	print('Requires parameter: %s %s' % (fname, pname))
      else: 
	fargs[fname][pname] = pdefault
	print('I have default value for: %s %s %s' % (fname, pname, pdefault))
  print(fargs)
  for item in s:
    if item != '0':
       print("%s: %s" % (item, s[item]))

def delrow(s, rowkey):
  try:
    del s[rowkey]
  except:
    pass
 
def Lumberjack(job, play='', status='Okay'):
  return "I'm okay"

