#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def toComparativeDegree(inputSTR):
    if inputSTR.endswith("i:"):                 #課堂上會說明這一段程式的 .endswith() 是什麼意思，然後執行給同學們看。
        resultSTR = inputSTR[:-2] + "ʲejʃi:"    #課堂上會說明這一段程式的 [:-2] 是什麼意思，然後執行給同學們看。
    return resultSTR


def toPositiveDegree(inputSTR):
    if inputSTR.endswith("ʲejʃi:"):
        resultSTR = inputSTR.replace("ʲejʃi:", "i:")   #課堂上會說明這一段程式的 replace() 是什麼意思，然後執行給同學們看。
    return resultSTR



if __name__ == "__main__":
    #Below are some data from Czech; The superscription j indicates palatalization,
    #and ':' indicates lengthening. (清華大學語言所 110 年入學考試：語言分析)
    #
    # 1. novi:          'new'              5. nevini:        'innocent'
    # 2. nevinʲejʃi:    'more innocent'    6. novʲejʃi:      'more new/newer'
    # 3. mora:lnʲejʃi:  'more moral'       7. nadani:        'gifted'
    # 4. u:plni:        'complate'         8. u:plnʲejʃi:    'more complete'
    #
    #Q1. Given these data, describe the grammatical rule that allows speakers to express
    #    the comparative degree (more X or X-er) of an adjective in Czech.
    #
    #Q2. What are the Czech translations for the English word 'more gifted' and 'moral'
    #    likely to be?

    #A1. 如果一個形容詞的原級是以 i: 結尾，就把 i: 替換成 "ʲejʃi:" 即為其比較級。(程式實作如下)
    adjSTR = "nadani:"
    comparativeSTR = toComparativeDegree(adjSTR)
    print(comparativeSTR)

    #A2. 如果一個形容詞的比較級是以 "ʲejʃi:" 結尾，就把 "ʲejʃi:" 替換成 "i:" 即為原級。(程式實作如下)
    adjSTR = "mora:lnʲejʃi:"
    positiveSTR = toPositiveDegree(adjSTR)
    print(positiveSTR)

    #ps. 恭喜您！您剛剛寫完的程式，就是 Chech 的形容詞級別變化程式。
    #作業就會是類似的題目：
    #e.g., 以下是丹麥文的形容詞：
    # 1. hurtig       'fast'
    # 2. hurtigere    'faster'
    # 3. høj          'tall'
    # 4. højere       'taller'
    # 5. stor         'big'
    # 6. større       'bigger'
    #
    # Q1. 請設計一個程式，可以把丹麥文的 kortere (shorter) 變成原級。
    # Q2. 另，若我們擁有丹麥文更多語料：
    # 7. langsom      'slow'
    # 8. langsommere  'slower'
    # 請調整你的程式，讓它可以把比較級的 langsommere 變為原級的 langsom 而不影響原來的功能。