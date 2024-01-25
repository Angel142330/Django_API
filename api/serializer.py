from rest_framework import serializers
from .models import Programador

class ProgramadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programador
        #fields = ('name', 'age','language')
        fields = '__all__'
        #read_only_fields = ('name', )
        
        