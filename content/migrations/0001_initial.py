# Generated by Django 5.2.4 on 2025-07-22 02:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CategoriaNoticia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Nombre"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="Versión del nombre apta para URLs.",
                        max_length=120,
                        unique=True,
                        verbose_name="Slug",
                    ),
                ),
            ],
            options={
                "verbose_name": "Categoría de Noticia",
                "verbose_name_plural": "Categorías de Noticias",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Noticia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=200, verbose_name="Título")),
                (
                    "slug",
                    models.SlugField(max_length=220, unique=True, verbose_name="Slug"),
                ),
                ("contenido", models.TextField(verbose_name="Contenido")),
                (
                    "estado",
                    models.CharField(
                        choices=[("BORRADOR", "Borrador"), ("PUBLICADA", "Publicada")],
                        db_index=True,
                        default="BORRADOR",
                        max_length=20,
                        verbose_name="Estado",
                    ),
                ),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
                ("fecha_modificacion", models.DateTimeField(auto_now=True)),
                (
                    "fecha_publicacion",
                    models.DateTimeField(
                        blank=True,
                        help_text="Si se deja en blanco, no se mostrará como publicada.",
                        null=True,
                        verbose_name="Fecha de Publicación",
                    ),
                ),
                (
                    "autor",
                    models.ForeignKey(
                        limit_choices_to={"is_staff": True},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="noticias_creadas",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "categoria",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="noticias",
                        to="content.categorianoticia",
                    ),
                ),
            ],
            options={
                "verbose_name": "Noticia",
                "verbose_name_plural": "Noticias",
                "ordering": ["-fecha_publicacion"],
            },
        ),
        migrations.CreateModel(
            name="ComentarioNoticia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "contenido",
                    models.TextField(verbose_name="Contenido del Comentario"),
                ),
                (
                    "aprobado",
                    models.BooleanField(
                        default=True,
                        help_text="Los administradores pueden desactivar comentarios inapropiados.",
                        verbose_name="Aprobado",
                    ),
                ),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
                (
                    "autor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comentarios_noticia",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "noticia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comentarios",
                        to="content.noticia",
                    ),
                ),
            ],
            options={
                "verbose_name": "Comentario de Noticia",
                "verbose_name_plural": "Comentarios de Noticias",
                "ordering": ["fecha_creacion"],
            },
        ),
    ]
