import sys
from bs4 import BeautifulSoup
vystup = open('./UDIanswers.txt', 'w');
#soup = BeautifulSoup('<div class="rightanswer">Správná odpověď je: před jejich uvedení do provozu.</div>','html.parser')
with open("test.html") as fp:
    soup = BeautifulSoup(fp)
Payload = soup.findAll('div', {"class":"rightanswer"})
Payload2 = soup.findAll('div', {"class":"qtext"})
print(Payload2[0].string)
print(Payload[0].string)
print(len(Payload), len(Payload2))
i = 0
while i < 105:
    if Payload[i].string == None or Payload2[i].string == None:
        if Payload[i].string == None:
            data = str(Payload[i]);
            soupc = BeautifulSoup(data, 'html.parser')
            pay = soupc.select_one('div span')
            vystup.write("{0}; Správná odpověď je: {1}\n".format(Payload2[i].string, pay.text))
        #vystup.write("{0}; {1}\n".format(Payload2[i].string,Payload[i].string))
        print("ok")
    else:
        vystup.write("{0}; {1}\n".format(Payload2[i].string, Payload[i].string))
        #vystup.write("{0}; {1}\n".format(Payload2[i],Payload[i]))

        print(Payload[i])
        
    i +=1
vystup.close()

