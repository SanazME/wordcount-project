
from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    import re

    fulltext = request.GET['fulltext']
    fulltext_unicode = re.sub(r'\W+', ' ', fulltext) # Exculde alpha_numerics and _ : \W == [^a-zA-Z0-9_]
    wordlist = fulltext_unicode.split()
    word_frequency_dict = word_frequency(wordlist)
    #wordlist = fulltext.split()

    # order in descending order (input: list of tuples of (key, value))
    sorted_words = sorted(word_frequency_dict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist), 'worddictionary':word_frequency_dict, 'sorted_words': sorted_words})

def about(request):
    return render(request, 'about.html')

def word_frequency(wordlist):
    word_frequency_dict={}
    for word in wordlist:
        if word not in word_frequency_dict:
            word_frequency_dict[word] = 0
        else:
            word_frequency_dict[word] += 1
    return word_frequency_dict
