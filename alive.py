import requests, time
import logging
import datetime

logging.basicConfig(filename='ltshdownlog', level=logging.DEBUG, format='%(message)s')
u = 'http://www.ltsh.ilc.edu.tw'
while True:
  time.sleep(60)
  s = requests.Session()
  beg = time.time()
  try:
    res = s.get(u, timeout=5)
    print('alive : %s'%datetime.datetime.now().isoformat().split('.')[0].replace('T', ','))
    logging.info('alive : %s s'%datetime.datetime.now().isoformat().split('.')[0].replace('T', ','))
    
  except:
    if str(time.time()-beg)[:4] != '0.00':
      print('Turn down 4 what?? : %s'%datetime.datetime.now().isoformat().split('.')[0].replace('T', ','))
      logging.info('Turn down 4 what?? : %s s'%datetime.datetime.now().isoformat().split('.')[0].replace('T', ','))