API Documention
========

* API prefix: `162.105.74.252:8082/SEServer/`, so method `login` has url  162.105.74.252:8082/SEServer/login

* All method shall be accessed with POST method

* All results returned in JSON format with status 0 indicates a successful request and status > 0 indicates error occurred and 'user_info' gives the reason.


## user auth

### login

#### parameters

* `username`: string
* `password`: string

#### return value

* success

		{
		    "status": 0
		}
* error
	* status `101`: bad username or password
	* example
	
			{
			    "status": 101,
			    "user_info": "bad username or password"
			}
		
### register
#### parameters
* `username`: string
* `password`: string
* `age`: integer
* `gender`: integer, 0 indicates male
* `realname`: string
* `nickname`: string

#### return value
* success 

		{
		    "status": 0
		}
		
* error
	* status `103`: username used
	
## user profile 

### profile 
`login required`

#### parameters
no parameters required

#### return value
* success

		{
		    "status": 0,
		    "realname": "罗宇香",
		    "tags": [],
		    "gender": 1,
		    "age": 21,
		    "nickname": "罗"
		}
* error
	* status `104`: login required or bad profile

### add_tags
`login required`
#### parameters
* `tags`: string separated by ',', eg. 'handsome,hentai'

### return value
* success 

		{
		    "status": 0,
		    "tags": [
		        "hentai",
		        "handsome"
		    ]
		}

* error
	* status `103`: tags required
	
### user/profile
`login required`
#### parameters
* `tags`: string separated by ',', eg. 'handsome,hentai'
* `id`: integer
#### return value
* success

		{
		    "username": "luo",
		    "realname": "罗宇香",
		    "tags": [
		        null,
		        null
		    ],
		    "gender": 1,
		    "age": 21,
		    "nickname": "罗",
		    "id": 5
		}
* error
	* status `103`: user id required or invalid user id,
	* status `105`: bad user profile,

## Activity
### activity/all
`login required`
#### parameters
no parameter required

#### return value
* success

		[
		    {
		        "subtitle": "u'软工开会'",
		        "title": "u'开会'",
		        "tags": [
		            "罗宇香",
		            "SE"
		        ],
		        "content": "u'软工第一次会议'",
		        "location": "u'1131'",
		        "time": "2013-05-31T13:00:00",
		        "organizer": "u'罗宇香'",
		        "id": 1
		    },
		    {
		        "subtitle": "u'软工聚餐'",
		        "title": "u'吃饭'",
		        "tags": [],
		        "content": "u'软工第一次聚餐'",
		        "location": "u'1132'",
		        "time": "2013-05-31T18:00:00",
		        "organizer": "u'罗宇香'",
		        "id": 2
		    }
		]
		
### activity/add_tags
`login required`
#### parameters
`id`: integer
`tags`: string separated by ',', eg. 'meeting,software engineering'

#### return value

* success

		[
		    {
		        "subtitle": "u'软工开会'",
		        "title": "u'开会'",
		        "tags": [
		            "罗宇香",
		            "SE"
		        ],
		        "content": "u'软工第一次会议'",
		        "location": "u'1131'",
		        "time": "2013-05-31T13:00:00",
		        "organizer": "u'罗宇香'",
		        "id": 1
		    },
		    {
		        "subtitle": "u'软工聚餐'",
		        "title": "u'吃饭'",
		        "tags": [],
		        "content": "u'软工第一次聚餐'",
		        "location": "u'1132'",
		        "time": "2013-05-31T18:00:00",
		        "organizer": "u'罗宇香'",
		        "id": 2
		    }
		]
* error
	* status `103`: invalid parameters
	