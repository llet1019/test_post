from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    board_name = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        verbose_name='게시판명'
    )
    is_display = models.BooleanField(
        null=False,
        blank=False,
        default=True,
        verbose_name='공개여부'
    )
    priority = models.IntegerField(
        null=False,
        blank=False,
        default=0,
        verbose_name='우선순위'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='생성일'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='수정일'
    )

    def __str__(self):
        return f'{self.board_name}'

    class Meta:
        verbose_name = '게시판'
        verbose_name_plural = '게시판'
        ordering = ['priority']


class Post(models.Model):
    board = models.ForeignKey(
        Board,
        on_delete=models.CASCADE,
        verbose_name='게시판'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='작성자'
    )
    title = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        verbose_name='제목'
    )
    context = models.TextField(
        null=False,
        blank=False,
        verbose_name='본문내용'
    )
    view_count = models.PositiveIntegerField(
        null=False,
        blank=False,
        default=0,
        verbose_name='조회수'
    )
    is_display = models.BooleanField(
        null=False,
        blank=False,
        default=True,
        verbose_name='공개여부'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='생성일'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='수정일'
    )

    def __str__(self):
        return f'{self.board} - {self.title}'

    class Meta:
        verbose_name = '게시글'
        verbose_name_plural = '게시글'
        ordering = ['-created_at']

