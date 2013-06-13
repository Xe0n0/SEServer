from django.http import HttpResponse
from django.utils import simplejson
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from models import UserProfile
from SEServer.lib import json_response, auth_required, require_params

@require_POST
@auth_required
@json_response
@require_params(['id'])
def profile(request, id):
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
	user_profile = request.user.profile
	online_list = UserProfile.objects.filter(online=True).filter(~Q(id=request.user.profile.id))

	if online_list.count():

		def best(xprofile, yprofile):
			if not hasattr(xprofile, 'count'):
				xprofile.count = len([tag for tag in xprofile.tag_list() if tag in user_profile.tag_list()])
			yprofile.count = len([tag for tag in yprofile.tag_list() if tag in user_profile.tag_list()])
			if xprofile.count >= yprofile.count:
				return xprofile
			return yprofile

		profile =  reduce(best, online_list)
		return {
			'status': 0,
			'username': profile.user.username,
			'realname': profile.realname,
			'nickname': profile.nickname,
			'tags': profile.tag_list(),
		}

	return {
		'status': 104,
		'user_info': 'no one else out there',
	}


	