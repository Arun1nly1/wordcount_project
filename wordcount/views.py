from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def count(request):
    words = request.GET["wordbox"]
    print (type(words))
    word_list = words.split()
    worddictionary = {}
    for word in word_list:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word] = 1

    return render(request,'result.html',{'words':words,'count':len(word_list),'worddictionary':worddictionary.items()})
