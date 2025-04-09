from django.shortcuts import render

# Create your views here.
def Menu(request):
    about_content = {'menu': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."} 
    return render(request, "menu.html", {'content': about_content}) ### Here we have to access the key for the content dict
def About(request):
    about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. "}
    return render(request, 'about.html', about_content) ### here we only have to specify the about content dict
##### That's why the templates differ and why it was like it was on coursera
#### With 
