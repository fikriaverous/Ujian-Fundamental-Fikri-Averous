# NOMOR 1========================================================================================

def calculate_years(principal, interest, tax, desire) :
    year = 0
    while principal < desire :
        principal = principal + (principal * interest) - ((principal * interest) * tax)
        year += 1
    
    return year

print(calculate_years(1000,0.05,0.18,1100))
print(calculate_years(1200,0.17,0.05,2000))
print(calculate_years(1500,0.07,0.6,5000))

# NOMOR 2========================================================================================

def expandedform(num):
    if num < 100:
        sisa = num%10
        return print(f'{num-sisa} + {sisa}')
    elif num < 1000:
        sisa_ratusan = num%100
        sisa_puluhan = sisa_ratusan%10
        return print(f'{num-sisa_ratusan} + {sisa_ratusan-sisa_puluhan} + {sisa_puluhan}')
    elif num < 100000:
        # sisa_ratus_ribuan = num%100000
        sisa_puluh_ribuan = num%10000
        sisa_ribuan = sisa_puluh_ribuan%1000
        sisa_ratusan = sisa_ribuan%100
        sisa_puluhan = sisa_ratusan%10
        return print(f'{num-sisa_puluh_ribuan} + {sisa_puluh_ribuan-sisa_ribuan} + {sisa_ribuan-sisa_ratusan} + {sisa_ratusan-sisa_puluhan} + {sisa_puluhan}')

expandedform(70304)

# NOMOR 3========================================================================================

def tower_builder(lantai, besar_lantai):
    lebar, tinggi = besar_lantai
    z = ''
    for item in range(lantai):
        for item1 in range(tinggi):
            for item2 in range((lebar * (lantai - item)) - lebar):
                z += ' ' 
            for item3 in range(lebar + (item * (lebar * 2))):
                z += '*'
            z += '\n'
    print(z)

tower_builder(3,(2,3))