w_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True :
    s = input()
    
    if s == '#' :
        break
    s = s.replace(' ', '')
    s = s.replace(',', '')
    s = s.replace('.', '')
    s = s.replace('!', '')
    s = s.replace('?', '')
    
    str = list(s)
    
    vowel = [w for w in str if w in w_list]
    print(len(vowel))
