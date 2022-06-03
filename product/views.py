from django.shortcuts import render, redirect

# Create your views here.
from product.models import Category, Drink, Allergy


def home(request):
    return redirect('/product')


def product(request):
    if request.method == 'GET':
        all_category = Category.objects.all()
        return render(request, 'home.html', {'category': all_category})

    elif request.method == 'POST':
        all_category = Category.objects.all()
        category = request.POST.getlist('category[]', '')
        print(category)

        if len(category) == 0:
            all_category = Category.objects.all()
            return render(request, 'home.html', {'error': '카테고리를 선택하세요', 'category': all_category})
        else:
            drinks = Drink.objects.filter(category_id=category[0])
            for i in range(1, len(category)):
                drink = Drink.objects.filter(category_id=category[i])
                drinks = drinks.union(drink)

            return render(request, 'home.html', {'drinks': drinks, 'category': all_category})
