from package.query import query
import sys

if __name__=="__main__":
    word = " ".join(sys.argv[1:])
    query(word)