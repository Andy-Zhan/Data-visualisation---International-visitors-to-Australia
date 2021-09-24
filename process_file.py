def process():
  f = open("short_term_visitors.csv", "r")
  line = f.readline().replace('\"','')
  countries = [l.split(";")[1].strip() for l in line.strip().split(";,")]
  data_in = []
  data_out = []
  line = f.readline()
  while line:
    line = line.strip().split(',')
    data_in.append(line)
    line = f.readline()
  f.close()
  by_year = []
  year = data_in[0][0].split('-')[1]
  years = [year]
  sums = [0]*(len(data_in[0])-1)
  for row in data_in:
    y = row[0].split('-')[1]
    if y != year:
      years.append(y)
      by_year.append(sums)
      year = y
      sums = [0]*(len(row)-1)
    for i in range(1, len(row)):
      sums[i-1] += int(row[i])
  by_year.append(sums)
  for i in range(len(years)):
    for j in range(len(countries)):
      data_out.append([years[i], countries[j], str(by_year[i][j])])
  f = open('short_term_visitors_output.csv', 'w')
  for l in data_out:
    if "Total" not in ','.join(l):
      f.write(','.join(l)+'\n')
  f.close()
  return

def process_2():
  f = open("short_term_visitors_output.csv", "r")
  line = f.readline()
  line = f.readline().strip().split(',')
  m = 0
  while line:
    print(line)
    if len(line) == 3:
      c = int(line[2])
      if c > m: m = c
    else:
      break
    line = f.readline().strip().split(',')
  print(m)
  f.close()


if __name__ == "__main__":
  #process()
  process_2()