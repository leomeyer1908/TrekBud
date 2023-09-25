# accounts/views.py
from django.contrib.auth import login, authenticate, get_user_model
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

def send_confirmation_email(request, user):
	current_site = get_current_site(request)
	mail_subject = 'Confirm your email address'
	token = default_token_generator.make_token(user)
	uid = urlsafe_base64_encode(force_bytes(user.pk))
	confirmation_url = reverse('confirm_email', args=[uid, token])
	message = render_to_string('registration/confirmation_email.html', {
		'user': user,
		'domain': current_site.domain,
		'confirmation_url': confirmation_url,
	})
	send_mail(mail_subject, message, 'your_email@gmail.com', [user.email])
	return render(request, 'registration/email_confirmation_sent.html')

def confirm_email(request, uidb64, token):
	User = get_user_model()
	try:
		uid = urlsafe_base64_decode(uidb64).decode()
		user = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

	if user and default_token_generator.check_token(user, token):
		user.email_confirmed = True
		user.save()
		return render(request, 'registration/email_confirmed.html')
	else:
		return render(request, 'registration/invalid_confirmation_link.html')

def registration(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('home')  # Replace 'home' with the URL name for your home page
	else:
		form = RegistrationForm()
	return render(request, 'registration/registration.html', {'form': form})

