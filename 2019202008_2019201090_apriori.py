# -*- coding: utf-8 -*-

import csv
import json
from itertools import combinations
import threading
import math
from multiprocessing.pool import ThreadPool as Pool
import datetime
from apyori import apriori
import matplotlib.pyplot as plt

"""##Transaction Reduction"""

freq_itemset = {}
def gen_tr_freq_itemset(D,sot,minsup):
  L = []
  C = {}
  total_count = 0
  total_ele = 0
  min_sup = minsup
  for key,value in D.items():
    for j in value:
      count = 0
      for key1,value1 in D.items():
        if j in value1:
          count = count+1
      temp = [j]
      C[json.dumps(temp)] = count
      
  for k,v in C.items():
    support = C[k]/len(D.keys())
    if support >= min_sup:
      L.append(json.loads(k))

  k = 2
  while True:
    if len(L) == 0:
      break
    for i,j in sot.items():
      if sot[i] <= k-1:
        del D[i]
    freq = []
    in_freq = []
    for i,j in C.items():
      lst = json.loads(i)
      if lst in L:
        for ele in lst:
          freq.append(ele)
      else:
        for ele in lst:
          in_freq.append(ele)

    diff_list = list(list(set(in_freq)-set(freq)))
    for ele in diff_list:
      for key,value in D.items():
        if ele in value:
          value.remove(ele)

    sot = {}
    for key,value in D.items():
      sot[key] = len(value)
    temp_L = []
    for i in range(len(L)):
      for j in range(i+1,len(L)):
        mismatch = 0
        for index in range(k-1):
          if k-1 > 0 and L[i][index] != L[j][index]:
            mismatch += 1
        if mismatch <= 1:
          u_list = list(set().union(L[i],L[j]))
          comb = list(combinations(u_list,k-1))
          flag = 0
          for element in comb:
            t_ele = sorted(list(element))
            if t_ele not in L:
              flag = 1
              break
          if flag == 0:
            temp_L.append(u_list)
    C_old = C.copy()
    L_old = L.copy()
  
    for element in L_old:
      ele = json.dumps(element)
      if ele in freq_itemset:
        freq_itemset[ele] += C_old[ele]
      else:
        freq_itemset[ele] = C_old[ele]

    C= {}
    L = []
    for i in temp_L:
      count = 0
      for key,value in D.items():
        if (set(i).issubset(set(value))):
          count += 1
      C[json.dumps(sorted(i))] = count
    
    for key,value in C.items():
      support = C[key]/len(D.keys())
      if support >= min_sup:
        L.append(sorted(json.loads(key)))
    k += 1

"""##Sign

**0.9**
"""

D = {}
sot = {}
min_sup = 0.9
with open('/content/data/sign.txt', 'r') as f:
    reader = csv.reader(f)
    index = 0
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()
        sot[str(index)] = len(temp)
        D[str(index)] = temp
        index += 1
start = datetime.datetime.now()
total_ele = len(D.keys())
gen_tr_freq_itemset(D,sot,min_sup)
end = datetime.datetime.now()
diff = end - start
freq = []
for key,value in freq_itemset.items():
  support = freq_itemset[key]/total_ele
  if support >= min_sup:
    freq.append(json.loads(key))
print(freq)
print(diff.total_seconds()/60.0)

"""**0.8**"""

D = {}
sot = {}
min_sup = 0.8
with open('/content/data/sign.txt', 'r') as f:
    reader = csv.reader(f)
    index = 0
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()
        sot[str(index)] = len(temp)
        D[str(index)] = temp
        index += 1
start = datetime.datetime.now()
total_ele = len(D.keys())
gen_tr_freq_itemset(D,sot,min_sup)
end = datetime.datetime.now()
diff = end - start
freq = []
for key,value in freq_itemset.items():
  support = freq_itemset[key]/total_ele
  if support >= min_sup:
    freq.append(json.loads(key))
print(freq)
print(diff.total_seconds()/60.0)

"""**0.7**"""

D = {}
sot = {}
min_sup = 0.7
with open('/content/data/sign.txt', 'r') as f:
    reader = csv.reader(f)
    index = 0
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()
        sot[str(index)] = len(temp)
        D[str(index)] = temp
        index += 1
start = datetime.datetime.now()
total_ele = len(D.keys())
gen_tr_freq_itemset(D,sot,min_sup)
end = datetime.datetime.now()
diff = end - start
freq = []
for key,value in freq_itemset.items():
  support = freq_itemset[key]/total_ele
  if support >= min_sup:
    freq.append(json.loads(key))
print(freq)
print(diff.total_seconds()/60.0)

"""##Leviathan

**0.7**
"""

D = {}
sot = {}
min_sup = 0.7
with open('/content/data/Leviathan.txt', 'r') as f:
    reader = csv.reader(f)
    index = 0
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()
        sot[str(index)] = len(temp)
        D[str(index)] = temp
        index += 1
start = datetime.datetime.now()
total_ele = len(D.keys())
gen_tr_freq_itemset(D,sot,min_sup)
end = datetime.datetime.now()
diff = end - start
freq = []
for key,value in freq_itemset.items():
  support = freq_itemset[key]/total_ele
  if support >= min_sup:
    freq.append(json.loads(key))
print(freq)
print(diff.total_seconds()/60.0)

"""**0.6**"""

D = {}
sot = {}
min_sup = 0.6
with open('/content/data/Leviathan.txt', 'r') as f:
    reader = csv.reader(f)
    index = 0
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()
        sot[str(index)] = len(temp)
        D[str(index)] = temp
        index += 1
start = datetime.datetime.now()
total_ele = len(D.keys())
gen_tr_freq_itemset(D,sot,min_sup)
end = datetime.datetime.now()
diff = end - start
freq = []
for key,value in freq_itemset.items():
  support = freq_itemset[key]/total_ele
  if support >= min_sup:
    freq.append(json.loads(key))
print(freq)
print(diff.total_seconds()/60.0)

"""**0.5**"""

D = {}
sot = {}
min_sup = 0.5
with open('/content/data/Leviathan.txt', 'r') as f:
    reader = csv.reader(f)
    index = 0
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()
        sot[str(index)] = len(temp)
        D[str(index)] = temp
        index += 1
start = datetime.datetime.now()
total_ele = len(D.keys())
gen_tr_freq_itemset(D,sot,min_sup)
end = datetime.datetime.now()
diff = end - start
freq = []
for key,value in freq_itemset.items():
  support = freq_itemset[key]/total_ele
  if support >= min_sup:
    freq.append(json.loads(key))
print(freq)
print(diff.total_seconds()/60.0)

"""##Partitioning"""

freq_itemset_p = {}
def gen_next_comb(L,k):
  for i in range(len(L)):
    for j in range(i+1,len(L)):
      mismatch = 0
      for index in range(len(L[i])):
        if L[i][index] != L[j][index]:
          mismatch += 1
      if mismatch <= 1:
        u_list = list(set().union(L[i],L[j]))
        comb = list(combinations(u_list,k-1))
        flag = 0
        for element in comb:
          t_ele = sorted(list(element))
          if t_ele not in L:
            flag = 1
            break
        if flag == 0:
          yield u_list

def gen_freq_itemset(partition,minsup):
  min_count = minsup
  
  D = partition.copy()
  L = []
  C = {}
  total_count = 0
  total_ele = 0
  for value in D:
    for j in value:
      count = 0
      for value1 in D:
        if j in value1:
          count = count+1
      temp = [j]
      C[json.dumps(temp)] = count
  for k,v in C.items():
    support = C[k]/len(partition)
    if support >= min_count:
      t = json.loads(k)
      L.append(t)

  k = 2
  while True:
    if len(L) == 0:
      break

    C_old = C.copy()
    L_old = L.copy()

    for key in L_old:
        ele = json.dumps(key)
        if ele in freq_itemset_p:
          freq_itemset_p[ele] += C_old[ele]
        else:
          freq_itemset_p[ele] = C_old[ele]
    C= {}
    L = []
    for i in gen_next_comb(L_old,k):
      count = 0
      for value in D:
        if (set(i).issubset(set(value))):
          count += 1
      C[json.dumps(sorted(i))] = count
    
    for key,value in C.items():
      support = C[key]/len(partition)
      if C[key] >= min_count:
        L.append(sorted(json.loads(key)))

    k += 1

"""##Sign

**0.9**
"""

itemset = []
with open('/content/data/sign.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()
        itemset.append(temp)

global_min_sup = 0.9
total_partition = 5
global_min_count = int(len(itemset)/total_partition)

time_period = []
if total_partition == math.ceil(total_partition):
  for i in range(total_partition):
    start = i*global_min_count
    end = start + global_min_count
    if end > len(itemset):
      end = len(itemset)
    partition  = itemset[start:end].copy()
    st = datetime.datetime.now()
    temp_min_sup = (((len(itemset)*global_min_sup))/total_partition)/float(len(partition))
    gen_freq_itemset(partition,temp_min_sup)
    et = datetime.datetime.now()
    diff = et-st
    time_period.append(diff.total_seconds()/60.0)
else:
  total_partition = math.ceil(total_partition)
  for i in range(total_partition):
    start = i*global_min_count
    end = start + global_min_count
    if end > len(itemset):
      end = len(itemset)
    partition  = itemset[start:end].copy()
    st = datetime.datetime.now()
    temp_min_sup = (((len(itemset)*global_min_sup))/total_partition)/float(len(partition))
    gen_freq_itemset(partition,temp_min_sup)
    et = datetime.datetime.now()
    diff = et-st
    time_period.append(diff.total_seconds()/60.0)

time_period

max(time_period)

"""**0.8**"""

itemset = []
with open('/content/data/sign.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()
        itemset.append(temp)

global_min_sup = 0.8
total_partition = 5
global_min_count = int(len(itemset)/total_partition)

time_period = []
if total_partition == math.ceil(total_partition):
  for i in range(total_partition):
    start = i*global_min_count
    end = start + global_min_count
    if end > len(itemset):
      end = len(itemset)
    partition  = itemset[start:end].copy()
    st = datetime.datetime.now()
    temp_min_sup = (((len(itemset)*global_min_sup))/total_partition)/float(len(partition))
    gen_freq_itemset(partition,temp_min_sup)
    et = datetime.datetime.now()
    diff = et-st
    time_period.append(diff.total_seconds()/60.0)
else:
  total_partition = math.ceil(total_partition)
  for i in range(total_partition):
    start = i*global_min_count
    end = start + global_min_count
    if end > len(itemset):
      end = len(itemset)
    partition  = itemset[start:end].copy()
    st = datetime.datetime.now()
    temp_min_sup = (((len(itemset)*global_min_sup))/total_partition)/float(len(partition))
    gen_freq_itemset(partition,temp_min_sup)
    et = datetime.datetime.now()
    diff = et-st
    time_period.append(diff.total_seconds()/60.0)

time_period

max(time_period)

"""**0.7**"""

itemset = []
with open('/content/data/sign.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()
        itemset.append(temp)

global_min_sup = 0.7
total_partition = 5
global_min_count = int(len(itemset)/total_partition)

time_period = []
if total_partition == math.ceil(total_partition):
  for i in range(total_partition):
    start = i*global_min_count
    end = start + global_min_count
    if end > len(itemset):
      end = len(itemset)
    partition  = itemset[start:end].copy()
    st = datetime.datetime.now()
    temp_min_sup = (((len(itemset)*global_min_sup))/total_partition)/float(len(partition))
    gen_freq_itemset(partition,temp_min_sup)
    et = datetime.datetime.now()
    diff = et-st
    time_period.append(diff.total_seconds()/60.0)
else:
  total_partition = math.ceil(total_partition)
  for i in range(total_partition):
    start = i*global_min_count
    end = start + global_min_count
    if end > len(itemset):
      end = len(itemset)
    partition  = itemset[start:end].copy()
    st = datetime.datetime.now()
    temp_min_sup = (((len(itemset)*global_min_sup))/total_partition)/float(len(partition))
    gen_freq_itemset(partition,temp_min_sup)
    et = datetime.datetime.now()
    diff = et-st
    time_period.append(diff.total_seconds()/60.0)

time_period

max(time_period)

"""##Leviathan

**0.7**
"""

itemset = []
with open('/content/data/Leviathan.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()
        itemset.append(temp)

global_min_sup = 0.7
total_partition = 10
global_min_count = int(len(itemset)/total_partition)

time_period = []
if total_partition == math.ceil(total_partition):
  for i in range(total_partition):
    start = i*global_min_count
    end = start + global_min_count
    if end > len(itemset):
      end = len(itemset)
    partition  = itemset[start:end].copy()
    st = datetime.datetime.now()
    temp_min_sup = (((len(itemset)*global_min_sup))/total_partition)/float(len(partition))
    gen_freq_itemset(partition,temp_min_sup)
    et = datetime.datetime.now()
    diff = et-st
    time_period.append(diff.total_seconds()/60.0)
else:
  total_partition = math.ceil(total_partition)
  for i in range(total_partition):
    start = i*global_min_count
    end = start + global_min_count
    if end > len(itemset):
      end = len(itemset)
    partition  = itemset[start:end].copy()
    st = datetime.datetime.now()
    temp_min_sup = (((len(itemset)*global_min_sup))/total_partition)/float(len(partition))
    gen_freq_itemset(partition,temp_min_sup)
    et = datetime.datetime.now()
    diff = et-st
    time_period.append(diff.total_seconds()/60.0)

time_period

max(time_period)

"""**0.6**"""

itemset = []
with open('/content/data/Leviathan.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()
        itemset.append(temp)

global_min_sup = 0.6
total_partition = 10
global_min_count = int(len(itemset)/total_partition)

time_period = []
if total_partition == math.ceil(total_partition):
  for i in range(total_partition):
    start = i*global_min_count
    end = start + global_min_count
    if end > len(itemset):
      end = len(itemset)
    partition  = itemset[start:end].copy()
    st = datetime.datetime.now()
    temp_min_sup = (((len(itemset)*global_min_sup))/total_partition)/float(len(partition))
    gen_freq_itemset(partition,temp_min_sup)
    et = datetime.datetime.now()
    diff = et-st
    time_period.append(diff.total_seconds()/60.0)
else:
  total_partition = math.ceil(total_partition)
  for i in range(total_partition):
    start = i*global_min_count
    end = start + global_min_count
    if end > len(itemset):
      end = len(itemset)
    partition  = itemset[start:end].copy()
    st = datetime.datetime.now()
    temp_min_sup = (((len(itemset)*global_min_sup))/total_partition)/float(len(partition))
    gen_freq_itemset(partition,temp_min_sup)
    et = datetime.datetime.now()
    diff = et-st
    time_period.append(diff.total_seconds()/60.0)

time_period

max(time_period)

"""**0.5**"""

itemset = []
with open('/content/data/Leviathan.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()
        itemset.append(temp)

global_min_sup = 0.5
total_partition = 10
global_min_count = int(len(itemset)/total_partition)

time_period = []
if total_partition == math.ceil(total_partition):
  for i in range(total_partition):
    start = i*global_min_count
    end = start + global_min_count
    if end > len(itemset):
      end = len(itemset)
    partition  = itemset[start:end].copy()
    st = datetime.datetime.now()
    temp_min_sup = (((len(itemset)*global_min_sup))/total_partition)/float(len(partition))
    gen_freq_itemset(partition,temp_min_sup)
    et = datetime.datetime.now()
    diff = et-st
    time_period.append(diff.total_seconds()/60.0)
else:
  total_partition = math.ceil(total_partition)
  for i in range(total_partition):
    start = i*global_min_count
    end = start + global_min_count
    if end > len(itemset):
      end = len(itemset)
    partition  = itemset[start:end].copy()
    st = datetime.datetime.now()
    temp_min_sup = (((len(itemset)*global_min_sup))/total_partition)/float(len(partition))
    gen_freq_itemset(partition,temp_min_sup)
    et = datetime.datetime.now()
    diff = et-st
    time_period.append(diff.total_seconds()/60.0)

time_period

max(time_period)

"""##Library

##SIgn

0.9
"""

itemset = []
st = datetime.datetime.now()
with open('/content/data/sign.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()
        itemset.append(temp)

a = list(apriori(itemset,min_support=0.9))
end = datetime.datetime.now()
diff = end - st
print(diff.total_seconds()/60.0)

"""**0.8**"""

itemset = []
st = datetime.datetime.now()
with open('/content/data/sign.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()
        itemset.append(temp)

a = list(apriori(itemset,min_support=0.8))
end = datetime.datetime.now()
diff = end - st
print(diff.total_seconds()/60.0)

"""**0.7**"""

itemset = []
st = datetime.datetime.now()
with open('/content/data/sign.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()
        itemset.append(temp)

a = list(apriori(itemset,min_support=0.7))
end = datetime.datetime.now()
diff = end - st
print(diff.total_seconds()/60.0)

"""##Leviathan

**0.7**
"""

itemset = []
st = datetime.datetime.now()
with open('/content/data/Leviathan.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()
        itemset.append(temp)

a = list(apriori(itemset,min_support=0.7))
end = datetime.datetime.now()
diff = end - st
print(diff.total_seconds()/60.0)

"""**0.6**"""

itemset = []
st = datetime.datetime.now()
with open('/content/data/Leviathan.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()
        itemset.append(temp)

a = list(apriori(itemset,min_support=0.6))
end = datetime.datetime.now()
diff = end - st
print(diff.total_seconds()/60.0)

"""**0.5**"""

itemset = []
st = datetime.datetime.now()
with open('/content/data/Leviathan.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()
        itemset.append(temp)

a = list(apriori(itemset,min_support=0.5))
end = datetime.datetime.now()
diff = end - st
print(diff.total_seconds()/60.0)

