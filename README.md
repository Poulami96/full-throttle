
Objective: 
*To design and implement a Django application with User and ActivityPeriod models 
*To write a custom management command to populate the database with some dummy data 
*To design an API to serve that data in the json format given in the link.


Deployed on AWS: http://13.235.50.137:8000/

Implementation:
*Used Class based nested serializers for fetching nested json data.
Serializers allow complex data such as querysets and model instances
to be converted to native Python datatypes that can then be easily
rendered into JSON, XML or other content types.

*Used rest_framework for generics for ListView and other features.
The generic views provided by REST framework allow you to quickly 
build API views that map closely to your database models.