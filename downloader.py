import urllib2
import time

#time.sleep(5)
brojac = 0
with open("mp3links.txt") as infile:
    for line in infile:
        if line in ['\n', '\r\n']: #izlaz iz programa
            print "That's it!"
            break
        naziv_mp3 = line
        naziv_mp3 = naziv_mp3.replace('http://archive.org/download/Best_of_8_Bit_Collective-2006-2011/Best_of_8_Bit_Collective-2006-2011.tar/Best_of_8_Bit_Collective_%288bc%29_%5B06-2006_to_06-2011%5D%2F','')
        naziv_mp3 = naziv_mp3.replace('\n','')
        naziv_mp3 = naziv_mp3.replace('%20',' ')
        naziv_mp3 = naziv_mp3.replace('%28','(')
        naziv_mp3 = naziv_mp3.replace('%29',')')
        naziv_mp3 = naziv_mp3.replace('%2C',',')
        mp3file = urllib2.urlopen(line)
        output = open(naziv_mp3,'wb')
        output.write(mp3file.read())
        output.close()
        time.sleep(5)
        brojac+=1
        print 'Line song number:', brojac,'- Name: ', naziv_mp3

print "WIN!"
