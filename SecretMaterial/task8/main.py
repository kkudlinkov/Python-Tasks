import re


def main(s):
    s = s.replace('\n', ' ')
    pattern = r'\.do var\s*\[(.+?)\]\s*\|\>\s*(\w+)'
    matches = re.findall(pattern, s)
    result = []
    for match in matches:
        values = re.findall(r'[\w_]+', match[0])
        result.append((match[1], values))
    return result

print(main(r'\begin .do var [rigele bibi_985] |> teen .end .do var[ cebiar rire_352 arat_55]|> islari .end \end'))