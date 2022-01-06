from xml.etree import ElementTree

def walk(node, rates, level):
    level += 1
    for child in node:
        rates[child.attrib['color']] += level
        walk(child, rates, level)

def main():
    # xml = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'
    xml = input()
    tree = ElementTree.ElementTree(ElementTree.fromstring(xml))
    root = tree.getroot()

    rates = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    rates[root.attrib['color']] = 1

    walk(root, rates, 1)

    print(rates['red'], rates['green'], rates['blue'])

if __name__ == '__main__':
    main()