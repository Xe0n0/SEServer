from django.http import HttpResponse
from django.utils import simplejson
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from models import UserProfile
from SEServer.lib import json_response, auth_required

@require_POST
@auth_required
@json_response
def profile(request):
	id = request.POST.get('id', None)
	if id is None:
		return {
			'status': 103,
			'user_info': u'user id required',
		}

	try:
		user = User.objects.get(id = id)
		profile = user.profile

		if profile is None:
			return {
				'status': 105,
				'user_info': u'bad user profile',
			}

	except:
		return {
			'status': 103,
			'user_info': u'invalid user id',
		}

	return {
		'id': user.id,
		'username': user.username,
		'realname': profile.realname,
		'nickname': profile.nickname,
		'age': profile.age,
		'gender': profile.gender,
		'tags': list(profile.tags.all()),
	}
