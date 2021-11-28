import pickle
def save_v(v,filename):
  f=open(filename,'wb')
  pickle.dump(v,f)
  f.close()
  return filename
 
def load_v(filename):
  with open(filename,'rb') as t:
      r=pickle.load(t)
  return r