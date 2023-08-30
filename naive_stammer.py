import pprint as pp

noun_1aoj = ["а"],["ы"],["е"],["у"],["ой","ою"],["е"]

noun_1aej = ["а"],["ы"],["е"],["у"],["eй","eю"],["е"]

noun_1aiej = ["а"],["и"],["е"],["у"],["eй","eю"],["е"]

noun_1aioj = ["а"],["и"],["е"],["у"],["ой","ою"],["е"]


noun_1ja =["я"],["и"],["е"],["ю"],["ей","ею"],["е"]

noun_1jajo =["я"],["и"],["е"],["ю"],["ёй","ёю"],["е"]


noun_1ka =["ка"],["ки"],["ке"],["ку"],["кой","кою"],["ке"]

noun_1ija =["ия"],["ии"],["ии"],["ию"],["ией"],["ии"]

noun_2jja = ["й"],["я"],["ю"],["я"],["ем"],["е"]

noun_2jj = ["й"],["я"],["ю"],["й"],["ем"],["е"]

noun_2ok = ["ок"],["ка"],["ку"],["ок"],["ком"],["ке"]

noun_2softja = ["ь"],["я"],["ю"],["я"],["ём"],["е"]

noun_2softsoft = ["ь"],["я"],["ю"],["ь"],["ем"],["е"]

noun_2softsoftjom = ["ь"],["я"],["ю"],["ь"],["ём"],["е"]

noun_2 = [""],["а"],["у"],[""],["ом"],["е"]

noun_2tsa = ["ец"],["ца"],["цу"],["ец"],["цем"],["це"]

noun_2u = [""],["а"],["у"],[""],["ом"],["е","у"]

noun_second_declension_em = [""],["а"],["у"],[""],["ем"],["е"] #овощ

noun_2o = ["о"],["а"],["у"],["о"],["ом"],["е"]

noun_2e = ["е"],["я"],["ю"],["е"],["ем"],["е"]

noun_2ije = ["ие"],["ия"],["ию"],["ие"],["ием"],["ии"]


noun_3soft = ["ь"],["и"], ["и"],["ь"],["ью"],["и"]

change_y_i_if = "гкхжшщч"

noun_mixed_mja =["мя"],["мени"], ["мени"],["мя"],["менем"],["мени"]






noun_plural = ["а" ,"я","ы" ,"и"],["cons", "ов" ,"ев","ей"],["ам" ,"ям"],["cons","а" ,"я","ы" ,"и","ей"],["ами" ,"ями"],["ах" ,"ях"]


adj_singular = ["ой", "ий", "ый", "ая", "яя", "ое", "ее"],["ого", "его", "ой", "ей"],["ому", "ему", "ой", "ей"],\
    ["ой", "ий", "ый", "ую", "юю", "ое", "ее","ого", "его", "ой", "ей"] ,["ой" ,"ей","им" ,"ым"],["ой" ,"ей","ом" ,"ем"]

adj_plural = ["ые" ,"ие"],["ых" ,"их"],["ым" ,"им"],["ые" ,"ие","ых" ,"их"],["ыми" ,"ими"],["ых" ,"их"]


endings = {"1aoj" : noun_1aoj,
            "1aej" : noun_1aej,
            "1aiej" : noun_1aiej,
            "1ja" : noun_1ja,
            "1ka" : noun_1ka,
            "1ija" : noun_1ija,
            "2jj" : noun_2jj,
            "2softsoft" : noun_2softsoft,
            "2ok" :noun_2ok,
            "2" : noun_2,
            "2tsa" : noun_2tsa,
            "2em" : noun_second_declension_em,#noun_1aiej
             "2o" :noun_2o,
            "2e" : noun_2e,
            "2ije" : noun_2ije,
            "3soft" : noun_3soft,
            "mixed_mja" : noun_mixed_mja,
}

case_names = ["nominative" , "genitive", "dative" , "accusative", "instrumentative", "prepositive"]

case_question = ["есть" , "нет", "рад" , "вижу", "любуюсь", "думаю о "]

word = "табачникова"
#word = "человек"
word = "овощем"
def naive_cases(word, endings):
    variants = []
    for declension,cases in endings.items():
        for n, case in enumerate(cases):
            for ending in case :
                if word[-len(ending):] == ending:
                    root = word[:-len(ending)]
                    variants.append((case_question[n],word,root + "|" + cases[0][0], case_names[n] , declension))
                elif ending == "":
                    root = word
                    variants.append((case_question[n],word, root + "|" + cases[0][0], case_names[n],declension))

    return variants


pp.pprint ( naive_cases(word,endings) )
