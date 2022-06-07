def Song(songstr):
    for ch in songstr:
        if ch in ", . ' !":
            songstr=songstr.replace(ch,"")
        return songstr
def wordcount(songcount):
    songlist=songcount.split()
    print("以下是歌词串列")
    for wd in songlist:
        if wd in dict:
             dict[wd]+=1
        else:
            dict[wd]=1

data="""I'm a flame Short of fire I'm the dark in need of light When we
touch You inspire Feel the change in me tonight So take me up Take me
higher There's a war not far from here We can dance In desire Or we can
burn in love tonight Our hearts are like Firestones And when they strike
We feel the love Sparks will fly They ignite our bones And when they
strike We light up the world! Our hearts are like Firestones And when
they strike We feel the love Sparks will fly They ignite our bones And
when they strike We light up the world We light up the world We light up
the world! Oh oh Woah Oh oh Firestone I'm from X , you're from Y
Perfect …"""

dict={}
print("将歌词改为小写同时将标点符号用子元取代：")
song= Song(data.lower())
print(song)
wordcount(song)
print("执行结果：")
print(dict)
