# Generated by Django 3.2.16 on 2023-02-18 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.CharField(max_length=225)),
                ('date', models.CharField(max_length=225)),
                ('status', models.CharField(max_length=225)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bouti.user')),
                ('sizechart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bouti_sizechart')),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.CharField(max_length=225)),
                ('dqty', models.CharField(max_length=225)),
                ('amount', models.CharField(max_length=225)),
                ('image', models.CharField(max_length=1000)),
                ('details', models.CharField(max_length=2000)),
                ('size_details', models.CharField(max_length=2000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bouti.category')),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=225)),
                ('password', models.CharField(max_length=225)),
                ('usertype', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='sizechart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=225)),
                ('status', models.CharField(max_length=225)),
                ('design', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bouti.design')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=225)),
                ('lname', models.CharField(max_length=225)),
                ('place', models.CharField(max_length=225)),
                ('phone', models.CharField(max_length=225)),
                ('email', models.CharField(max_length=225)),
                ('address', models.CharField(max_length=225)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bouti.login')),
            ],
        ),
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bouti.design')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bouti.user')),
            ],
        ),
        migrations.CreateModel(
            name='refer_no',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refer_no', models.CharField(max_length=225)),
                ('date', models.CharField(max_length=225)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bouti.booking')),
            ],
        ),
        migrations.CreateModel(
            name='purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=225)),
                ('amount', models.CharField(max_length=225)),
                ('date', models.CharField(max_length=1000)),
                ('details', models.CharField(max_length=2000)),
                ('design', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bouti.design')),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=225)),
                ('date', models.CharField(max_length=225)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bouti.booking')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=225)),
                ('date', models.CharField(max_length=225)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bouti.user')),
            ],
        ),
        migrations.CreateModel(
            name='customised_design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=225)),
                ('cd_name', models.CharField(max_length=225)),
                ('details', models.CharField(max_length=225)),
                ('amount', models.CharField(max_length=225)),
                ('date', models.CharField(max_length=1000)),
                ('status', models.CharField(max_length=2000)),
                ('orderid', models.CharField(max_length=2000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bouti.user')),
            ],
        ),
        migrations.CreateModel(
            name='cpayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camount', models.CharField(max_length=225)),
                ('cdate', models.CharField(max_length=225)),
                ('customised_design', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bouti.customised_design')),
            ],
        ),
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.CharField(max_length=225)),
                ('reply', models.CharField(max_length=225)),
                ('date', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bouti.user')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='sizechart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bouti.sizechart'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bouti.user'),
        ),
        migrations.CreateModel(
            name='bchild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.CharField(max_length=225)),
                ('bamt', models.CharField(max_length=225)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bouti.booking')),
                ('design', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bouti.design')),
            ],
        ),
    ]
