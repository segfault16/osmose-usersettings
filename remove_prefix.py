import re
with open ('state.txt', 'r' ) as f:
    content = f.read()
    content_new = re.sub('(\d{1,2},)(.*)', r'\2', content, flags = re.M)
    print(content_new)
    # write content_new to file
    with open ('state.txt', 'w' ) as f:
        f.write(content_new)