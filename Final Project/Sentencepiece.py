# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 18:20:05 2022

@author: Bryant & Wade
"""

import sentencepiece as spm


def get_models():
    spm.SentencePieceTrainer.Train(input="Es_clean.txt", model_prefix='es', vocab_size = 8000)
    spm.SentencePieceTrainer.Train(input="Pl_clean.txt", model_prefix='pl', vocab_size= 12000)
    
#get_models()


def tokenize(file, src_lang):
    
    if src_lang == "Pl":
        sp = spm.SentencePieceProcessor(model_file="pl.model")
    elif src_lang == "Es":
        sp = spm.SentencePieceProcessor(model_file="es.model")
    else:
        raise ValueError("language given not in domain")
    
    with open(file, 'r', encoding = "utf-8") as myfile:
        data = myfile.readlines()
        print(len(data))
        
    for i in range(len(data)):
        data[i] = " ".join(sp.encode(data[i], out_type=str))+"\n"
        if i ==0:
            print(data[i])
    
    with open(src_lang+"_tok.txt", 'w', encoding = "utf-8") as outfile:
        outfile.writelines(data)
        
        
        
def untokenize(file, src_lang):
    if src_lang == "Pl":
        sp = spm.SentencePieceProcessor(model_file="Multi Model/Sentencepiece built on/pl2.model")
    elif src_lang == "Es":
        sp = spm.SentencePieceProcessor(model_file="es.model")
    else:
        raise ValueError("language given not in domain")
        
    with open(file, 'r', encoding = "utf-8") as myfile:
        data = myfile.readlines()
        print(len(data))
        
    for i in range(len(data)):
        data[i] = sp.decode(data[i].split())+"\n"
        if i ==0:
            print(data[i])
        
    with open(src_lang+"_OUT.txt", 'w', encoding = "utf-8") as outfile:
        outfile.writelines(data)

if __name__ == "__main__":
    #untokenize("tgt-test.txt", "Es")
    pass
    
