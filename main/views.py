from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Word
from django.core.paginator import Paginator, EmptyPage

def getVoice(word):
    firstVowel = "ሀለሐመሠረሰሸቀቐበቨተቸኀነኘአከኸወዐዘዠየደዸጀገጘጠጨጰጸፀፈፐ"
    secondVowel = "ሁሉሑሙሡሩሱሹቁቑቡቩቱቹኁኑኙኡኩኹዉዑዙዡዩዱዹጁጉጙጡጩጱጹፁፉፑ"
    thirdVowel = "ሂሊሒሚሢሪሲሺቂቒቢቪቲቺኂኒኚኢኪኺዊዒዚዢዪዲዺጂጊጚጢጪጲጺፂፊፒ"
    fourthVowel = "ሃላሓማሣራሳሻቃቓባቫታቻኃናኛኣካኻዋዓዛዣያዳዻጃጋጛጣጫጳጻፃፋፓ"
    fifthVowel = "ሄሌሔሜሤሬሴሼቄቔቤቬቴቼኄኔኜኤኬኼዌዔዜዤዬዴዼጄጌጜጤጬጴጼፄፌፔ"
    sixthVowel = "ህልሕምሥርስሽቅቕብቭትችኅንኝእክኽውዕዝዥይድዽጅጝግጥጭጵጽፅፍፕ"
    seventhVowel = "ሆሎሖሞሦሮሶሾቆቖቦቮቶቾኆኖኞኦኮኾዎዖዞዦዮዶዾጆጎጞጦጮጶጾፆፎፖ"

    if word[-1] in firstVowel:
        voice="አ"
    elif word[-1] in secondVowel:
        voice="ኡ"
    elif word[-1] in thirdVowel:
        voice="ኢ"
    elif word[-1] in fourthVowel:
        voice="ኣ"
    elif word[-1] in fifthVowel:
        voice="ኤ"
    elif word[-1] in sixthVowel:
        voice="እ"
    elif word[-1] in seventhVowel:
        voice="ኦ"
    else:
        voice=""

    return voice

def paginate(request, query_set, page_num):
    p = Paginator(query_set, int(page_num))
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    return page

def index(request):
    page = {}
    searchVal = request.GET.get("search")
    if request.method == "GET":
        if searchVal:
            if request.GET.get("type")=="last":
                words = Word.objects.filter(last_word=searchVal[-1])
            elif request.GET.get("type")=="second":
                if len(searchVal)<2:
                    return render(request, "main/home.html")
                words = Word.objects.filter(second_last_word=searchVal[-2], last_word=searchVal[-1])
            elif request.GET.get("type")=="voice":
                words = Word.objects.filter(sound=getVoice(searchVal))
            else:
                words = {}

            page = paginate(request, words, 200)

            return render(request, "main/home.html", {"words":page})

    return render(request, "main/home.html", {"words":page})

def search(request):
    return JsonResponse("granted", safe=False)
