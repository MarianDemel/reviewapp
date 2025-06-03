from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Place, Review
from .forms import ReviewForm
from django.db import transaction, IntegrityError


def index(request):
    places = Place.objects.all().prefetch_related('review_set')
    return render(request, "hodnoceni/index.html", {"places": places})


def place_detail(request, place_id):
    try:
        place = Place.objects.get(id=place_id)
    except Place.DoesNotExist:
        raise Http404("Place does not exist")

    reviews = Review.objects.filter(place=place)
    return render(request, 'hodnoceni/place_detail.html', {
        'place': place,
        'reviews': reviews
    })


@login_required
def add_review(request, place_id):
    try:
        place = Place.objects.get(id=place_id)
    except Place.DoesNotExist:
        raise Http404("Place does not exist")

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    review = form.save(commit=False)
                    review.place = place
                    review.user = request.user
                    review.save()
                    return redirect('place_detail', place_id=place.id)
            except IntegrityError as e:
                form.add_error(None, "Databázová chyba - ujistěte se, že váš účet existuje a je správně přihlášen.")
    else:
        form = ReviewForm()
    return render(request, 'hodnoceni/add_review.html', {'form': form, 'place': place})