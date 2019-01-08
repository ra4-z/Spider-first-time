import requests
from bs4 import BeautifulSoup
import time
import random

if __name__ == '__main__':
    # prepared headers
    head = []
    head.append({'User-Agent': 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'})
    head.append({'User-Agent': 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19'})
    head.append({'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'})
    head.append({'User-Agent': 'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19'})
    #names of areas 
    areas=["yuexiu","huangpua","nansha","liwan","conghua""fanyu","tianhe","baiyun","haizhu","zengcheng","huadu"]

    # uniformationalization
    def formation(rawtxt):
        txt = rawtxt.text
        txt = txt.replace(' ','')
        txt = txt.replace('\t','')
        txt = txt.replace('\n','\t')
        return txt

    for place in areas:
        # output file 
        outf = open(place + ".txt","w",encoding='utf-8')
        for page in range(2,42):
            # url
            source = "https://gz.zu.anjuke.com/fangyuan/"
            target = source + place + '/' + 'p' + str(page) + '/'
            #header and request
            random.seed(page)
            header = head[random.randint(0,3)]
            req = requests.get(url = target, headers = header)
            html = req.text
            #find needed info
            bf = BeautifulSoup(html)
            price = bf.find_all('div', class_ = 'zu-side')
            area = bf.find_all('p', class_ = 'details-item tag')
            address = bf.find_all('address', class_ = 'details-item')
            #write to file
            for i in range(len(price)):
                outf.write(formation(price[i]))
                outf.write(formation(area[i]))
                outf.write(formation(address[i]))
                outf.write("\n")
            #have a rest
            time.sleep(random.uniform(1,5))
        outf.close()