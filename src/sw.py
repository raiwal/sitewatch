# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 15:01:32 2021

@author: Rainer Waltzer
"""
import configparser
import time
import datetime
import requests
import re
import logging

config = configparser.ConfigParser()
config.read('src/sitewatch.ini', encoding='utf-8')
time_interval = int(config['DEFAULT']['Delay'])

log_date = str(datetime.date.today())
log_filename = 'logs/responselog_' + log_date + '.log'
logging.basicConfig(filename=log_filename, level=logging.INFO)

class WebPage:
    def __init__(self, address, information, timeout):
        self.ok = False
        self.response = None
        self.address = address
        self.information = information
        self.timeout = timeout

    def update(self):
        self.ok = True
        self.start = time.perf_counter()
        try:
            self.response = requests.get(self.address, timeout=self.timeout)
        except requests.Timeout as e:
            self.ok = False
            self.response_time =  time.perf_counter() - self.start
            logging.critical(self.address + ':Timeout:' + str(e))
        except requests.ConnectionError as e:
            self.ok = False
            self.response_time =  time.perf_counter() - self.start
            logging.critical(self.address + ':Connection error:' + str(e))
        except Exception as e:
            self.ok = False
            self.response_time =  time.perf_counter() - self.start
            logging.critical(self.address + ':Exception:' + str(e))
        self.response_time =  time.perf_counter() - self.start

    def pattern_match(self):
        found = re.search(self.information, self.response.text)
        if found:
            logging.info(self.address + ':{:.3f}s'.format(self.response_time))
        else:
            logging.warning(self.address + ':' + '{:.3f}s'.format(self.response_time) + ':' + ':PATTERN NOT FOUND:' + self.information)
                                   
while True:    
    for site in config.sections():
        page = WebPage(site, config[site]['Pattern'], float(config[site]['Timeout']))
        page.update()
        if page.ok:
            page.pattern_match()
        time.sleep(time_interval)
