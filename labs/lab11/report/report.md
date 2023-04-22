---
## Front matter
title: "Отчёта по лабораторной работе №11"
subtitle: "Дисциплина: Операционные системы"
author: "Рыжкова Ульяна Валерьевна"

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

Изучить основы программирования в оболочке ОС UNIX. Научится писать более сложные командные файлы с использованием логических управляющих конструкций и циклов.

# Выполнение лабораторной работы

1. Первое задание: написать программу, которая анализирует командную строку и ищет нужные строки

![Командный файл 1](image/1.png){#fig:001 width=100%}

![Результат работы](image/2.png){#fig:002 width=100%}

2. Второе задание: написать две программы. Одна анализирует число, а вторая по результататм работы первой выводит сообщение о введенном числе

![Командный файл 2](image/3.png){#fig:003 width=100%}

![Вспомогательная программа на C](image/4.png){#fig:004 width=100%}

![Результат работы](image/5.png){#fig:005 width=100%}

3. Третье задание: написать программу, которая создаёт и удаляет (при их существовании) указанное число файлов

![Командный файл 3](image/6.png){#fig:006 width=100%}

![Результат работы](image/7.png){#fig:007 width=100%}

4. Четвертое задание: написать программу, которая запаковывает в tar архив только те файлы, которые были изменены в течение последней недели

![Командный файл 4](image/8.png){#fig:008 width=100%}

![Результат работы](image/9.png){#fig:009 width=100%}

# Выводы

Я продолжаю познавать основы программирования в оболочке ОС UNIX
