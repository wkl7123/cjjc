#coding=utf-8
from pyquery import PyQuery as pq
import re
import sys
from termcolor import colored,cprint
def hj_query(word):
    html=pq('http://dict.hjenglish.com/jp/cj/'+word, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
    container=html('div.mian_container.main_container')
    string_template='#headword_jp_'
    def my_print(x):
        print x
    for i in range(1,21):
        num='%d' %i
        id_name=string_template+num
        target=container(id_name)
        if target==[]:
            break
        kannji=target('div.jp_title_td input').val()
        hiragana=target('div.mt10 span.trs_jp.bold font').text()
        english=target('div.mt10 span.trs_jp.bold').eq(1).text()
        # english='['+english[1:-1]+']'
        if i==1:
            cprint('-'*38+' ✂ '+'-'*39,'white')
        else:
            cprint('-  -'*20,'white')
        cprint(chr(64+i)+'  '+kannji+' '+hiragana+' '+english,'magenta')
        main=target('div.word_ext_con.clearfix')
        type_name=main('div.flag.big_type.tip_content_item').html() #May be None
        if type_name!=None:
            cprint(type_name,'cyan')
        yakus=main('ul li')
        for li in yakus.items():
            yaku=li('div').eq(0).text()
            tatoes=li('div[style]').html()    #May be None
            # print type(tatoes)
            cprint(yaku,'yellow')
            if tatoes!=None:
                # tatoes=re.sub('^<img.*?/>$','+ ',tatoes)
                tatoes=re.sub(r'<img src="http://dict.hjenglish.com/images/icon_star.gif" align="absmiddle"/>','+ ',tatoes)
                tatoes=re.sub(r'<br/>','\n',tatoes)
                tatoes=re.sub(r'<b>' ,'',tatoes)
                tatoes=re.sub(r'</b>','',tatoes)
                tatoes=re.sub(r'/','\n  ',tatoes)
                if tatoes[0]=="\n":
                    tatoes=tatoes[1:]
                print tatoes
    if i!=1:
        cprint('-'*38+' ✂ '+'-'*39,'white')
hj_query(sys.argv[1])

