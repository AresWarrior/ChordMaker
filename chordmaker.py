class Key():
    def __init__(self,name,i,ii,iii,iv,v,vi,vii):
        self.name = name
        self.i = i
        self.ii = ii
        self.iii = iii
        self.iv = iv
        self.v = v
        self.vi = vi
        self.vii = vii
    def printKey(self):
        print(self.i,self.ii,self.iii,self.iv,self.v,self.vi,self.vii)
    def printChord(self,ui):
        if ui == 'i':
            print(self.i,self.iii,self.v)
        if ui == 'ii':
            print(self.ii,self.iv,self.vi)
        if ui == 'iii':
            print(self.iii,self.v,self.vii)
        if ui == 'iv':
            print(self.iv,self.vi,self.i)
        if ui == 'v':
            print(self.v,self.vii,self.ii)
        if ui == 'vi':
            print(self.vi,self.i,self.iii)
        if ui == 'vii':
            print(self.vii,self.ii,self.iv)


def main():
    print('Welcome to the Chord Maker!')
    cmajor = Key('C Major','C','D','E','F','G','A','B')
    gmajor = Key('G Major','G','A','B','C','D','E','F#')
    dmajor = Key('D Major','D','E','F#','G','A','B','C#')
    amajor = Key('A Major','A','B','C#','D','E','F#','G#')
    emajor = Key('E Major','E','F#','G#','A','B','C#','D#')
    bmajor = Key('B Major','B','C#','D#','E','F#','G#','A#')
    fsharpmajor = Key('F# Major','F#','G#','A#','B','C#','D#','E#')
    csharpmajor = Key('C# Major','C#','D#','E#','F#','G#','A#','B#')
    aminor = Key('A Minor','A','B','C','D','E','F','G')
    eminor = Key('E Minor','E','F#','G','A','B','C','D')
    bminor = Key('B Minor','B','C#','D','E','F#','G','A')
    fsharpminor = Key('F# Minor','F#','G#','A','B','C#','D','E')
    csharpminor = Key('C# Minor','C#','D#','E','F#','G#','A','B')
    gsharpminor = Key('G# Minor','G#','A#','B','C#','D#','E','F#')
    dsharpminor = Key('D# Minor','D#','E#','F#','G#','A#','B','C#')
    asharpminor = Key('A# Minor','A#','B#','C#','D#','E#','F#','G#')
    fmajor = Key('F Major','F','G','A','Bb','C','D','E')
    bflatmajor = Key('Bb Major','Bb','C','D','Eb','F','G','A')
    eflatmajor = Key('Eb Major','Eb','F','G','Ab','Bb','C','D')
    aflatmajor = Key('Ab Major','Ab','Bb','C','Db','Eb','F','G')
    dflatmajor = Key('Db Major','Db','Eb','F','Gb','Ab','Bb','C')
    gflatmajor = Key('Gb Major','Gb','Ab','Bb','Cb','Db','Eb','F')
    cflatmajor = Key('Cb Major','Cb','Db','Eb','Fb','Gb','Ab','Bb')
    dminor = Key('D Minor','D','E','F','G','A','Bb','C')
    gminor = Key('G Minor','G','A','Bb','C','D','Eb','F')
    cminor = Key('C Minor','C','D','Eb','F','G','Ab','Bb')
    fminor = Key('F Minor','F','G','Ab','Bb','C','Db','Eb')
    bflatminor = Key('Bb Minor','Bb','C','Db','Eb','F','Gb','Ab')
    eflatminor = Key('Eb Minor','Eb','F','Gb','Ab','Bb','Cb','Db')
    aflatminor = Key('Ab Minor','Ab','Bb','Cb','Db','Eb','Fb','Gb')
    while True:
        thekeyin = input('What key do you want to work with? (Enter quit to quit): ')
        thekey = thekeyin.lower()
        if thekey == 'c major':
            while True:
                print('C Major')
                ui = input('What chord would you like? (Enter back to go back): ')
                if ui == 'back':
                    break
                else:
                    cmajor.printChord(ui)
        if thekey == 'g major':
            while True:
                print('G Major')
                ui = input('What chord would you like? (Enter back to go back): ')
                if ui == 'back':
                    break
                else:
                    gmajor.printChord(ui)
        if thekey == 'd major':
            while True:
                print('D Major')
                ui = input('What chord would you like? (Enter back to go back): ')
                if ui == 'back':
                    break
                else:
                    dmajor.printChord(ui)
        if thekey == 'a major':
            while True:
                print('A Major')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    amajor.printChord(ui)
        if thekey == 'e major':
            while True:
                print('E Major')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    emajor.printChord(ui)
        if thekey == 'b major':
            while True:
                print('B Major')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    bmajor.printChord(ui)
        if thekey == 'f sharp major' or thekey == 'f# major':
            while True:
                print('A Major')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    fsharpmajor.printChord(ui)
        if thekey == 'c sharp major' or thekey == 'c# major':
            while True:
                print('C# Major')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    csharpmajor.printChord(ui)
        if thekey == 'a minor':
            while True:
                print('A Minor')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    aminor.printChord(ui)
        if thekey == 'e minor':
            while True:
                print('E Minor')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    eminor.printChord(ui)
        if thekey == 'b minor':
            while True:
                print('B Minor')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    bminor.printChord(ui)
        if thekey == 'f sharp minor' or thekey == 'f# minor':
            while True:
                print('F# Minor')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    fsharpminor.printChord(ui)
        if thekey == 'c sharp minor' or thekey == 'c# minor':
            while True:
                print('C# Minor')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    csharpminor.printChord(ui)
        if thekey == 'g sharp minor' or thekey == 'g# minor':
            while True:
                print('G# Minor')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    gsharpminor.printChord(ui)
        if thekey == 'd sharp minor' or thekey == 'd# minor':
            while True:
                print('D# Minor')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    dsharpminor.printChord(ui)
        if thekey == 'e sharp minor' or thekey == 'e# minor':
            while True:
                print('E# Minor')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    esharpminor.printChord(ui)
        if thekey == 'a sharp minor' or thekey == 'a# minor':
            while True:
                print('A# Minor')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    asharpminor.printChord(ui)
        if thekey == 'f major':
            while True:
                print('F Major')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    fmajor.printChord(ui)
        if thekey == 'b flat major' or thekey == 'bb major':
            while True:
                print('Bb Major')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    bflatmajor.printChord(ui)
        if thekey == 'e flat major' or thekey == 'eb major':
            while True:
                print('Eb Major')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    eflatmajor.printChord(ui)
        if thekey == 'a flat major' or thekey == 'ab major':
            while True:
                print('Ab Major')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    aflatmajor.printChord(ui)
        if thekey == 'd flat major' or thekey == 'db major':
            while True:
                print('Db Major')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    dflatmajor.printChord(ui)
        if thekey == 'g flat major' or thekey == 'gb major':
            while True:
                print('Gb Major')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    gflatmajor.printChord(ui)
        if thekey == 'c flat major' or thekey == 'cb major':
            while True:
                print('Cb Major')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    cflatmajor.printChord(ui)
        if thekey == 'd minor':
            while True:
                print('D Minor')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    dminor.printChord(ui)
        if thekey == 'g minor':
            while True:
                print('G Minor')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    gminor.printChord(ui)
        if thekey == 'c minor':
            while True:
                print('C Minor')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    cminor.printChord(ui)
        if thekey == 'f minor':
            while True:
                print('F Minor')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    fminor.printChord(ui)
        if thekey == 'b flat minor' or thekey == 'bb minor':
            while True:
                print('Bb Minor')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    bflatminor.printChord(ui)
        if thekey == 'e flat minor' or thekey == 'eb minor':
            while True:
                print('Eb Minor')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    eflatminor.printChord(ui)
        if thekey == 'a flat minor' or thekey == 'ab minor':
            while True:
                print('Ab Minor')
                uiin = input('What chord would you like? (Enter back to go back): ')
                ui = uiin.lower()
                if ui == 'back':
                    break
                else:
                    aflatminor.printChord(ui)
        if thekey == "quit":
            break
    print('Thank you, and goodbye!')
main()
