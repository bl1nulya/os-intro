---
## Front matter
title: "Шаблон отчёта по лабораторной работе №3"
subtitle: "Простейший вариант"
author: "Дмитрий Сергеевич Кулябов"

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Цель данной работы: познакомиться с основными возможностями разметки Markdown.

# Выполнение лабораторной работы

1. Заданием является составить отчёт предыдущей лабораторной работы. Увы, я делала её с опозданием и совершенно забыла о скриншотах (надеюсь, скринкаст с комментариями решит этот недочёт)

2. Поскольку я уже являюсь пользователем github и в прошлом семестре настроила систему git, перехожу к шагу создания pgp ключа. 

![Подключенный pgp ключ](image/1.png){#fig:001 width=100%}

3. Настроила подпись коммитов.

4. С помощью шаблона создаю репозиторий для проходимого в этом семестре курса.

![Новый репозиторий](image/2.png){#fig:002 width=100%}

5. Удаляю лишние файлы и создаю необходимые каталоги с помощью команды make. Отправляю файлы на сервер.

![Создание каталогов и загрузка файлов на сервер](image/3.png){#fig:003 width=100%}

# Выводы

Я ознакомилась с языком разметки Markdown
