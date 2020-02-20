import argparse

def deduplicate(filename):

    dedup = set()
    with open(filename) as f:
        content = f.read().splitlines()

    output_filename = filename.split('.')[0] + "_dedup.bib"
    with open(output_filename, "w") as fo:

        for line in content:
            if len(line) == 0:
                writeflag = True
            elif len(line) > 0 and line[0] == '@':
                refname = line.split('{')[-1][:-1]

                if refname in dedup:
                    print "Remove duplicated " + refname
                    writeflag = False
                else:
                    writeflag = True
                    dedup.add(refname)

            if writeflag:
                fo.write(line+'\n')

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type = str, default = "ref.bib", help='Input bib file name')
    args = parser.parse_args()

    filename = args.filename
    deduplicate(filename)
