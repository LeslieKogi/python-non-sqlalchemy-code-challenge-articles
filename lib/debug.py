#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")
    
    author1=Author("Halo")
    magazine1=Magazine("The Inn","Hospitality")

    article1=Article(author1,magazine1,"Gilmore girls")
    article2=Article(author1,magazine1,"Jess Marianos show")
    article3=Article(author1,magazine1,"yass Jess")

    # don't remove this line, it's for debugging!
    ipdb.set_trace()

  
    
