from django.shortcuts import render
from django.http import JsonResponse

# Hashtag generation logic
def get_hashtags(keyword):
    hashtag_database = {
        'travel': ['#travel', '#wanderlust', '#travelgram', '#vacation', '#explore'],
        'fitness': ['#fitness', '#health', '#gym', '#fitfam', '#workout'],
        'art': ['#art', '#artist', '#painting', '#drawing', '#creative'],
        'movies': ['#movies', '#cinema', '#film', '#moviebuff', '#movienight'],
        'fight': ['#fight', '#mma', '#boxing', '#wrestling', '#combat'],
        'products': ['#products', '#shopping', '#onlineshopping', '#bestproducts', '#productreview']
    }
    return hashtag_database.get(keyword.lower(), [f"#{keyword}", f"#{keyword}Tips", f"#{keyword}Life"])

# Home page view
def index(request):
    return render(request, 'index.html')

# Hashtag generation view
def generate_hashtags(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword', '')
        hashtags = get_hashtags(keyword)
        return JsonResponse({'hashtags': hashtags})
