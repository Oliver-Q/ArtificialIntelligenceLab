from utils import expr


def OriKnowBase():

    okb = expr('(BU1==>~G1)&(BU3==>~G3)')

    okb= okb & expr('N1==>G1')
    okb= okb & expr('N2==>G2')
    okb= okb & expr('N3==>G3')
    okb= okb & expr('N4==>G4')
    okb= okb & expr('N5==>(G2&G4&G5)')
    
    okb= okb & expr('BR1==>(~G1|~G5|~G9)') # left might be dangerous
    okb= okb & expr('BR2==>(~G2|~G5|~G9)')
    okb= okb & expr('BR3==>(~G3|~G5|~G9)')
    okb= okb & expr('BR4==>(~G4|~G5|~G9)')
    return okb
    okb= okb & expr('BR5==>(~G1|~G2|~G3|~G4|~G5)')
'''    
    okb= okb & expr('S1==>(~G1|~G5|~G9)') #can't go left
    okb= okb & expr('S2==>(~G2|~G5|~G9)')
    okb= okb & expr('S3==>(~G3|~G5|~G9)')
    okb= okb & expr('S4==>(~G4|~G5|~G9)')
    okb= okb & expr('S5==>(~G1|~G2|~G3|~G4|~G5)')
    return okb
'''



