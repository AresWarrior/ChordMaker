#this code is pretty lit, and the program tells you chords of major and natural minor

aflatmaj = "AbCEb"
aflatmin = "AbCbEb"
aflatdim = "AbCbEbb"
amaj = "AC#E"
amin = "ACE"
adim = "ACEb"
asharpmaj = "A#CxE#"
asharpmin = "A#C#E#"
asharpdim = "A#C#E"
bflatmaj = "BbDF"
bflatmin = "BbDbF"
bflatdim = "BbDbFb"
bmaj = "BD#F#"
bmin = 'BDF#'
bdim = "BDF"
bsharpmaj = "B#DxFx"
bsharpmin = "B#D#Fx"
bsharpdim = "B#D#F#"
cflatmaj= "CbEbGb"
cflatmin = "CbEbbGb"
cflatdim = "CbEbbGbb"
cmaj = 'CEG'
cmin = 'CEbG'
cdim = "CEbGb"
csharpmaj = 'C#E#G#'
csharpmin = 'C#EG#'
csharpdim = 'C#EG'
dflatmaj = "DbFAb"
dflatmin = "DbFbAb"
dflatdim = 'DbFbAbb'
dmaj = 'DF#A'
dmin = 'DFA'
ddim = "DFAb"
dsharpmaj = 'D#FxA#'
dsharpmin = 'D#F#A#'
dsharpdim = 'D#F#A'
eflatmaj = "EbGBb"
eflatmin = "EbGbBb"
eflatdim = "EbGbBbb"
emaj = 'EG#B'
emin = "EGB"
edim = "EGBb"
esharpmaj = "E#GxB#"
esharpmin = "E#G#B#"
esharpdim = "E#G#B"
fflatmaj = "FbAbCb" 
fflatmin = "FbAbbCb"
fflatdim = "FbAbbCbb"
fmaj = "FAC"
fmin = "FAbC"
fdim = "FAbCb"
fsharpmaj = "F#A#C#"
fsharpmin = 'F#AC#'
fsharpdim = "F#AC"
gflatmaj = "GbBbDb"
gflatmin = "GbBbbDb"
gflatdim = "GbBbbDbb"
gmaj = "GBD"
gmin = "GBbD"
gdim = "GBbDb"
gsharpmaj = "G#B#D#"
gsharpmin = "G#BD#"
gsharpdim = 'G#BD'


def keycmaj():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii, enter 'back' to go back): ")
	
		if rom == 'I':
			print(cmaj)
		if rom == 'ii':
			print(dmin)
		if rom == 'iii':
			print(emin)
		if rom == 'IV':
			print(fmaj)
		if rom == 'V':
			print(gmaj)
		if rom == 'vi':
			print(amin)
		if rom == 'vii':
			print(bdim)
		if rom == 'back':
			count1 = 2

def keyamin():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii and ii, enter 'back' to go back): ")
	
		if rom == 'III':
			print(cmaj)
		if rom == 'iv':
			print(dmin)
		if rom == 'v':
			print(emin)
		if rom == 'VI':
			print(fmaj)
		if rom == 'VII':
			print(gmaj)
		if rom == 'i':
			print(amin)
		if rom == 'ii':
			print(bdim)
		if rom == 'back':
			count1 = 2
		
def keygmaj():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii, enter 'back' to go back): ")	
		
		
		if rom == 'I':
			print(gmaj)
		if rom == 'ii':
			print(amin)
		if rom == 'iii':
			print(bmin)
		if rom == 'IV':
			print(cmaj)
		if rom == 'V':
			print(dmaj)
		if rom == 'vi':
			print(emin)
		if rom == 'vii':
			print(fsharpdim)
		if rom == 'back':
			count1 = 2
			
def keyemin():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii and ii, enter 'back' to go back): ")	
		
		
		if rom == 'III':
			print(gmaj)
		if rom == 'iv':
			print(amin)
		if rom == 'v':
			print(bmin)
		if rom == 'VI':
			print(cmaj)
		if rom == 'VII':
			print(dmaj)
		if rom == 'i':
			print(emin)
		if rom == 'ii':
			print(fsharpdim)
		if rom == 'back':
			count1 = 2
			
			
def keydmaj():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii, enter 'back' to go back): ")
		
		if rom == 'I':
			print(dmaj)
		if rom == 'ii':
			print(emin)
		if rom == 'iii':
			print(fsharpmin)
		if rom == 'IV':
			print(gmaj)
		if rom == 'V':
			print(amaj)
		if rom == 'vi':
			print(bmin)
		if rom == 'vii':
			print(csharpdim)
		if rom == 'back':
			count1 = 2
			
def keybmin():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii and ii, enter 'back' to go back): ")
		
		if rom == 'III':
			print(dmaj)
		if rom == 'iv':
			print(emin)
		if rom == 'v':
			print(fsharpmin)
		if rom == 'VI':
			print(gmaj)
		if rom == 'VII':
			print(amaj)
		if rom == 'i':
			print(bmin)
		if rom == 'ii':
			print(csharpdim)
		if rom == 'back':
			count1 = 2
			
def keyamaj():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii, enter 'back' to go back): ")
		
		if rom == 'I':
			print(amaj)
		if rom == 'ii':
			print(bmin)
		if rom == 'iii':
			print(csharpmin)
		if rom == 'IV':
			print(dmaj)
		if rom == 'V':
			print(emaj)
		if rom == 'vi':
			print(fsharpmin)
		if rom == 'vii':
			print(gsharpdim)
		if rom == 'back':
			count1 = 2
			
def keyfsharpmin():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii and ii, enter 'back' to go back): ")
		
		if rom == 'III':
			print(amaj)
		if rom == 'iv':
			print(bmin)
		if rom == 'v':
			print(csharpmin)
		if rom == 'VI':
			print(dmaj)
		if rom == 'VII':
			print(emaj)
		if rom == 'i':
			print(fsharpmin)
		if rom == 'ii':
			print(gsharpdim)
		if rom == 'back':
			count1 = 2
			
def keyemaj():
	
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii, enter 'back' to go back): ")
	
	
		if rom == 'I':
			print(emaj)
		if rom == 'ii':
			print(fsharpmin)
		if rom == 'iii':
			print(gsharpmin)
		if rom == 'IV':
			print(amaj)
		if rom == 'V':
			print(bmaj)
		if rom == 'vi':
			print(csharpmin)
		if rom == 'vii':
			print(dsharpdim)
		if rom == 'back':
			count1 = 2
			
def keycsharpmin():
	
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii and ii, enter 'back' to go back): ")
	
	
		if rom == 'III':
			print(emaj)
		if rom == 'iv':
			print(fsharpmin)
		if rom == 'v':
			print(gsharpmaj)
		if rom == 'VI':
			print(amaj)
		if rom == 'VII':
			print(bmaj)
		if rom == 'i':
			print(csharpmin)
		if rom == 'ii':
			print(dsharpdim)
		if rom == 'back':
			count1 = 2

def keybmaj():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii, enter 'back' to go back): ")
	
		if rom == 'I':
			print(bmaj)
		if rom == 'ii':
			print(csharpmin)
		if rom == 'iii':
			print(dsharpmin)
		if rom == 'IV':
			print(emaj)
		if rom == 'V':
			print(fsharpmaj)
		if rom == 'vi':
			print(gsharpmin)
		if rom == 'vii':
			print(asharpdim)
		if rom == 'back':
			count1 = 2
			
def keygsharpmin():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii and ii, enter 'back' to go back): ")
	
		if rom == 'III':
			print(bmaj)
		if rom == 'iv':
			print(csharpmin)
		if rom == 'v':
			print(dsharpmin)
		if rom == 'VI':
			print(emaj)
		if rom == 'VII':
			print(fsharpmaj)
		if rom == 'i':
			print(gsharpmin)
		if rom == 'ii':
			print(asharpdim)
		if rom == 'back':
			count1 = 2

def keyfsharpmaj():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii, enter 'back' to go back): ")
	
		if rom == 'I':
			print(fsharpmaj)
		if rom == 'ii':
			print(gsharpmin)
		if rom == 'iii':
			print(asharpmin)
		if rom == 'IV':
			print(bmaj)
		if rom == 'V':
			print(csharpmaj)
		if rom == 'vi':
			print(dsharpmin)
		if rom == 'vii':
			print(esharpdim)
		if rom == 'back':
			count1 = 2
			
def keydsharpmin():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii and ii, enter 'back' to go back): ")
	
		if rom == 'III':
			print(fsharpmaj)
		if rom == 'iv':
			print(gsharpmin)
		if rom == 'v':
			print(asharpmin)
		if rom == 'VI':
			print(bmaj)
		if rom == 'VII':
			print(csharpmaj)
		if rom == 'i':
			print(dsharpmin)
		if rom == 'ii':
			print(esharpdim)
		if rom == 'back':
			count1 = 2

def keycsharpmaj():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii, enter 'back' to go back): ")
	
		if rom == 'I':
			print(csharpmaj)
		if rom == 'ii':
			print(dsharpmin)
		if rom == 'iii':
			print(esharpmin)
		if rom == 'IV':
			print(fsharpmaj)
		if rom == 'V':
			print(gsharpmaj)
		if rom == 'vi':
			print(asharpmin)
		if rom == 'vii':
			print(bsharpdim)
		if rom == 'back':
			count1 = 2
			
def keyasharpmin():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii and ii, enter 'back' to go back): ")
	
		if rom == 'III':
			print(csharpmaj)
		if rom == 'iv':
			print(dsharpmin)
		if rom == 'v':
			print(esharpmin)
		if rom == 'VI':
			print(fsharpmaj)
		if rom == 'VII':
			print(gsharpmaj)
		if rom == 'vi':
			print(asharpmin)
		if rom == 'ii':
			print(bsharpdim)
		if rom == 'back':
			count1 = 2

def keyfmaj():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii, enter 'back' to go back): ")
	
		if rom == 'I':
			print(fmaj)
		if rom == 'ii':
			print(gmin)
		if rom == 'iii':
			print(amin)
		if rom == 'IV':
			print(bflatmaj)
		if rom == 'V':
			print(cmaj)
		if rom == 'vi':
			print(dmin)
		if rom == 'vii':
			print(edim)
		if rom == 'back':
			count1 = 2
			
def keydmin():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii and ii, enter 'back' to go back): ")
	
		if rom == 'III':
			print(fmaj)
		if rom == 'iv':
			print(gmin)
		if rom == 'v':
			print(amin)
		if rom == 'VI':
			print(bflatmaj)
		if rom == 'VII':
			print(cmaj)
		if rom == 'i':
			print(dmin)
		if rom == 'ii':
			print(edim)
		if rom == 'back':
			count1 = 2

def keybflatmaj():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii, enter 'back' to go back): ")
	
		if rom == 'I':
			print(bflatmaj)
		if rom == 'ii':
			print(cmin)
		if rom == 'iii':
			print(dmin)
		if rom == 'IV':
			print(eflatmaj)
		if rom == 'V':
			print(fmaj)
		if rom == 'vi':
			print(gmin)
		if rom == 'vii':
			print(adim)
		if rom == 'back':
			count1 = 2
			
def keygmin():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii and ii, enter 'back' to go back): ")
	
		if rom == 'III':
			print(bflatmaj)
		if rom == 'iv':
			print(cmin)
		if rom == 'v':
			print(dmin)
		if rom == 'VI':
			print(eflatmaj)
		if rom == 'VII':
			print(fmaj)
		if rom == 'i':
			print(gmin)
		if rom == 'ii':
			print(adim)
		if rom == 'back':
			count1 = 2

def keyeflatmaj():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii, enter 'back' to go back): ")
	
		if rom == 'I':
			print(eflatmaj)
		if rom == 'ii':
			print(fmin)
		if rom == 'iii':
			print(gmin)
		if rom == 'IV':
			print(aflatmaj)
		if rom == 'V':
			print(bflatmaj)
		if rom == 'vi':
			print(cmin)
		if rom == 'vii':
			print(ddim)
		if rom == 'back':
			count1 = 2
			
def keycmin():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii and ii, enter 'back' to go back): ")
	
		if rom == 'III':
			print(eflatmaj)
		if rom == 'iv':
			print(fmin)
		if rom == 'v':
			print(gmin)
		if rom == 'VI':
			print(aflatmaj)
		if rom == 'VII':
			print(bflatmaj)
		if rom == 'i':
			print(cmin)
		if rom == 'ii':
			print(ddim)
		if rom == 'back':
			count1 = 2
			
def keyaflatmaj():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii, enter 'back' to go back): ")
	
		if rom == 'I':
			print(aflatmaj)
		if rom == 'ii':
			print(bflatmin)
		if rom == 'iii':
			print(cmin)
		if rom == 'IV':
			print(dflatmaj)
		if rom == 'V':
			print(eflatmaj)
		if rom == 'vi':
			print(fmin)
		if rom == 'vii':
			print(gdim)
		if rom == 'back':
			count1 = 2

def keyfmin():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii and ii, enter 'back' to go back): ")
	
		if rom == 'III':
			print(aflatmaj)
		if rom == 'iv':
			print(bflatmin)
		if rom == 'v':
			print(cmin)
		if rom == 'VI':
			print(dflatmaj)
		if rom == 'VII':
			print(eflatmaj)
		if rom == 'i':
			print(fmin)
		if rom == 'ii':
			print(gdim)
		if rom == 'back':
			count1 = 2

def keydflatmaj():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii, enter 'back' to go back): ")
	
		if rom == 'I':
			print(dflatmaj)
		if rom == 'ii':
			print(eflatmin)
		if rom == 'iii':
			print(fmin)
		if rom == 'IV':
			print(gflatmaj)
		if rom == 'V':
			print(aflatmaj)
		if rom == 'vi':
			print(bflatmin)
		if rom == 'vii':
			print(cdim)
		if rom == 'back':
			count1 = 2
			
def keybflatmin():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii and ii, enter 'back' to go back): ")
	
		if rom == 'III':
			print(dflatmaj)
		if rom == 'iv':
			print(eflatmin)
		if rom == 'v':
			print(fmin)
		if rom == 'VI':
			print(gflatmaj)
		if rom == 'VII':
			print(aflatmaj)
		if rom == 'i':
			print(bflatmin)
		if rom == 'ii':
			print(cdim)
		if rom == 'back':
			count1 = 2
			
def keygflatmaj():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii, enter 'back' to go back ): ")
	
		if rom == 'I':
			print(gflatmaj)
		if rom == 'ii':
			print(aflatmin)
		if rom == 'iii':
			print(bflatmin)
		if rom == 'IV':
			print(cflatmaj)
		if rom == 'V':
			print(dflatmaj)
		if rom == 'vi':
			print(eflatmin)
		if rom == 'vii':
			print(fdim)
		if rom == 'back':
			count1 = 2
			
def keyeflatmin():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii and ii, enter 'back' to go back ): ")
	
		if rom == 'III':
			print(gflatmaj)
		if rom == 'iv':
			print(aflatmin)
		if rom == 'v':
			print(bflatmin)
		if rom == 'VI':
			print(cflatmaj)
		if rom == 'VII':
			print(dflatmaj)
		if rom == 'i':
			print(eflatmin)
		if rom == 'ii':
			print(fdim)
		if rom == 'back':
			count1 = 2

def keycflatmaj():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii, enter 'back' to go back): ")
	
		if rom == 'I':
			print(cflatmaj)
		if rom == 'ii':
			print(dflatmin)
		if rom == 'iii':
			print(eflatmin)
		if rom == 'IV':
			print(fflatmaj)
		if rom == 'V':
			print(gflatmaj)
		if rom == 'vi':
			print(aflatmin)
		if rom == 'vii':
			print(bflatdim)
		if rom == 'back':
			count1 = 2
			
def keyaflatmin():
	count1 = 1
	while (count1 < 2):
		rom = input("Enter the roman numeral of the chord you want (Ignore the diminished symbol on vii and ii, enter 'back' to go back): ")
	
		if rom == 'III':
			print(cflatmaj)
		if rom == 'iv':
			print(dflatmin)
		if rom == 'v':
			print(eflatmin)
		if rom == 'VI':
			print(fflatmaj)
		if rom == 'VII':
			print(gflatmaj)
		if rom == 'i':
			print(aflatmin)
		if rom == 'ii':
			print(bflatdim)
		if rom == 'back':
			count1 = 2

			

			



 
def main():
	
	
	count = 1
	while (count < 2):
		key = input("Enter the key you're working in(for example, A Major, B Flat Minor, enter 'exit' to quit): ")
		if key == "A Flat Major":
			keyaflatmaj()
		if key == "A Major":
			keyamaj()
		if key == "B Flat Major":
			keybflatmaj()
		if key == "B Major":
			keybmaj()
		if key == "C Major":
			keycmaj()
		if key == "C Sharp Major":
			keycsharpmaj()
		if key == "D Flat Major":
			keydflatmaj()
		if key == "D Major":
			keydmaj()
		if key == "E Flat Major":
			keyeflatmaj()
		if key == "E Major":
			keyemaj()
		if key == "F Major":
			keyfmaj()
		if key == "F Sharp Major":
			keyfsharpmaj()
		if key == "G Major":
			keygmaj()
		if key == "G Flat Major":
			keygflatmaj()
		if key == "C Minor":
			keycmin()
		if key == "G Minor":
			keygmin()
		if key == "D Minor":
			keydmin()
		if key == "A Minor":
			keyamin()
		if key == "E Minor":
			keyemin()
		if key == "B Minor":
			keybmin()
		if key == "F Sharp Minor":
			keyfsharpmin()
		if key == "C Sharp Minor":
			keycsharpmin()
		if key == "G Sharp Minor":
			keygsharpmin()
		if key == "E Flat Minor":
			keyeflatmin()
		if key == "B Flat Minor":
			keybflatmin()
		if key == "F Minor":
			keyfmin()
		if key == 'exit':
			print('Thank you for using this program!')
			count = 2
		
main()
