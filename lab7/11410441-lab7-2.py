from logic import*

fam_kb = FolKB(
    map(expr, ['Child(gc,p) & Child(p,gp)==>Grandchild(gc,gp)',
               'Child(gcc,p) & Child(p,gp) & Child(gp,ggp)\
                ==>Greatgrandparent(ggp,ggc)',

                'Husband(h,w) & Sister(w,x)==>BrotherInLaw(h,x)',
                'Child(cl,p) & Child(c2,p)==>Sibling(c1,c2)',
                'Sibling(x,y) & Child(cx,x) & Child(cy,y)\
                ==>Cousin(cx,xy)',
                'Child(Elizabeth,George)',

                'Child(Charles,Elizabeth)','Child(Anne,Elizabeth)',
                'Child(Andrew,Elizabeth)','Child(Edward,Elizabeth)',

                'Child(William,Charles)','Child(Harry,Charles)',
                'Child(Pete,Anne)','Child(Zara,Anne)',
                'Child(Beatrice,Andrew)','Child(Eugenie,Andrew)',
                'Child(Louise,Edward)','Child(James,Edward)',

                'Husband(Mark,Anne)','Sister(Anne,Diana)',
                ]))

print("Who are Elizabeth's grandchildren?")
print(fam_kb.ask(expr('Grandchild(x,Elizabeth)'))[x])
print("Who are Zara's great grandparents?")
print(fam_kb.ask(expr('Greatgrandparent(x,Zara)'))[x])
print("Who are Diana's Brothers-In-Law?")
print(fam_kb.ask(expr('BrotherInLaw(x,Diana)'))[x])
print("Who are Anne's cousins?")
print(fam_kb.ask(expr('Cousin(x, Anne)'))[x])