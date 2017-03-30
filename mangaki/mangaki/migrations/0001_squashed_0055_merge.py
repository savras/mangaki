# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 20:41
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.migrations.operations.special
import django.db.models.deletion
from django.utils.timezone import utc


def add_categories(apps, schema_editor):
    Category = apps.get_model("mangaki", "Category")
    Category.objects.bulk_create([
        Category(slug='anime', name="Anime"),
        Category(slug='manga', name="Manga"),
        Category(slug='album', name="Album"),
    ])


def create_stafftype(apps, schema_editor):
    Role = apps.get_model("mangaki", "Role")
    Role.objects.create(name="Scénariste", slug="writer")
    Role.objects.create(name="Mangaka", slug="mangaka")
    Role.objects.create(name="Auteur", slug="author")
    Role.objects.create(name="Compositeur", slug="composer")
    Role.objects.create(name="Réalisateur", slug="director")


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(db_index=True, max_length=10)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.RunPython(
            code=add_categories,
            reverse_code=django.db.migrations.operations.special.RunPython.noop,
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=32, null=True)),
                ('last_name', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('text', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=33)),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=17)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField()),
                ('markdown', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_shared', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('avatar_url', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('mal_username', models.CharField(blank=True, default='', max_length=64, null=True)),
                ('nsfw_ok', models.BooleanField(default=False)),
                ('reco_willsee_ok', models.BooleanField(default=False)),
                ('score', models.IntegerField(default=0)),
                ('newsletter_ok', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('source', models.CharField(blank=True, max_length=1044)),
                ('poster', models.CharField(max_length=128)),
                ('date', models.DateField(blank=True, null=True)),
                ('nsfw', models.BooleanField(default=False)),
                ('synopsis', models.TextField(blank=True, default='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangaki.Category')),
                ('controversy', models.FloatField(blank=True, default=0)),
                ('nb_dislikes', models.IntegerField(blank=True, default=0)),
                ('nb_likes', models.IntegerField(blank=True, default=0)),
                ('nb_ratings', models.IntegerField(blank=True, default=0)),
                ('sum_ratings', models.FloatField(blank=True, default=0)),
                ('studio', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mangaki.Studio')),
                ('editor', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mangaki.Editor')),
                ('vgmdb_aid', models.IntegerField(blank=True, null=True)),
                ('anidb_aid', models.IntegerField(blank=True, default=0)),
                ('catalog_number', models.CharField(blank=True, max_length=20)),
                ('manga_type', models.TextField(blank=True, choices=[('seinen', 'Seinen'), ('shonen', 'Shonen'), ('shojo', 'Shojo'), ('yaoi', 'Yaoi'), ('sonyun-manhwa', 'Sonyun-Manhwa'), ('kodomo', 'Kodomo'), ('ecchi-hentai', 'Ecchi-Hentai'), ('global-manga', 'Global-Manga'), ('manhua', 'Manhua'), ('josei', 'Josei'), ('sunjung-sunjeong', 'Sunjung-Sunjeong'), ('chungnyun', 'Chungnyun'), ('yuri', 'Yuri'), ('dojinshi-parodie', 'Dojinshi-Parodie'), ('manhwa', 'Manhwa'), ('yonkoma', 'Yonkoma')], max_length=16)),
                ('vo_title', models.CharField(blank=True, max_length=128)),
                ('anime_type', models.TextField(blank=True, max_length=42)),
                ('nb_episodes', models.TextField(blank=True, default='Inconnu', max_length=16)),
                ('origin', models.CharField(blank=True, choices=[('japon', 'Japon'), ('coree', 'Coree'), ('france', 'France'), ('chine', 'Chine'), ('usa', 'USA'), ('allemagne', 'Allemagne'), ('taiwan', 'Taiwan'), ('espagne', 'Espagne'), ('angleterre', 'Angleterre'), ('hong-kong', 'Hong Kong'), ('italie', 'Italie'), ('inconnue', 'Inconnue'), ('intl', 'International')], default='', max_length=10)),
                ('genre', models.ManyToManyField(to='mangaki.Genre')),
            ],
        ),
        migrations.AlterIndexTogether(
            name='work',
            index_together=set([('category', 'nb_ratings'), ('category', 'controversy')]),
        ),
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('work_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mangaki.Work')),
                ('deprecated_composer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='composed', to='mangaki.Artist')),
                ('deprecated_director', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='directed', to='mangaki.Artist')),
                ('deprecated_anime_type', models.TextField(default='', max_length=42)),
                ('deprecated_author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='authored', to='mangaki.Artist')),
                ('deprecated_editor', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mangaki.Editor')),
                ('deprecated_genre', models.ManyToManyField(to='mangaki.Genre')),
                ('deprecated_nb_episodes', models.TextField(default='Inconnu', max_length=16)),
                ('deprecated_origin', models.CharField(choices=[('japon', 'Japon'), ('coree', 'Coree'), ('france', 'France'), ('chine', 'Chine'), ('usa', 'USA'), ('allemagne', 'Allemagne'), ('taiwan', 'Taiwan'), ('espagne', 'Espagne'), ('angleterre', 'Angleterre'), ('hong-kong', 'Hong Kong'), ('italie', 'Italie'), ('inconnue', 'Inconnue'), ('intl', 'International')], default='', max_length=10)),
                ('deprecated_studio', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mangaki.Studio')),
                ('deprecated_anidb_aid', models.IntegerField(default=0)),
            ],
            bases=('mangaki.work',),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('favorite', 'Mon favori !'), ('like', "J'aime"), ('dislike', "Je n'aime pas"), ('neutral', 'Neutre'), ('willsee', 'Je veux voir'), ('wontsee', 'Je ne veux pas voir')], max_length=8)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangaki.Work')),
                ('date', models.DateField(auto_now=True, default=datetime.datetime(2016, 4, 9, 14, 0, 22, 626332, tzinfo=utc))),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set([('user', 'work')]),
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('problem', models.CharField(choices=[('title', "Le titre n'est pas le bon"), ('poster', 'Le poster ne convient pas'), ('synopsis', 'Le synopsis comporte des erreurs'), ('author', "L'auteur n'est pas le bon"), ('composer', "Le compositeur n'est pas le bon"), ('double', 'Ceci est un doublon'), ('nsfw', "L'oeuvre est NSFW"), ('n_nsfw', "L'oeuvre n'est pas NSFW"), ('ref', 'Proposer une URL (myAnimeList, AniDB, Icotaku, VGMdb, etc.)')], default='ref', max_length=8, verbose_name='Partie concernée')),
                ('message', models.TextField(blank=True, verbose_name='Proposition')),
                ('is_checked', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangaki.Work')),
            ],
        ),
        migrations.CreateModel(
            name='Neighborship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=3, max_digits=8)),
                ('neighbor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neighbor', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('work_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mangaki.Work')),
                ('deprecated_vo_title', models.CharField(max_length=128)),
                ('deprecated_editor', models.CharField(max_length=32)),
                ('deprecated_origin', models.CharField(choices=[('japon', 'Japon'), ('coree', 'Coree'), ('france', 'France'), ('chine', 'Chine'), ('usa', 'USA'), ('allemagne', 'Allemagne'), ('taiwan', 'Taiwan'), ('espagne', 'Espagne'), ('angleterre', 'Angleterre'), ('hong-kong', 'Hong Kong'), ('italie', 'Italie'), ('inconnue', 'Inconnue'), ('intl', 'International')], max_length=10)),
                ('deprecated_manga_type', models.TextField(blank=True, choices=[('seinen', 'Seinen'), ('shonen', 'Shonen'), ('shojo', 'Shojo'), ('yaoi', 'Yaoi'), ('sonyun-manhwa', 'Sonyun-Manhwa'), ('kodomo', 'Kodomo'), ('ecchi-hentai', 'Ecchi-Hentai'), ('global-manga', 'Global-Manga'), ('manhua', 'Manhua'), ('josei', 'Josei'), ('sunjung-sunjeong', 'Sunjung-Sunjeong'), ('chungnyun', 'Chungnyun'), ('yuri', 'Yuri'), ('dojinshi-parodie', 'Dojinshi-Parodie'), ('manhwa', 'Manhwa'), ('yonkoma', 'Yonkoma')], max_length=16)),
                ('deprecated_genre', models.ManyToManyField(to='mangaki.Genre')),
                ('deprecated_mangaka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drew', to='mangaki.Artist')),
                ('deprecated_writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wrote', to='mangaki.Artist')),
            ],
            bases=('mangaki.work',),
        ),
        migrations.CreateModel(
            name='SearchIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128)),
                ('poster', models.CharField(blank=True, max_length=128, null=True)),
                ('mal_id', models.IntegerField(blank=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangaki.Work')),
            ],
        ),
        migrations.CreateModel(
            name='Pairing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangaki.Artist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangaki.Work')),
                ('is_checked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=512)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangaki.Work')),
                ('suggestions', models.ManyToManyField(blank=True, to='mangaki.Suggestion')),
            ],
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('score', models.FloatField()),
                ('nb_ratings', models.PositiveIntegerField()),
                ('nb_stars', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Top',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('category', models.CharField(choices=[('directors', 'Réalisateurs'), ('authors', 'Auteurs'), ('composers', 'Compositeurs')], max_length=10, unique_for_date='date')),
                ('contents', models.ManyToManyField(through='mangaki.Ranking', to='contenttypes.ContentType')),
            ],
        ),
        migrations.AddField(
            model_name='ranking',
            name='top',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangaki.Top'),
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('work_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mangaki.Work')),
                ('deprecated_catalog_number', models.CharField(max_length=20)),
                ('deprecated_vgmdb_aid', models.IntegerField(blank=True, null=True)),
                ('deprecated_composer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='composer', to='mangaki.Artist')),
            ],
            bases=('mangaki.work',),
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('album', models.ManyToManyField(to='mangaki.Album')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangaki.Artist')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangaki.Role')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangaki.Work')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='staff',
            unique_together=set([('work', 'artist', 'role')]),
        ),
        migrations.AddField(
            model_name='work',
            name='artists',
            field=models.ManyToManyField(blank=True, through='mangaki.Staff', to='mangaki.Artist'),
        ),
        migrations.RunPython(
            code=create_stafftype,
            reverse_code=django.db.migrations.operations.special.RunPython.noop,
        ),
        migrations.CreateModel(
            name='ArtistSpelling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('was', models.CharField(db_index=True, max_length=255)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangaki.Artist')),
            ],
        ),
    ]