from collections import defaultdict
import os

def process():
  path = os.path.realpath(__file__)
  dir = os.path.dirname(path)
  dir = dir.replace('utility','data')
  os.chdir(dir)
  f = open('reasons_for_visiting.csv','r')
  headers=f.readline().strip().split(',')[1:-1]
  year_dict = defaultdict(lambda: [0]*len(headers))
  l = f.readline().strip()
  while l and len(l):
    l=l.split(',')
    year, l = l[0].split('-')[1], l[1:]
    for i, c in enumerate(l):
      if c == '': continue
      c = int(c)
      year_dict[year][i] += c
    l = f.readline().strip()
  f.close()

  f = open('reasons_for_visiting_output.csv','w')
  for key, value in year_dict.items():
    for i, c in enumerate(value):
      f.write(key + ',' + headers[i] + ',' + str(c)+'\n')
  f.close()

if __name__ == "__main__":
  process()