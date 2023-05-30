import cssfuck.compiler as compiler
import sys
def main():
        if(len(sys.argv) - 1 < 1):
            print("NO ARGUMENTS")
            return
        if(sys.argv[1] == "-h" or sys.argv[1] == "--help"):
            print("-------------")
            print("-h or --help: Prints this message.")
            print("-c <conversiontype> <cssfuckfile> <cssfile> or --compile: Compiles a cssfuck file to a css one.")
            print("-o <file> <lang> or --onefile: Prints the compiled version of that file.")
            print("-------------")
            return
        if(sys.argv[1] == "-o" or sys.argv[1] == "--onefile"):
            if(len(sys.argv) < 3):
                print("Specify the file.")
                return 
            if(len(sys.argv)< 4):
                print("Specify the file type.")
                return
            if(sys.argv[3] == "css"):
                with open(sys.argv[2], "r") as f:
                    file_ = f.read()
                print(compiler.decompile(file_))
                return
            elif(sys.argv[3] == "cssfuck"):
                with open(sys.argv[2], "r") as f:
                    file_ = f.read()
                print(compiler.compile(file_))
                return
            else:
                print("Unknown file type.")
                return
        if(sys.argv[1] == "-c" or sys.argv[1] == "--compile"):
            if(len(sys.argv) < 2):
                print("Please specify the conversion type.")
                print("1. CSSFuck to CSS")
                print("2. CSS to CSSFuck")
                return
            if(len(sys.argv) < 3):
                print("Please specify the css file.")
                return
            elif(len(sys.argv) < 4):
                print("Please specify the cssfuck file")
                return
            elif(sys.argv[2] == "1"):
                with open(f"{sys.argv[4]}", "r") as f:
                    text = f.read()
                    compiled = compiler.compile(text)
                with open(f"{sys.argv[3]}", "w") as f:
                    f.write(compiled)
            if(sys.argv[2] == "2"):
                with open(f"{sys.argv[3]}", "r") as f:
                    text = f.read()
                    compiled = compiler.decompile(text)
                with open(f"{sys.argv[4]}", "w") as f:
                    f.write(compiled)