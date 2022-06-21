# Generated by Django 4.0.4 on 2022-06-19 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0010_osservatorio_star_citizen'),
    ]

    operations = [
        migrations.AddField(
            model_name='episodio',
            name='descrizione_html',
            field=models.TextField(blank=True, help_text="Testo che riassume l'episodio (HTML)", null=True, verbose_name='Descrizione (HTML)'),
        ),
        migrations.AddField(
            model_name='episodio',
            name='descrizione_txt',
            field=models.TextField(blank=True, help_text="Testo che riassume l'episodio (TXT)", null=True, verbose_name='Descrizione (TXT)'),
        ),
    ]
