

#different chars mapped to different letters
#flag format : bcactf{example_flag}
#uses DVORAK keyboard

qwerty = """wq_}eqwertyuiop{}\\asdfghjkl;'zxcvbnm,./"""
dvorak = """,'{+.?<>pyfgcrl?+\\aoeuidhtns":qjkxbmwvz"""
msg = "Cy ygpbo rgy ydco t.fxrape go.o yd. Ekrpat nafrgy! Cy p.annf m.oo.o gl mf mgojn. m.mrpfv Yd. unai co xjajyu?t3fx0ape{naf0g7{jdabi3gl{',.pyf+"
msg = msg.lower()
#Dict = {'c' : 'i','y' : 't','f':'b','x':'c','0':'a','a':'c','p':'t','e':'f','.'}
res = ""
for i in range(0,len(msg)):
	if msg[i] == " ":
		res += " "
		continue
	found = False
	for x in range(0,len(dvorak)):
		if msg[i] == dvorak[x]:
			res += qwerty[x] 
			found = True
	if not found:
		res += msg[i]


print(res)  

