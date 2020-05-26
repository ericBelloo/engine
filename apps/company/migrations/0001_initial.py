# Generated by Django 3.0.5 on 2020-04-28 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('constitutive_act', models.FileField(upload_to='')),
                ('estate', models.FileField(upload_to='')),
                ('tax_certificate', models.FileField(upload_to='')),
                ('proof_of_address', models.FileField(upload_to='')),
                ('bank_account', models.FileField(upload_to='')),
                ('sat', models.FileField(upload_to='')),
                ('employer_registration', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('create_at', models.DateField(auto_now=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('business_name', models.CharField(max_length=100)),
                ('rfc', models.CharField(max_length=50)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utils.Address')),
                ('document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Document')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]