from django.shortcuts import render
from .models import FreebiesPostDb

# Create your views here.

def makePost(request):
	if request.method == 'POST':
		if request.POST.get('name') and request.POST.get('email') and request.POST.get('number') and request.POST.get('program') and request.POST.get('state') and request.POST.get('country') and request.POST.get('tee_size'):
			post = FreebiesPostDb() #name,email,number,prgram,state,country,tee_size
			post.name = request.POST.get('name')
			post.email = request.POST.get('email')
			post.number = request.POST.get('number')
			post.program = request.POST.get('program')
			post.state = request.POST.get('state')
			post.country = request.POST.get('country')
			post.tee_size = request.POST.get('tee_size')
			#post.ip = request.POST.get('ip')
			post.save()

		#return render(request, 'posts/templates/SignTest.html')
		return render(request, '../templates/FreeTee.html')

	else:
		return render(request, '../templates/FreeTee.html')
		