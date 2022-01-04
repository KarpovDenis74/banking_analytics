#!/bin/bash
flake8
if [ $? -eq 0 ]
then
  echo "flake8:   - ОК"
else
  echo "Не пройдено тестирование:   - flake8"
  exit 1
fi
python manage.py test
if [ $? -eq 0 ]
then
  echo "python manage.py test:   - ОК"
else
  echo "Не пройдено тестирование:   - python manage.py test"
  exit 1
fi
git status
git add .
read -p 'Введите комментарий для текущего коммита: ' commit_text
git commit -m "$commit_text"
git push git push git@github.com:KarpovDenis74/banking_analytics.git
