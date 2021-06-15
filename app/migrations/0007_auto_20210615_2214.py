# Generated by Django 3.2.3 on 2021-06-15 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210615_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Copie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('note', models.IntegerField()),
                ('isvalidated', models.BooleanField()),
                ('subi3eme', models.BooleanField()),
                ('idepreuve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.epreuve')),
                ('matricule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.candidat')),
            ],
        ),
        migrations.AddField(
            model_name='specialite',
            name='ep1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='specialite',
            name='ep2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='specialite',
            name='ep3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='table_inter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_copie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.copie')),
                ('id_correcteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.correcteur')),
            ],
        ),
    ]
