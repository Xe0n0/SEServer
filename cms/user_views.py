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

from django.db.models import Q

@require_POST
@auth_required
@json_response
def random(request):
	online_list = UserProfile.objects.filter(online=True).filter(~Q(id=request.user.profile.id))
	from random import randint
	if online_list.count():
		i = randint(0, online_list.count()-1)
		profile = online_list[i]
		return {
			'status': 0,
			'username': profile.user.username,
			'realname': profile.realname,
			'nickname': profile.nickname,
		}

	return {
		'status': 104,
		'user_info': 'no one else out there',
	}

@require_POST
@auth_required
@json_response
def first(request):
	online_list = UserProfile.objects.filter(online=True).filter(~Q(id=request.user.profile.id))
	from random import randint
	if online_list.count():
		profile = online_list[0]
		return {
			'status': 0,
			'username': profile.user.username,
			'realname': profile.realname,
			'nickname': profile.nickname,
		}

	return {
		'status': 104,
		'user_info': 'no one else out there',
	}


	