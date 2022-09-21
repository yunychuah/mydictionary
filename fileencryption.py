infile = open('info_security.txt', 'r')
encrypted = infile.read()

codes = {'A':'&','a':'8','B':'@','b':'!','C':'@','c':'8','D':'*','d':'4',
        'E':'5','e':'#','F':'^','f':'9','G':'%','g':'Y','H':'3','h':'@',
        'I':'-','+':'=','J':'r','j':'w','K':'(','k':',','L':'$','l':'c',
        'M':'#','m':'=','N':'_','n':'.','O':'~','o':'}','P':'9','p':'*',
        'Q':'8','q':'O','R':'#','r':'~','S':'7','s':';','T':'{','t':'_',
        'U':'76','u':'S','V':'i','v':'=','W':'U','w':'(','X':'%','x':'k',
        'Y':'@','y':'R','Z':'!','z':'i','.':'*',':':'%',' ':'('}

outfile = open('encrypted.txt', 'w')

for k,v in codes.items():
    search = k
    replace = v
    encrypted = encrypted.replace(search,replace)

outfile.write(encrypted)