import requests
import datetime

# 下週一開始計算
nextMondayDate = datetime.datetime(2022, 7, 18, 0, 0)
url = 'http://140.124.181.95:30200/api/log/record'


labDutyies = [
    {
        "userID":"cfdf18a5-8b8f-4315-82b5-d930811f10e6",
        "title":"4 hour",
        "activityTypeName":"LabProject",
        "startTime": (nextMondayDate+datetime.timedelta(days=0, hours=14, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "endTime": (nextMondayDate+datetime.timedelta(days=0, hours=18, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "description": "",
        "activityUnitID": "3ac3fee8-1ad9-49ac-9c77-e5c7dc28be8f"
    },
    {
        "userID":"cfdf18a5-8b8f-4315-82b5-d930811f10e6",
        "title":"1 hour",
        "activityTypeName":"LabProject",
        "startTime": (nextMondayDate+datetime.timedelta(days=1, hours=11, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "endTime": (nextMondayDate+datetime.timedelta(days=1, hours=12, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "description": "",
        "activityUnitID": "3ac3fee8-1ad9-49ac-9c77-e5c7dc28be8f"
    },
    {
        "userID":"cfdf18a5-8b8f-4315-82b5-d930811f10e6",
        "title":"4 hour",
        "activityTypeName":"LabProject",
        "startTime": (nextMondayDate+datetime.timedelta(days=1, hours=14, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "endTime": (nextMondayDate+datetime.timedelta(days=1, hours=18, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "description": "",
        "activityUnitID": "3ac3fee8-1ad9-49ac-9c77-e5c7dc28be8f"
    },
    {
        "userID":"cfdf18a5-8b8f-4315-82b5-d930811f10e6",
        "title":"2 hour",
        "activityTypeName":"LabProject",
        "startTime": (nextMondayDate+datetime.timedelta(days=2, hours=10, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "endTime": (nextMondayDate+datetime.timedelta(days=2, hours=12, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "description": "",
        "activityUnitID": "3ac3fee8-1ad9-49ac-9c77-e5c7dc28be8f"
    },
    {
        "userID":"cfdf18a5-8b8f-4315-82b5-d930811f10e6",
        "title":"4 hour",
        "activityTypeName":"LabProject",
        "startTime": (nextMondayDate+datetime.timedelta(days=2, hours=14, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "endTime": (nextMondayDate+datetime.timedelta(days=2, hours=18, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "description": "",
        "activityUnitID": "3ac3fee8-1ad9-49ac-9c77-e5c7dc28be8f"
    },
    {
        "userID":"cfdf18a5-8b8f-4315-82b5-d930811f10e6",
        "title":"2 hour",
        "activityTypeName":"LabProject",
        "startTime": (nextMondayDate+datetime.timedelta(days=3, hours=10, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "endTime": (nextMondayDate+datetime.timedelta(days=3, hours=12, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "description": "",
        "activityUnitID": "3ac3fee8-1ad9-49ac-9c77-e5c7dc28be8f"
    },
    {
        "userID":"cfdf18a5-8b8f-4315-82b5-d930811f10e6",
        "title":"3 hour",
        "activityTypeName":"LabProject",
        "startTime": (nextMondayDate+datetime.timedelta(days=3, hours=14, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "endTime": (nextMondayDate+datetime.timedelta(days=3, hours=17, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "description": "",
        "activityUnitID": "3ac3fee8-1ad9-49ac-9c77-e5c7dc28be8f"
    }
]
Others = [
    {
        "userID":"cfdf18a5-8b8f-4315-82b5-d930811f10e6",
        "title":"study group",
        "activityTypeName":"Study Group",
        "startTime": (nextMondayDate+datetime.timedelta(days=1, hours=10, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "endTime": (nextMondayDate+datetime.timedelta(days=1, hours=11, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "description": "",
        "activityUnitID": "cfdf18a5-8b8f-4315-82b5-d930811f10e6"
    },
    {
        "userID":"cfdf18a5-8b8f-4315-82b5-d930811f10e6",
        "title":"clean lab",
        "activityTypeName":"LabDuty",
        "startTime": (nextMondayDate+datetime.timedelta(days=3, hours=17, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "endTime": (nextMondayDate+datetime.timedelta(days=3, hours=18, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "description": "",
        "activityUnitID": "cfdf18a5-8b8f-4315-82b5-d930811f10e6"
    },
    
]
Courses = [
    {
        "userID":"cfdf18a5-8b8f-4315-82b5-d930811f10e6",
        "title":"FSS",
        "activityTypeName":"Courses",
        "startTime": (nextMondayDate+datetime.timedelta(days=0, hours=16, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "endTime": (nextMondayDate+datetime.timedelta(days=0, hours=18, minutes=30)).strftime("%Y/%m/%d %H:%M"),
        "description": "",
        "activityUnitID": "cfdf18a5-8b8f-4315-82b5-d930811f10e6"
    },
    {
        "userID":"cfdf18a5-8b8f-4315-82b5-d930811f10e6",
        "title":"STV",
        "activityTypeName":"Courses",
        "startTime": (nextMondayDate+datetime.timedelta(days=1, hours=9, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "endTime": (nextMondayDate+datetime.timedelta(days=1, hours=10, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "description": "",
        "activityUnitID": "cfdf18a5-8b8f-4315-82b5-d930811f10e6"
    },
    {
        "userID":"cfdf18a5-8b8f-4315-82b5-d930811f10e6",
        "title":"STV",
        "activityTypeName":"Courses",
        "startTime": (nextMondayDate+datetime.timedelta(days=2, hours=13, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "endTime": (nextMondayDate+datetime.timedelta(days=2, hours=15, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "description": "",
        "activityUnitID": "cfdf18a5-8b8f-4315-82b5-d930811f10e6"
    },
    {
        "userID":"cfdf18a5-8b8f-4315-82b5-d930811f10e6",
        "title":"DS",
        "activityTypeName":"Courses",
        "startTime": (nextMondayDate+datetime.timedelta(days=2, hours=15, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "endTime": (nextMondayDate+datetime.timedelta(days=2, hours=18, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "description": "",
        "activityUnitID": "cfdf18a5-8b8f-4315-82b5-d930811f10e6"
    },
    {
        "userID":"cfdf18a5-8b8f-4315-82b5-d930811f10e6",
        "title":"SA",
        "activityTypeName":"Courses",
        "startTime": (nextMondayDate+datetime.timedelta(days=3, hours=9, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "endTime": (nextMondayDate+datetime.timedelta(days=3, hours=12, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "description": "",
        "activityUnitID": "cfdf18a5-8b8f-4315-82b5-d930811f10e6"
    },
    {
        "userID":"cfdf18a5-8b8f-4315-82b5-d930811f10e6",
        "title":"專題討論",
        "activityTypeName":"Courses",
        "startTime": (nextMondayDate+datetime.timedelta(days=3, hours=15, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "endTime": (nextMondayDate+datetime.timedelta(days=3, hours=17, minutes=00)).strftime("%Y/%m/%d %H:%M"),
        "description": "",
        "activityUnitID": "cfdf18a5-8b8f-4315-82b5-d930811f10e6"
    }
]

for activity in labDutyies:
    x = requests.post(url, json = activity)
    print(x)
    
for activity in Others:
    x = requests.post(url, json = activity)
    print(x)
