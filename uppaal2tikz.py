import xml.etree.ElementTree
import sys

def texify(str):
    # TODO
    return str


def format_label(ptr):
    print(f'\\node[uppaal_label, uppaal_{ptr.attrib["kind"]}] at({ptr.attrib["x"]}, {ptr.attrib["y"]}) {{$ {texify(ptr.text)} $}};')


def format_node(ptr):
    print(f'\\node[uppaal_node] at({ptr.attrib["x"]}, {ptr.attrib["y"]}) ({ptr.attrib['id']}) {{}};')
    lbl = ptr.find('name')
    if lbl is not None:
        print(f'\\node[uppaal_node_name] at({lbl.attrib["x"]}, {lbl.attrib["y"]}) {{ {lbl.text} }};')
    for lbl in ptr.findall('label'):
        format_label(lbl)


def format_trans(ptr):
    def fetch_ref(name):
        return ptr.find(name).attrib["ref"]
    print(f'\\draw[uppaal_trans] ({fetch_ref("source")}) -- ({fetch_ref("target")});')
    for lbl in ptr.findall('label'):
        format_label(lbl)


def main():
    print(f'Parsing {sys.argv[1]}')
    doc = xml.etree.ElementTree.parse(sys.argv[1])
    root = doc.getroot()
    for elem in root.find('template'):
        if elem.tag == 'location':
            format_node(elem)
        if elem.tag == 'transition':
            format_trans(elem)


if __name__ == '__main__':
    main()
