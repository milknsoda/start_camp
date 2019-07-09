import webbrowser

idols = ['bts', 'iu', '레드벨벳']
for idol in idols:
    # string interpolation
    # 문자열 보간법 : f-string / v3.6+
    webbrowser.open(f'https://search.naver.com/search.naver?query={idol}')
