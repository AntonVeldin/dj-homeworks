import json

from django.core.management import BaseCommand

from school.models import Teacher, Student

# EXISTING_MODELS = {
#     'school.teacher': Teacher,
#     'school.student': Student,
# }

# def handle(self, *args, **options):
#     path = options['path']
#     for each_path in path:
#         with open(each_path, 'r', encoding='utf-8') as file:
#             school = json.load(file)
#             for each_person in school:
#                 person = EXISTING_MODELS[each_person['model']]
#                 person.objects.create(**each_person['fields'])


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'path',
            nargs='*',
            type=str,
        )

    def handle(self, *args, **options):
        path = options['path']
        for each_path in path:
            with open(each_path, 'r', encoding='utf-8') as file:
                school = json.load(file)
                for each_person in school:
                    if each_person['model'] == 'school.teacher':
                        # Хотел универсально развернуть, но не смог
                        # модель препода привязать по id :(
                        # Пришлось в if снова пихать логику
                        Teacher.objects.create(**each_person['fields'])
                    elif each_person['model'] == 'school.student':
                        teacher = Teacher.objects.get(id=each_person['fields']['teacher'])
                        Student.objects.create(
                            name=each_person['fields']['name'],
                            teacher=teacher,
                            group=each_person['fields']['group'],
                        )
