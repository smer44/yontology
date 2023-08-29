rules = [
    "PPLoc.place : в|на  adjective.prepositive* noun.prepositive",
    "PPLoc.place : y|около|возле|вокруг|впереди|сзади  adjective.genitive * noun.genitive",
    "PPLoc.place : над|под adjective.instrumentative* noun.instrumentative",

    "PPLoc.target : в|на  adjective.accusative* noun.accusative",
    "PPLoc.source : из|от  adjective.genitive* noun.genitive",

    "NounAttrPost.genitive :    adjective.genitive* noun.genitive",
#можно также с моим другом, атрибут может быть местоимением
    "PPInst.instrumentative :  c?  attribut.instrumentative* noun.instrumentative",

    "PPContent<prepositive> : o adjective<prepositive>* noun<prepositive>"

]



