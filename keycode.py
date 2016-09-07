import re

fx = open('test.txt', 'wb+')
fx.flush()
with open('keycode.txt', 'r') as f:
    for i in f:
        try:
            st = re.search("(KEY.*_)(.*)", i).group(2) + '\n'
        except:
            continue
        fx.write(st)
    fx.close()
