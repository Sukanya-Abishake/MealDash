# Generated by Django 3.2.4 on 2021-09-26 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0004_delete_restaurant'),
        ('restaurant_management', '0004_auto_20210926_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=120)),
                ('actual_price', models.FloatField(max_length=15)),
                ('final_price', models.FloatField(max_length=15)),
                ('type', models.DateTimeField(choices=[('custom', 'custom'), ('default', 'Default')], default='default', max_length=15)),
                ('status', models.CharField(max_length=15)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal_plan', to='restaurant_management.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=120)),
                ('actual_price', models.FloatField(max_length=15)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custmer_item', to='user_management.customer')),
                ('mealplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mealplan_item', to='restaurant_management.mealplan')),
            ],
        ),
    ]
