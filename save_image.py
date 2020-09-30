import random
import re

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

def selenium(url):
    capabilities = webdriver.DesiredCapabilities().FIREFOX
    capabilities["marionette"] = True
    binary = FirefoxBinary('/root/firefox/firefox')
    driver = webdriver.Firefox(firefox_binary=binary, capabilities=capabilities,
                               executable_path="/usr/local/bin/geckodriver")
    driver.get(url)
    command = driver.page_source
    jancok = []
    lonte = []
    # all_divs = driver.find_elements_by_class_name("KL4Bh")
    # for image in all_divs:
    #     jancok.append(image.get_attribute("innerHTML"))
    if(re.findall('(?:"src":")(https://instagram.fcgk18-1.fna.fbcdn.net/v/t51.2885-15/e35/s1080x1080/.*?)"', command) or
            re.findall('(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/e35/s1080x1080/.*?)"', command)):
        if (re.findall('(?:"src":")(https://instagram.fcgk18-1.fna.fbcdn.net/v/t51.2885-15/e35/s1080x1080/.*?)"', command)):
            bodat = re.findall('(?:"src":")(https://instagram.fcgk18-1.fna.fbcdn.net/v/t51.2885-15/e35/s1080x1080/.*?)"', command)
            for bodats in bodat:
                jancok.append(bodats.replace('\\u0026', '&'))
            if(re.findall('(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/e35/s1080x1080/.*?)"', command)):
                badot = re.findall('(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/e35/s1080x1080/.*?)"', command)
                for bodats in badot:
                    jancok.append(bodats.replace('\\u0026', '&'))
            # if (re.findall('(?:"src":")(https://instagram.fcgk18-1.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s750x750/.*?)"',command)):
            #     asu = re.findall('(?:"src":")(https://instagram.fcgk18-1.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s750x750/.*?)"',command)
            #     for bodats in asu:
            #         jancok.append(bodats.replace('\\u0026', '&'))
        if (re.findall('(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/e35/s1080x1080/.*?)"', command)):
            basot = re.findall('(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/e35/s1080x1080/.*?)"', command)
            for bodats in basot:
                jancok.append(bodats.replace('\\u0026', '&'))
    elif(re.findall('(?:"src":")(https://instagram.fcgk18-1.fna.fbcdn.net/v/t51.2885-15/e35/p1080x1080/.*?)"',command) or
         re.findall('(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/e35/p1080x1080/.*?)"', command)):
        if (re.findall('(?:"src":")(https://instagram.fcgk18-1.fna.fbcdn.net/v/t51.2885-15/e35/p1080x1080/.*?)"', command)):
            asu = re.findall('(?:"src":")(https://instagram.fcgk18-1.fna.fbcdn.net/v/t51.2885-15/e35/p1080x1080/.*?)"', command)
            for bodats in asu:
                jancok.append(bodats.replace('\\u0026', '&'))
            if (re.findall('(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/e35/p1080x1080/.*?)"', command)):
                usa = re.findall('(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/e35/p1080x1080/.*?)"', command)
                for bodats in usa:
                    jancok.append(bodats.replace('\\u0026', '&'))
        if (re.findall('(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/e35/p1080x1080/.*?)"', command)):
            tai = re.findall('(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/e35/p1080x1080/.*?)"', command)
            for bodats in tai:
                jancok.append(bodats.replace('\\u0026', '&'))
    elif (re.findall('(?:"src":")(https://instagram.fcgk18-1.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s750x750/.*?)"',command) or
          re.findall('(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s750x750/.*?)"',command)):
        if (re.findall('(?:"src":")(https://instagram.fcgk18-1.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s750x750/.*?)"', command)):
            asu = re.findall('(?:"src":")(https://instagram.fcgk18-1.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s750x750/.*?)"',command)
            for bodats in asu:
                jancok.append(bodats.replace('\\u0026', '&'))
            if (re.findall('(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s750x750/.*?)"',command)):
                usa = re.findall(
                    '(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s750x750/.*?)"', command)
                for bodats in usa:
                    jancok.append(bodats.replace('\\u0026', '&'))
        if (re.findall('(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s750x750/.*?)"', command)):
            tai = re.findall('(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s750x750/.*?)"',command)
            for bodats in tai:
                jancok.append(bodats.replace('\\u0026', '&'))
    elif (re.findall('(?:"src":")(https://instagram.fcgk18-1.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/p750x750/.*?)"',command) or
          re.findall('(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/p750x750/.*?)"',command)):
        if (re.findall('(?:"src":")(https://instagram.fcgk18-1.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/p750x750/.*?)"', command)):
            asu = re.findall('(?:"src":")(https://instagram.fcgk18-1.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/p750x750/.*?)"',command)
            for bodats in asu:
                jancok.append(bodats.replace('\\u0026', '&'))
            if (re.findall('(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/p750x750/.*?)"',command)):
                usa = re.findall(
                    '(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/p750x750/.*?)"', command)
                for bodats in usa:
                    jancok.append(bodats.replace('\\u0026', '&'))
        if (re.findall('(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/p750x750/.*?)"', command)):
            tai = re.findall('(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/p750x750/.*?)"',command)
            for bodats in tai:
                jancok.append(bodats.replace('\\u0026', '&'))
    elif (re.findall('(?:"src":")(https://instagram.fcgk18-1.fna.fbcdn.net/v/t51.2885-15/e35/.*?)"',command) or
          re.findall('(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/e35/.*?)"',command)):
        if (re.findall('(?:"src":")(https://instagram.fcgk18-1.fna.fbcdn.net/v/t51.2885-15/e35/.*?)"', command)):
            asu = re.findall('(?:"src":")(https://instagram.fcgk18-1.fna.fbcdn.net/v/t51.2885-15/e35/.*?)"',command)
            for bodats in asu:
                jancok.append(bodats.replace('\\u0026', '&'))
            if (re.findall('(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/e35/.*?)"',command)):
                usa = re.findall(
                    '(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/p750x750/.*?)"', command)
                for bodats in usa:
                    jancok.append(bodats.replace('\\u0026', '&'))
        if (re.findall('(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/e35/.*?)"', command)):
            tai = re.findall('(?:"src":")(https://instagram.fcgk18-2.fna.fbcdn.net/v/t51.2885-15/e35/.*?)"',command)
            for bodats in tai:
                jancok.append(bodats.replace('\\u0026', '&'))
    else:
        print("Jancok")
    jancok = list(dict.fromkeys(jancok))
    # print(command)
    return jancok

def check(responses):
    parsed_link = BeautifulSoup(responses.content, "html.parser")
    if (parsed_link.find("meta", property="og:video")):
        return True
    if (parsed_link.find("meta", property="og:image")):
        return False

def parsing(response):
    parsed_html = BeautifulSoup(response.content, "html.parser")
    if(parsed_html.find("meta", property="og:video")):
        bacot = parsed_html.find("meta", property="og:video")
        pantek = requests.get(bacot["content"])
        download = pantek.content
    else:
        bacot = parsed_html.find("meta", property="og:image")
        pantek = requests.get(bacot["content"])
        download = pantek.content
    return download

def download(file_name, content):
    # if(isinstance(content, str)):
        with open(file_name, "wb") as file:
            file.write(content)
            print("[+] Download Succesful " + file_name)
    # else:
    #     with open(file_name, "wb") as file:
    #         for string in content:
    #             parah = requests.get(string)
    #             file.write(parah.content)
    #             print("[+] Download Succesful")

def run():
    print("PLease Input the link")
    command = raw_input()
    jancok = selenium(command)
    response = request(command)
    halo = check(response)
    parsed = parsing(response)
    if (len(jancok) > 0):
        for string in jancok:
            pantek = requests.get(string)
            if halo == True:
                file_name = 'Vid' + str(random.randint(1, 1000)) + '.mp4'
                download(file_name, parsed)
            else:
                file_name = 'Pic' + str(random.randint(1, 1000)) + '.jpg'
                download(file_name, pantek.content)
    else:
        if halo == True:
            file_name = 'Vid' + str(random.randint(1, 1000)) + '.mp4'
            download(file_name, parsed)
run()





