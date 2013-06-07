from django.http import HttpResponse
from django.utils import simplejson
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from models import Activity, ActivityForm
from SEServer.lib import json_response, auth_required
import sys


@require_POST
@auth_required
@json_response
def create(request):
	from datetime import datetime

	form = ActivityForm(request.POST)
	# form.time = datetime.strptime(request.POST.get('time', None), '%Y-%m-%d %H:%M')
	


	if form.is_valid():
		ac = form.save(commit=False)

		ac.organizer = request.user.profile.realname
		ac.save()

		return {
			'status': 0
		}
	return {
		'status': 103,
		'error_info': form.errors,
		'user_info': u'bad parameters',
	}



@require_POST
@auth_required
@json_response
def add_tags(request):
	id = request.POST.get('id', None)
	tags = request.POST.get('tags', None)
	if id is None or tags is None:
		return {
			'status': 103,
			'user_info': u'activity id and tags required',
		}

	try: 
		act = Activity.objects.get(id=id)
		tags = tags.split(',')
		act.tags.add(*tags)
	except:
		return {
			'status': 103,
			'user_info': u'invalid parameters',
		}

	r_tags = map(lambda x: x.name, act.tags.all())

	return {
		'status': 0,
		'tags': r_tags,
	}

@require_POST
@auth_required
@json_response
def all(request):
	

	def tags(array, obj):
		tags = map(lambda x: x.name, obj.tags.all())
		array.update({'tags': tags})
		return array

	array = Activity.objects.all()
	array = map(tags, array.values(), array)
	# print >> sys.stderr, array
	return array