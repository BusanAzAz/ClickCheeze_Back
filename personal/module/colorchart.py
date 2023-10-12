spring_warm = ['#FFEDCF', '#FBDBC4', '#F8A980' ,'#90D7EB']
summer_cool = ['#91A5C0', '#FBCAD0', '#AFBDE0', '#B3DDD3']
fall_warm = ['#D3C191', '#8EB161', '#EBA188', '#A48B53']
winter_cool = ['#003060', '#FFF9AF', '#BDBEC0', '#42429C']

def getChart(tone):
    if tone == '봄웜톤':
        return spring_warm
    elif tone == '여름쿨톤':
        return summer_cool
    elif tone == '가을웜톤':
        return fall_warm
    elif tone == '겨울쿨톤':
        return winter_cool