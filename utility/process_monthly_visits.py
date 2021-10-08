from collections import defaultdict
import os

def process():
  path = os.path.realpath(__file__)
  dir = os.path.dirname(path)
  dir = dir.replace('utility','data')
  os.chdir(dir)
  f = open('total_tourists_by_year.csv','r')
  yearly_total = defaultdict(lambda: 0)
  l = f.readline()
  while l:
    d, c = l.strip().split(',')
    y = d.split('-')[-1]
    yearly_total[y] += int(c)
    l = f.readline()
  f.close()
  f = open('total_tourists_by_year.csv','r')
  l = f.readline()
  out = []
  while l:
    d, c = l.strip().split(',')
    m, y = d.split('-')
    out.append([m, y, int(c)/(yearly_total[y])])
    l = f.readline()

  f = open('monthly_visits_output.csv','w')
  f.write('month,year,yearfrac\n')
  for m, y, c in out:
    f.write(m + ',' + y+ ',' + str(c)+'\n')
  f.close()

if __name__ == "__main__":
  process()