from django.http import HttpResponse
from django.shortcuts import render
import string


def homepage(request):
    return render(request , 'homepage.html')

def analyze(request):
    Text = request.POST.get('text' , 'No Text')

    Removepunc = request.POST.get('removepunc' , 'OFF')  
    Capitalize_Characters = request.POST.get('capitalize' , 'OFF')  
    Remove_New_Lines = request.POST.get('removenewline' , 'OFF')  
    Remove_Extra_Spaces = request.POST.get('removeextraspaces' , 'OFF')
    Character_Counter = request.POST.get('charactercounter' , 'OFF')
    # print(Removepunc)
    # print(Text)

    if(Removepunc=="on"):
        punc = string.punctuation
        l1 = list(punc)
        analyzed = ""
        for char in Text:
                if char not in l1:
                    analyzed = analyzed + char

        dict = {"purpose" : "Remove Punctuations" , "analyzed_text" : analyzed}
        Text = analyzed
        # return render(request , 'analyze.html' , dict)

    if(Capitalize_Characters=="on"):
        analyzed = ""
        for char in Text:
            analyzed = analyzed + char.upper()

        dict = {"purpose" : "Capitalize Characters" , "analyzed_text" : analyzed}
        Text = analyzed
        # return render(request , 'analyze.html' , dict)

    if(Remove_New_Lines=="on"):
        analyzed = ""
        for char in Text:
            if(char!="\n" and char!="\r"):
                analyzed = analyzed + char

        dict = {"purpose" : "Remove New Lines" , "analyzed_text" : analyzed}
        Text = analyzed
        # return render(request , 'analyze.html' , dict)

    if(Remove_Extra_Spaces=="on"):
        analyzed = ""
        for index , char in enumerate(Text):
            if(Text[index]==" " and Text[index+1]==" "):
                pass
            else:
                analyzed = analyzed + char

        dict = {"purpose" : "Remove Extra Spaces" , "analyzed_text" : analyzed}
        Text = analyzed
        # return render(request , 'analyze.html' , dict)

    if(Character_Counter=="on"):
        num = len(Text)
        # for index , char in enumerate(Text):
        #     if Text[index]!=" ":
        #         index = index + 1
            
        dict = {"purpose" : "Count Character(No Space Character)","Number":f"The total number of characters are {num}" }

    if(Removepunc!="on" and Capitalize_Characters!="on" and Remove_New_Lines!="on" and Remove_Extra_Spaces!="on" and Character_Counter!="on"):
        return HttpResponse(f"You have not selected any options...Please check again!!!\n{Text}")
       
    return render(request , 'analyze.html' , dict)
