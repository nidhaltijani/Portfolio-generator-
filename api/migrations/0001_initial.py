# Generated by Django 4.1.4 on 2022-12-09 19:12

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(default='name@xyz.com', max_length=254, unique=True)),
                ('password', models.CharField(default='', max_length=40)),
                ('username', models.CharField(default='', max_length=40)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('philosophy_statement', models.CharField(default='', max_length=50)),
                ('about', models.TextField(blank=True, null=True)),
                ('usr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'portfolio',
            },
        ),
        migrations.CreateModel(
            name='work_experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poste', models.CharField(default='', max_length=50)),
                ('organization', models.CharField(default='', max_length=50)),
                ('start_date', models.DateField(default=datetime.date(2022, 1, 1))),
                ('end_date', models.DateField(default=datetime.date(2022, 1, 1))),
                ('portoflio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.portfolio')),
            ],
            options={
                'db_table': 'work_experience',
            },
        ),
        migrations.CreateModel(
            name='volunteering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poste', models.CharField(default='', max_length=50)),
                ('organization', models.CharField(default='', max_length=50)),
                ('start_date', models.DateField(default=datetime.date(2022, 1, 1))),
                ('end_date', models.DateField(default=datetime.date(2022, 1, 1))),
                ('portoflio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.portfolio')),
            ],
            options={
                'db_table': 'volunteering',
            },
        ),
        migrations.CreateModel(
            name='social_accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(default='', max_length=500)),
                ('github', models.CharField(blank=True, default='', max_length=500)),
                ('linkedin', models.CharField(default='', max_length=500)),
                ('website', models.CharField(blank=True, default='', max_length=500)),
                ('google', models.CharField(blank=True, default='', max_length=500)),
                ('portoflio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.portfolio')),
            ],
            options={
                'db_table': 'social_accounts',
            },
        ),
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('tool', models.CharField(blank=True, max_length=50)),
                ('portoflio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.portfolio')),
            ],
            options={
                'db_table': 'skill',
            },
        ),
        migrations.CreateModel(
            name='recommendationLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.TextField(default='')),
                ('date_of_letter', models.DateField(default=datetime.date(2022, 1, 1))),
                ('writer', models.CharField(default='', max_length=50)),
                ('occupation', models.CharField(default='', max_length=50)),
                ('portoflio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.portfolio')),
            ],
            options={
                'db_table': 'recommendation_letter',
            },
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=100)),
                ('date_creation', models.CharField(default='', max_length=100)),
                ('visual_demo', models.FileField(upload_to='Project/demo')),
                ('portoflio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.portfolio')),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('birthday', models.DateField(default=datetime.date(2000, 1, 1))),
                ('phone_number', models.PositiveIntegerField(default=99999999)),
                ('photo', models.ImageField(upload_to='photos/users')),
                ('usr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='professionalAccomplishment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('summary', models.CharField(default='', max_length=500)),
                ('justification', models.FileField(upload_to='pro_accomp/justifications')),
                ('date_a', models.DateField(default=datetime.date(2022, 1, 1))),
                ('accomp_type', models.CharField(choices=[('advising', 'Spirit category'), ('partnering', 'Pioneer category'), ('examining', 'Commitment category')], default='advising', max_length=100)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.portfolio')),
            ],
            options={
                'db_table': 'professional_Accomplishment',
            },
        ),
        migrations.CreateModel(
            name='motivationLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.TextField(default='')),
                ('date_of_letter', models.DateField(default=datetime.date(2022, 1, 1))),
                ('portfolio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.portfolio')),
            ],
            options={
                'db_table': 'motivation_letter',
            },
        ),
        migrations.CreateModel(
            name='language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('typeoflanguage', models.CharField(choices=[('0', 'No Proficiency'), ('1', 'Elementary Proficiency'), ('2', 'Limited Working Proficiency'), ('3', 'Professional Working Proficiency'), ('4', 'Full Professional Proficiency'), ('5', 'Native / Bilingual Proficiency')], default='0', max_length=30)),
                ('portoflio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.portfolio')),
            ],
            options={
                'db_table': 'language',
            },
        ),
        migrations.CreateModel(
            name='formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('establishment', models.CharField(default='', max_length=50)),
                ('country_establishment', models.CharField(default='', max_length=50)),
                ('start_date', models.DateField(default=datetime.date(2022, 1, 1))),
                ('end_date', models.DateField(default=datetime.date(2023, 1, 1))),
                ('portoflio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.portfolio')),
            ],
            options={
                'db_table': 'formation',
            },
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('feedback', models.CharField(default='', max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
        migrations.CreateModel(
            name='certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('organization', models.CharField(default='', max_length=50)),
                ('certification_type', models.CharField(choices=[('comp', 'completion'), ('ach', 'achievement'), ('pro', 'professional')], default='comp', max_length=50)),
                ('portoflio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.portfolio')),
            ],
            options={
                'db_table': 'certificate',
            },
        ),
        migrations.CreateModel(
            name='award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('summary', models.CharField(default='', max_length=500)),
                ('justification', models.FileField(upload_to='pro_accomp/justifications')),
                ('date_a', models.DateField(default=datetime.date(2022, 1, 1))),
                ('recognition', models.CharField(choices=[('nat', 'national recognition'), ('inter', 'international recognition')], default='nat', max_length=100)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.portfolio')),
            ],
            options={
                'db_table': 'award',
            },
        ),
    ]
