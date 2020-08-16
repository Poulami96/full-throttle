from rest_framework import serializers

from appbook.models import User,ActivityPeriod



class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']

class UserSerializer(serializers.ModelSerializer):
    tracks = ActivityPeriodSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'real_name', 'tz','tracks']

    def create(self, validated_data):
        tracks_data = validated_data.pop('tracks')
        user = User.objects.create(**validated_data)
        for track_data in tracks_data:
            ActivityPeriod.objects.create(user=user, **track_data)
        return user


# data = {'id': "hghj",
#         "real_name": "Egon Spengler",
#         "tz": "America/Los_Angeles",
#         "tracks": [
# 					{
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
# 				}]
#         }
# serializer = UserSerializer(data=data)
# print(serializer.is_valid())
# serializer.save()