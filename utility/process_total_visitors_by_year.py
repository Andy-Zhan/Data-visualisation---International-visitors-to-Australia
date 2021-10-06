from collections import defaultdict
import os

def process():
  path = os.path.realpath(__file__)
  dir = os.path.dirname(path)
  dir = dir.replace('utility','data')
  os.chdir(dir)
  f = open('total_tourists_by_year.csv','r')
  year_dict = defaultdict(lambda: 0)
  l = f.readline().strip()
  while l and len(l):
    d,c=l.split(',')
    year = d.split('-')[1]
    c = int(c)
    year_dict[year] += c
    l = f.readline()
  f.close()

  f = open('total_tourists_by_year_output.csv','w')
  for key, value in year_dict.items():
    f.write(key + ',' + str(value)+'\n')
  f.close()

if __name__ == "__main__":
  process()