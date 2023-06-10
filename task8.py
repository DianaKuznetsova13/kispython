def main(s):
    dict = {}
    s = s.replace("\n", ' ')
    s = s.replace("[", ' ')
    s = s.replace("<section>", ' ')
    s = s.replace("`", ' ')
    s = s.replace("::=", ' ')
    s = s.replace(";", ' ')
    s = s.replace("]", ' ')
    s = s.replace("</section>", '')
    s = s.split(' ')
    try:
        while True:
            s.remove("")
    except ValueError:
        pass
    for i in range(0, len(s)):
        if s[i] == 'store':
            key = s[i + 1]
            value = []
            value.append(s[i + 2])
            value.append(s[i + 3])
            value.append(s[i + 4])
            dict[key] = value
    return dict

s = input()
print(main(s))
