from rest_framework import serializers

from appbook.models import User,ActivityPeriod



class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']

class UserSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'real_name', 'tz','activity_periods']

    def create(self, validated_data):
        tracks_data = validated_data.pop('activity_periods')
        user = User.objects.create(**validated_data)
        print(user)
        for track_data in tracks_data:
            print(track_data)
            try:
                ActivityPeriod.objects.create(user_pk=user, **track_data)
            except Exception as error:
                print(error)
            
        return user


# data = 	{"id": "W07QCRPA4",
# 			"real_name": "Glinda Southgood",
# 			"tz": "Asia/Kolkata",
# 			"activity_periods": [{
# 					"start_time": "Feb 1 2020  1:33PM",
# 					"end_time": "Feb 1 2020 1:54PM"
# 				},
# 				{
# 					"start_time": "Mar 1 2020  11:11AM",
# 					"end_time": "Mar 1 2020 2:00PM"
# 				},
# 				{
# 					"start_time": "Mar 16 2020  5:33PM",
# 					"end_time": "Mar 16 2020 8:02PM"
# 				}
# 			]
# 		}
           
# serializer = UserSerializer(data=data)
# print(serializer.is_valid())
# print(serializer.errors)
# serializer.save()