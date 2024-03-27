import logging

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.users.forms import CreationForm, FormUsersEdit

# настраиваем логирование в приложении Users
users_logger = logging.getLogger("Users")
users_logger.setLevel(logging.INFO)
fh = logging.FileHandler(filename="users.log", mode="w+")
formatter = logging.Formatter('%(asctime)s - %(name)s'
                              ' - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
users_logger.addHandler(fh)

User = get_user_model()


class SignUp(CreateView):
    template_name = 'users/reg.html'
    form_class = CreationForm
    success_url = reverse_lazy(
        "login")

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        self.object.open_pass = form.cleaned_data.get('password1')
        self.object.save()
        # confirmation_code = PasswordResetTokenGenerator()
        try:
            send_mail(
                f'Вы зарегистрировались на сайте {settings.SITE_NAME}',
                'Поздравляем, Вам открыты ресурсы для зарегистрированных'
                ' пользователей. ',
                settings.EMAIL_HOST_USER,
                [self.object.email],
                fail_silently=False,
            )
        except Exception as e:
            users_logger.error('Регистрация пользователя username: '
                               f'{self.object.username}.'
                               'Ошибка отправки письма на адрес: '
                               f'{self.object.email} {e.args[-1]}')
        return super().form_valid(form)


@login_required
def users_admin(request):
    count = User.objects.all()
    return render(request, 'users/users_admin.html',
                  {'count': count}
                  )


@login_required
def users_admin_edit(request, user_id):
    if not request.user.is_staff:
        return redirect('index')
    user = get_object_or_404(User, pk=user_id)
    form = FormUsersEdit(request.POST or None, instance=user)
    if not form.is_valid():
        return render(request, 'users/users_admin_edit.html',
                      {'user': user, 'form': form}
                      )
    user = form.save()

    return redirect('users:users_admin')


@login_required
def users_admin_delete(request, user_id):
    if not request.user.is_admin:
        return redirect('recipes:index')
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return redirect('users:users_admin')


def page_not_found(request, exception):
    context = {"path": request.path,
               "title": "Ошибка 404",
               "text": "Такой страницы не существует"}
    return render(request, "misc/404.html",
                  context, status=404)


def server_error(request):
    context = {"title": "Ошибка 500",
               "text": ("Вы зашли на секретную страницу сайта, "
                        "на нее попадают менее 0.01% пользователей. "
                        "Мы подумаем, что с этим сделать ;)")}
    return render(request, "misc/500.html", context, status=500)
