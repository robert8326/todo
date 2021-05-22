from django.db import models
from django.utils.translation import gettext_lazy as _

# - дата и время создания
# - дата и время к которому должна быть выполнена
# - приоритет (высокий, средний, низкий)
# - статус(ожидает выполнения, выполнена, в процессе выполнения)
# - название задачи
# - описание задачи


priority_choice = [
    ('red', 'red'),
    ('orange', 'orange'),
    ('green', 'green'),
]

status = [
    ('ожидает выполнения', 'ожидает выполнения'),
    ('выполнена', 'выполнена'),
    ('в процессе выполнения', 'в процессе выполнения'),
]


class TodoList(models.Model):
    """Todo list model that keeps all todos"""
    name = models.CharField(_('Название задачи'), max_length=255)
    description = models.TextField(_('Описание задачи'))
    priority = models.CharField(
        _('Приоритет'),
        max_length=30,
        choices=priority_choice,
        default='yellow'
    )
    status = models.CharField(
        _('Статус'),
        max_length=30,
        choices=status,
        default='ожидает выполнения'
    )
    start = models.DateTimeField(_('Дата и время создания'))
    finish = models.DateTimeField(_('дата и время к которому должна быть выполнена'))
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Todo list'
        verbose_name_plural = 'Todo lists'
        ordering = ['-created_at']
