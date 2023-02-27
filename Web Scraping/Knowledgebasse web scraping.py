# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 00:36:16 2023

@author: Himanshu Mayank
"""
#Web Scraping to create a knowledge base  
import bs4
import requests
import re
import os


def scrape_content(url): 
    doc=""
    res=requests.get(url)
    res.raise_for_status()
    wiki = bs4.BeautifulSoup(res.text,"html.parser")
    for i in wiki.select('p'):
        text=i.getText()
        doc=doc+str(text)
    return(str(doc))

#Creation of the dynamic dataset
def search_and_scrape(query,url):    
    href_list=[]
    imp_href_list=[]
    os.chdir(r'D:\MMA Material\Term 3\BUSA Submission\BDC Modelling')
    res=requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    txt_file=query+".txt"
    with open(txt_file,'a',encoding='utf-8') as f:
        text_1=scrape_content(url)
        text_1=str(text_1)
        f.write(text_1)
        f.close() 

topics =["Analysis","KPI Performance","Data Engineering"]
for query in topics:
    #query="Marketing Management"
    query1 =query+"wikipedia"
    
    try: 
            from googlesearch import search 
    except ImportError:  
            print("No module named 'google' found") 
    for j in search(query1, tld="co.in", num=1 , stop=1, pause=2): 
            print(j) 
            print('\n')
    url=j
    print(url)
    search_and_scrape(query,url)