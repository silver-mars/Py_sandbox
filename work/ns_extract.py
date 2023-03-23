from sys import path, argv
path.append("/home/silver/quests/saint/")

def extract_namespace(doc):
    with open(doc, 'r') as fd:
        textum = fd.readlines()

    ns = dict()
    for line in textum:
        if 'xmlns:' in line:
            #print(line)
            ns_count = line.count('xmlns:')
            tmp = 0
            for i in range(ns_count):
                begin = line[tmp:].index('xmlns:') + 6 + tmp
                end = begin + line[begin:].index('=')
                # debug
                #   print(begin, end)
                #   print(line[begin:end])
                #   print(line[end:].split('"')[1])
                ns[line[begin:end]] = line[end:].split('"')[1]
                #print(ns)
                tmp = end
    return(ns)

if __name__ == "__main__":
    doc = argv[1]
    extract_namespace(doc)
