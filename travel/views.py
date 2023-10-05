# travel/views.py
from django.shortcuts import render
from .forms import RegionSelectionForm

def select_region(request):
	if request.method == 'POST':
		form = RegionSelectionForm(request.POST)
		if form.is_valid():
			selected_region = form.cleaned_data['selected_region']

			user_profile = request.user.userprofile  # Assuming a OneToOneField to the user profile
			user_profile.selected_region = selected_region
			user_profile.save()

			return redirect('profile')
	else:
		form = RegionSelectionForm()

	return render(request, 'travel/select_region.html', {'form': form})

