from logic import *
hkb = PropDefiniteKB()

mkb="(FS&O)==>FO; (FS&O)==>SO2; (SO2&O)==>SO3;\
     (SO3&H2O)==>H2SO4; (FO&H2SO4)==>FSO4".split(';')
for s in mkb:
        hkb.tell(expr(s))

for s in "FS;O;H2O".split(';'):
    hkb.tell(expr(s))

print(hkb.clauses)

s=expr('FSO4')
myans=pl_fc_entails(hkb,s)
print(myans)