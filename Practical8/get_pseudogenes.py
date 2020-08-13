def get_name(line):
    for i in line.split(" "):
        if i.startswith("gene:"):
            return i


def get_len(SEQ):
    cnt = 0
    for i in SEQ:
        cnt += len(i)
    return cnt


FILE_NAME = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
NEW_FILE_NAME = "pseudogenes.fa"

NEW_FILE = open(NEW_FILE_NAME, "w+")

with open(FILE_NAME) as f:
    LINES = f.readlines()

LINE_NAME = None

for LINE in LINES:
    if LINE[0] == ">":
        if LINE_NAME:
            NEW_FILE.write(f">{LINE_NAME} length:{get_len(SEQ)}\n")
            for i in SEQ:
                NEW_FILE.write(i)
        LINE_NAME = get_name(LINE)
        SEQ = []
    else:
        SEQ.append(LINE)

NEW_FILE.close()
