from rest_framework import serializers

from classes.models import Classroom


class ClassroomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = [ 'year', 'subject', 'teacher']



class ClassroomDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['name', 'year', 'subject', 'teacher']


class UpdateClassroomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['name', 'year', 'subject','teacher']


class CreateClassroomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['name', 'year', 'subject',]