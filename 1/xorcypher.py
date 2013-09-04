import json 
import urllib2

from utils import fixed_XOR

def wordProbability(message):
    
    baseUrl = "http://en.wiktionary.org/w/api.php?action=query&format=json&titles={0}"
    words = message.split()
    found = 0.0 
    total = 0.0 

    for word in message.split():
        total += 1
        apiUrl = baseUrl.format(word)
        response = urllib2.urlopen(apiUrl)
        result = json.load(response)

        if "query" in result:
            if "pages" in result["query"]:
                if "-1" not in result["query"]["pages"]:
                    found += 1

    return found/total
   
    
def tryAllKeys(xored):

    maxProbability = 0.0 
    maxMessage = ""

    for i in range( 0x00,0xff):
        
        tryNow = ( "%x" % i )* ( len(xored) / 2 ) 
        original = fixed_XOR(xored, tryNow)

        probability = wordProbability(original.decode("hex"))
        if probability > maxProbability:
            maxProbability = probability
            maxMessage = original.decode("hex")


    return maxMessage






    

