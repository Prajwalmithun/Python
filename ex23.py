from sys import argv

script, encoding, error = argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)    #recursion

def print_line(line, encoding, errors):
    next_lang = line.strip()    # Removes leading and trailing spaces
    raw_bytes = next_lang.encode(encoding, errors = errors)     # DBES(Decode Bytes Encode String)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)