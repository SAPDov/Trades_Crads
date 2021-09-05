from django.shortcuts import render


# Create your views here.
def info(request):
	return render(request, "pages/info.html")


def about(Request):
	pass
	#inherite from the card model and insert some details on the episode and so on..

