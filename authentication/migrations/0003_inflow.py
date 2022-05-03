# Generated by Django 4.0.4 on 2022-04-20 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_bankcard_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inflow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('registered_at', models.DateTimeField()),
                ('registered_by', models.CharField(max_length=55)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authentication.category')),
            ],
        ),
    ]