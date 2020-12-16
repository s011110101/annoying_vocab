import requests,sys
time=int(sys.stdin.readline())
words=[]
for i in range(time):
    ans=""
    temp=str(sys.stdin.readline())
    li=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    li2=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'," ","(",")",":"]
    for i in temp:
        for j in li:
            if i==j:
                ans+=i
    words.append(ans)
print (words)
kv={"user-agent":"Mozilla/5.0"}
for j in words:
    url="https://www.merriam-webster.com/dictionary/"+j
    try:
        r = requests.get(url,headers = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print (j)
        out=r.text
        defin=[]
        flagdocstart=False
        for i in range(len(out)):
            #to start grabbing the definition
            if out[i:i+21]=='''<span class="dtText">''':
                flagdocstart=True
            if flagdocstart:
                temp=""
                j=i+35+21
                while out[j:j+7]!="</span>" and out[j:j+5]!="<span":
                    temp+=out[j]
                    j+=1
                flagdocstart=False
                defin.append(temp)
        #     #to start grabbing the first example
        #     if flag3:
        #         if out[i:i+23]=="<span class="+"\""+"t has-aq"+"\""+">":
        #             start=i+23
        #             break
        # out=out[start:start+1000]
        # for i in range(1000):
        #     if out[i:i+32]=='''</span> <span class="aq has-aq">''':
        #         out=out[0:i]
        #         break
        # flag=True
        # exa=""
        # #to get avoid of style
        print (defin)
        out=[]
        flagvaliddefin=True
        for j in defin:
            temp=""
            for i in j:
                if i=="<":
                    flagvaliddefin=False
                if flagvaliddefin and i in li2:
                    temp+=i
                if i==">":
                    flagvaliddefin=True
            out.append(temp)
        for i in out:
            print(i)
    except:
        print("error")
