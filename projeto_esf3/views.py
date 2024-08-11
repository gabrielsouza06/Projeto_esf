from django.contrib.auth.models import Group

def create_groups():
    groups = ['Paciente', 'Profissional']
    for group_name in groups:
        Group.objects.get_or_create(name=group_name)
