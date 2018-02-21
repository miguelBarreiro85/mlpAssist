# Generated by Django 2.0.2 on 2018-02-06 18:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topico_text', models.CharField(max_length=50)),
                ('descricao_text', models.CharField(max_length=200)),
                ('pub_date', models.DateField(verbose_name=django.utils.timezone.now)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('foto', models.FileField(blank=True, upload_to='')),
                ('pago_bol', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido_text', models.CharField(max_length=200)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('foto', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_text', models.CharField(max_length=50)),
                ('telefone_text', models.IntegerField()),
                ('email_text', models.EmailField(max_length=254)),
                ('assistencias', models.ManyToManyField(blank=True, to='assistencias.Assistencia')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca_text', models.CharField(max_length=200)),
                ('numserie_text', models.CharField(max_length=200)),
                ('descricao_text', models.CharField(max_length=200)),
                ('assistencias', models.ManyToManyField(blank=True, related_name='assistencias', to='assistencias.Assistencia')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assistencias.Pessoa'),
        ),
        migrations.AddField(
            model_name='assistencia',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to='assistencias.Pessoa'),
        ),
        migrations.AddField(
            model_name='assistencia',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funcionario', to='assistencias.Pessoa'),
        ),
        migrations.AddField(
            model_name='assistencia',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assistencias.Produto'),
        ),
    ]