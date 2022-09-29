import random
elements = [ 
['H', 'hydrogen','1'],
['He', 'helium', '2'],
['Li', 'lithium','3'],
['Be', 'beryllium','4'],
['B', 'boron','5'],
['C', 'carbon', '6'],
['N', 'nitrogen', '7'],
['O', 'oxygen', '8'],
['F', 'fluorine', '9'],
['Ne', 'neon','10'],
['Na', 'sodium','11'],
['Mg', 'magnesium','12'],
['Al', 'aluminium','13'],
['Si', 'sillicon','14'],
['P', 'phosphorus','15'],
['S', 'sulphur','16'],
['Cl', 'chlorine','17'],
['Ar', 'argon','18'],
['K', 'potassium','19'],
['Ca', 'calcium','20'],
['Sc', 'scandium','21'],
['Ti', 'titanium','22'],
['V', 'vanadium','23'],
['Cr', 'chromium','24'],
['Mn', 'maganese','25'],
['Fe', 'iron','26'],
['Co', 'cobalt','27'],
['Ni', 'nickel','28'],
['Cu', 'copper','29'],
['Zn', 'zinc','30'],
['Ga', 'gallium','31'],
['Ge', 'germanium','32'],
['As', 'arsenic','33'],
['Se', 'selenium','34'],
['Br', 'bromine','35'],
['Kr', 'krypton','36'],
['Rb', 'rubidium','37'],
['Sr', 'strontium','38'],
['Y', 'yittrium','39'],
['Zr', 'zirconium','40'],
['Nb', 'niobium','41'],
['Mb', 'molybdenum','42'],
['Tc', 'technetium','43'],
['Ru', 'ruthenium','4 4'],
['Rh', 'rhodium','45'],
['Pd', 'palladium','46'],
['Ag', 'silver','47'],
['Cd', 'cadmium','48'],
['In', 'indium','49'],
['Sn', 'tin','50'],
['Sb', 'antimony','51'],
['Te', 'tellurium','52'],
['I', 'iodine','53'],
['Xe', 'xenon','54'],
['Cs', 'caesium','55'],
['Ba', 'barium','56'],
['La', 'lanthanum','57'],
['Ce', 'cerium','58'],
['Pr', 'praseodymium','59'],
['Nd','neodymium','60'],
['Pm','promethium','61'],
['Sm','samarium','62'],
['Eu','europium','63'],
['Gd','gadolinium','64'],
['Tb','terbium','65'],
['Dy','dysprosium','66'],
['Ho','holmium','67'],
['Er','erbium','68'],
['Tm','thulium','69'],
['Yb','ytterbium','70'],
['Lu','lutetium','71'],
['Hf','hafnium','72'],
['Ta','tantalum','73'],
['W','tungsten','74'],
['Re','rhenium','75'],
['Os','osmium','76'],
['Ir','iridium','77'],
['Pt','platinum','78'],
['Au','gold','79'],
['Hg','mercury','80'],
['Tl','thallium','81'],
['Pb','lead','82'],
['Bi', 'bismuth','83'],
['Po','polonium','84'],
['At','astatine','85'],
['Rn','radon','86'],
['Fr','francium','87'],
['Ra','radium','88'],
['Ac','actinium','89'],
['Th','thorium','90'],
['Pa','protactinium','91'],
['U','uranium','92'],
['Np','neptunium','93'],
['Pu','plutonium','94'],
['Am','americium','95'],
['Cm','curium','96'],
['Bk','berkelium','97'],
['Cf','californium','98'],
['Es','einsteinium','99'],
['Fm','fermium','100'],
['Md','mendelevium','101'],
['No','nobelium','102'],
['Lr','lawrencium','103'],
['Rf','rutherfordium','104'],
['Db','dubnium','105'],
['Sg','seaborgium','106'],
['Bh','bohrium','107'],
['Hs','hassium','108'],
['Mt','meitnerium','109'],
['Ds','darmstadtium','110'],
['Rg','roentgenium','111'],
['Cn','copernicium','112'],
['Nh','nihonium','113'],
['Fl','flerovium','114'],
['Mc','moscovium','115'],
['Lv','livermorium','116'],
['Ts','tennessine','117'],
['Og','oganesson','118'],
]

ezelements = [ 
['H', 'hydrogen','1'],
['He', 'helium', '2'],
['Li', 'lithium','3'],
['Be', 'beryllium','4'],
['B', 'boron','5'],
['C', 'carbon', '6'],
['N', 'nitrogen', '7'],
['O', 'oxygen', '8'],
['F', 'fluorine', '9'],
['Ne', 'neon','10'],
['Na', 'sodium','11'],
['Mg', 'magnesium','12'],
['Al', 'aluminium','13'],
['Si', 'sillicon','14'],
['P', 'phosphorus','15'],
['S', 'sulphur','16'],
['Cl', 'chlorine','17'],
['Ar', 'argon','18'],
['K', 'potassium','19'],
['Fe', 'iron','26'],
['Co', 'cobalt','27'],
['Ni', 'nickel','28'],
['Cu', 'copper','29'],
['Zn', 'zinc','30'],
['Ga', 'gallium','31'],
['As', 'arsenic','33'],
['Ag', 'silver','47'],
['Sn', 'tin','50'],
['Sb', 'antimony','51'],
['I', 'iodine','53'],
['Xe', 'xenon','54'],
['Pt','platinum','78'],
['Au','gold','79'],
['Hg','mercury','80'],
]
score = 0
questions = 0
startgame = input('Do you want to play(P) or use the periodic table(T)?')

if startgame.lower()[0] == 'p':
  knows_to_play = input('Do you know how to play?')
  if knows_to_play.lower()[0] == 'n':
    print('Welcome to the periodic table quiz!')
    print('')
    print('How to play:')
    print('Difficulty 1: Gives you an element symbol, and you must give the element name')
    print('')
    print('Difficulty 2: The same as difficulty 1 but it also asks you for the atomic number')
    print('')
    print('Difficulty 3: Gives you the atomic number and you have to give the element name and symbol')
    print('')
    print('Modes: Endless mode will give you a never-ending quiz, set question count will let you choose how many questions you have.')
    print('')
    print('All answers are not case sensitive, and simply type quit at any time to stop the game and get your score.')
    
  difficulty = input('Choose difficulty, 1, 2 or 3 ')
  mode = input('Choose mode, endless (E), or set question count, (S)')

  if mode.lower() == 'e':

    if difficulty == '1':
      while True:
        randel = random.randint(0,117)
        print(elements[randel][0])
        answer = input('')

        if answer.lower() == elements[randel][1]:
          print('you shine bright like a diamond!')
          score += 1
          questions += 1

        elif answer.lower() == 'quit':
          print('You got ' + str(score) + ' out of ' + str(questions))
          break

        else:
          print("Wrongdont give up on yourselve, it's "+ elements[randel][1])
          questions += 1

    elif difficulty == '2':
      while True:
        randel = random.randint(0,117)
        print(elements[randel][0])
        answer = input('')

        if answer.lower() == elements[randel][1]:
          print('spectacular done!')
          score += 1
          questions += 1
          answer = input('Atomic number:')

          if answer.lower() == elements[randel][2]:
            print('Your amma and appa is proud!')
            score += 1
            questions += 1

          elif answer.lower() == 'quit':
            print('You got ' + str(score) + ' out of ' + str(questions))
            break

          else:
            print("Wrong, it's " + elements[randel][2])
            questions += 1

        elif answer.lower() == 'quit':
          print('You got ' + str(score) + ' out of ' + str(questions))
          break

        else:
          print("Wrong, it's "+ elements[randel][1])
          questions += 1

    elif difficulty == '3':
      while True:
        randel = random.randint(0,117)
        print(elements[randel][2])
        answer = input('')

        if answer.lower() == elements[randel][1]:
          print('wow this is excellent!')
          score += 1
          questions += 1
          answer = input('Symbol:')

          if answer.lower() == elements[randel][0].lower():
            print('Your the ronaldo of sceince.....siuuuuu!')
            score += 1
            questions += 1

          elif answer.lower() == 'quit':
            print('You got ' + str(score) + ' out of ' + str(questions))
            break

          else:
            print("Wrong, it's " + elements[randel][0])
            questions += 1

        elif answer.lower() == 'quit':
          print('You got ' + str(score) + ' out of ' + str(questions))
          break

        else:
          print("Wrong, it's "+ elements[randel][1])
          questions += 1

  if mode.lower() == 's':
    questioncount = int(input('How many questions?'))
    if difficulty == '1':
      for i in range(0,questioncount):
        randel = random.randint(0,117)
        print(elements[randel][0])
        answer = input('')

        if answer.lower() == elements[randel][1]:
          print('Correct! Your parents are proud of YOU!')
          score += 1
          questions += 1

        elif answer.lower() == 'quit':
          print('You got ' + str(score) + ' out of ' + str(questions))
          break

        else:
          print("Wrong,dont give up try again it's accually "+ elements[randel][1])
          questions += 1
      print('You got ' + str(score) + ' out of ' + str(questions))
      

    elif difficulty == '2':
      for i in range(0,questioncount):
        randel = random.randint(0,117)
        print(elements[randel][0])
        answer = input('')

        if answer.lower() == elements[randel][1]:
          print('Well done its the correct answer')
          score += 1
          questions += 1
          answer = input('Atomic number:')

          if answer.lower() == elements[randel][2]:
            print('you really challenged yourself!')
            score += 1
            questions += 1

          elif answer.lower() == 'quit':
            print('You got ' + str(score) + ' out of ' + str(questions))
            break

          else:
            print("Wrong, it's " + elements[randel][2])
            questions += 1

        elif answer.lower() == 'quit':
          print('You got ' + str(score) + ' out of ' + str(questions))
          break

        else:
          print("Wrong, it's "+ elements[randel][1])
          questions += 1
      print('You got ' + str(score) + ' out of ' + str(questions))
      

    elif difficulty == '3':
      for i in range(0,questioncount):
        randel = random.randint(0,117)
        print(elements[randel][2])
        answer = input('')

        if answer.lower() == elements[randel][1]:
          print('well done ur parents are proud!')
          score += 1
          questions += 1
          answer = input('Symbol:')

          if answer.lower() == elements[randel][0].lower:
            print('I knew you could do it!')
            score += 1
            questions += 1

          elif answer.lower() == 'quit':
            print('You got ' + str(score) + ' out of ' + str(questions))
            break

          else:
            print("Wrong, it's " + elements[randel][0])
            questions += 1

        elif answer.lower() == 'quit':
          print('You got ' + str(score) + ' out of ' + str(questions))
          break

        else:
          print("Wrong, it's "+ elements[randel][1])
          questions += 1
      print('You got ' + str(score) + ' out of ' + str(questions))
    

elif startgame.lower() == 't':
  while True:
    searchfor = input('Input any element information:Symbol, name or atomic number     ')

    print()
    for e in elements:
      for info in e:
        if info.lower()[:len(searchfor)]==searchfor.lower():
          print(e[0],e[1],e[2])
          break
    print()

    for e in elements:
      for info in e:
        if info.lower().find(searchfor.lower())!=-1:
          print(e[0] + ' ' + e[1] + ' ' +  e[2])
          break
    print()
else:
  print('Ok, quitting....see you again next time!')
