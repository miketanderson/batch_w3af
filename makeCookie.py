
def makeCookie(cookiepath="~/cookies.txt",domain=".website.com",cName="", cVal="",cName2="", cVal2="",cName3="",cVal3=""):
    cookieString = "# Netscape HTTP Cookie File" + "\n"
    if len(cName) > 0 and len(cVal) > 0:
        cookieString += domain + "\tTRUE\t/\tFALSE\t999999999999\t" + cName + "\t" + cVal + "\n"
    if len(cName2) > 0 and len(cVal2) > 0:
        cookieString += domain + "\tTRUE\t/\tFALSE\t999999999999\t" + cName2 + "\t" + cVal2 +"\n"
    if len(cName3) > 0 and len(cVal3) > 0:
        cookieString += domain + "\tTRUE\t/\tFALSE\t999999999999\t" + cName3 + "\t" + cVal3 +"\n"

    cookieFile = open(cookiepath,"w")
    cookieFile.write(cookieString)
    cookieFile.close()

makeCookie("/tmp/cookies.txt", ".website.com","server","development","user","admin")
