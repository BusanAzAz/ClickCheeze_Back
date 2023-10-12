# 분위기 (카테고리) 배경 색 도출
simple = ['#E5E5E5','#B2B2B2','#FDE9E8','#475F77','#FFFFFF','#000000'] #one tone (그레이, 화이트, 블랙)
cute = ['#FF8#99','#FFC0CB','#FFB0D9','#F9C3B7','#FFDAB1','#F9C3B7'] # ???주황 0
happy = ['#FFD966','#FFF9AB','#AEC9FE','#F06A8A','#FAE360','#F48E35'] # 기쁜계열 폭죽계열, 원색 노란 0
lovely = ['FFCCFF','FF99FF','FF66FF','FF33FF','FF00FF','FF8184'] # pink 0
chic = ['#000000','#822525','#6a329f','#A61B26','#092126','#243E73'] # black, 진보라,버건디 0
kitsch = ['#CC66FF', '#FE7CAD','#EF415B','#FAD0E6','#FF5A5A','#4A4E8C'] # 다홍, 보라, 베이비핑크, 연핑크, 진한다홍 0
romantic = ['#F30A0A','#D52B2B','#CC0066','#A60311','#D92344','#8D414D'] # red 장미색 0
casual = ['#073763','#83A1FF','#41507F','#686D7F','#FFDBB3','#324359'] # blue, 무채색, 어두눈, 보라, 네이비 0
vintage = ['#f1c27d','#8d5524','#153450','#993366','#990033','#8C6472'] #빈티지 의상 브라운 0
bright = ['#FFFFCC','#FFFF99','#FFFF66','#FFFF33','#FFFF00','#ECFFCB'] # yellow 병아리 0
fresh = ['#e3cac4','#B7D0D4','#5A9CA1','#4B6580','#0099FF','#33FF00'] # beige, 청색, 라임, 스카이블루 0
calm = ['#BAFFC9','#B0ED9B','#2986CC','#A6BEE0','#889FC4','#E2E1DE'] # green (딥그린, 채도 낮은 블루, 그레이) 0

def getBackColor(category):
    if category == '심플한':
        return simple
    elif category == '귀여운':
        return cute
    elif category == '즐거운':
        return happy
    elif category == '사랑스러운':
        return lovely
    elif category == '시크한':
        return chic
    elif category == '키치한':
        return kitsch
    elif category == '로맨틱한':
        return romantic
    elif category == '캐주얼한':
        return casual
    elif category == '빈티지한':
        return vintage
    elif category == '화사한':
        return bright
    elif category == '산뜻한':
        return fresh
    elif category == '차분한':
        return calm
