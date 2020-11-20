import requests,sys
time=int(sys.stdin.readline())
words=[]
for i in range(time):
    ans=""
    temp=str(sys.stdin.readline())
    li=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
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
        flag1=True
        flag2=True
        flag3=True
        for i in range(len(out)):
            #to start grabbing the definition
            if flag1:
                if out[i:i+25]=="property="+"\""+"og:description"+"\"":
                    start1=i+35
                    flag1=False
            if flag2:
                if out[i:i+23]=="See the full definition":
                    ans=out[start1:i-2]
                    flag2=False
            #to start grabbing the first example
            if flag3:
                if out[i:i+23]=="<span class="+"\""+"t has-aq"+"\""+">":
                    start=i+23
                    break
        out=out[start:start+1000]
        for i in range(1000):
            if out[i:i+32]=='''</span> <span class="aq has-aq">''':
                out=out[0:i]
                break
        flag=True
        exa=""
        #to get avoid of style
        for i in out:
            if i=="<":
                flag=False
            if flag:
                exa+=i
            if i==">":
                flag=True
        print(ans)
        print(exa)
        print("\n")
    except:
        print("error")
