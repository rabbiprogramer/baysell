def index(request):
    name = 'rabbi'
    num_list = [2,3,4,5,6,7,8,]
    my_info = {
        'name':'rabbi hossain',
        'age':17,
        'hight':5.7,
    }

    context = {
        'name':name,
        'age':20,
        'num_list':num_list,
        'my_info':my_info,

    }
    return render(request,'customer/index.html',context)


# Generated by Django 5.0.2 on 2024-03-03 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='birthtime',
            field=models.TimeField(blank=True, null=True),
        ),
    ]


