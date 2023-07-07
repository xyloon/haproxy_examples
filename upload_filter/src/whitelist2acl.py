#
from sys import argv


# acl  file_ext_png req.body -m reg \"(file|path)\":.*\"\.\/[^\"]+\.[pP][nN][gG]\"
# http-request deny if upload_req http_post !file_ext_png !file_ext_txt

acllist=[ 'upload_req', 'http_post']
with open(argv[1], 'r') as fdr:
    for oneline in fdr.readlines():
        extname_base = oneline.strip()
        extname=extname_base.replace("*", "_all_").replace(".", "_dot_")
        extstr=""
        for onechr in extname_base:
            if onechr >= 'a' and onechr <= 'z':
                extstr += f'[{onechr}{onechr.upper()}]'
            elif onechr >='a' and onechr <='Z':
                extstr += f'[{onechr}{onechr.lower()}]'
            elif onechr == '*':
                extstr += '[^\\"]*'
            elif onechr == '.':
                extstr += '\\.'
            elif onechr >='0' and onechr <='9':
                extstr += onechr
            else:
                raise Exception(f"{onechr} is not processed")
        acllist.append(f'!file_ext_{extname}')
        print(f'  acl  file_ext_{extname} req.body -m reg \\"(file|path)\\":.*\\"\.\\/[^\\"]+\\.{extstr}\\"')
print(f'  http-request deny if {" ".join(acllist)}')
