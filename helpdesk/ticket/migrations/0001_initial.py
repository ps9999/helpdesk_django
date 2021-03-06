# Generated by Django 2.2.10 on 2021-05-29 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=64)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=70)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.CharField(max_length=10)),
                ('status', models.BooleanField(default=True)),
                ('escalation_time', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TicketStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_code', models.CharField(max_length=50)),
                ('issue', models.CharField(max_length=1000)),
                ('level', models.CharField(default='1', max_length=50)),
                ('area', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('email_on_update', models.BooleanField(default=True)),
                ('email_on_closure', models.BooleanField(default=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('on_hold_till', models.PositiveIntegerField(blank=True, null=True)),
                ('corrective_action', models.CharField(blank=True, max_length=500, null=True)),
                ('preventive_action', models.CharField(blank=True, max_length=500, null=True)),
                ('rca_desc', models.CharField(blank=True, max_length=500, null=True)),
                ('status', models.BooleanField(default=True)),
                ('image_description', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ticket/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.Category')),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.Priority')),
                ('ticket_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.TicketStatus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.Department'),
        ),
    ]
