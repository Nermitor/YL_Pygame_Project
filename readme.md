#2D Parkourist
Сделано Матюхиным Дмитрием

##Суть проекта
Проект представляет собой игру - платформер. Целью игрока является прохождение уровней.

После прохождения каждого уровня ему становится доступен следующий. 

Игрок может идти, бегать, прыгать, совершать двойной прыжок, скользить по стенам, прыгать со стены на стену.

То есть свобода движений и вариаций прохождения уровня ограничивается только ловкостью пальцев пользователя и его фантазией.

##Немного о реализации

###Менеджер сцен
В главном файле самый большой интерес представляет экземпляр класса SceneAggregator - менеджер сцен игры.

Менеджер сцен позволяет очень удобно распределить обязанности между частями программы, не наваливая всё в кучу.

В его основные обязанности входит переключение сцен между собой, а также распределения событий между ними.

###Сцены
В моей игре сценой является определённый набор объектов, схожих по предназначению или смыслу, находящихся одновременно на экране.

Например, отдельными сценами являются главное меню (scenes/menu.py), само игровое поле (scenes/game_scene.py).

Все сцены наследуются от метакласса сцены MetaScene (scenes/metascene.py). И поэтому должны и реализуют определённые методы.

Из них:

update - обновление сцены

handle_event - обработчик событий

draw - отрисовка сцены на экран

В большинстве сцен используются виджеты

###Виджеты
- статичные объекты, которые являются либо показателем чего-либо (таймер), либо служат для выполнения каких-либо действий (кнопки)

Основным классом виджетов является OnlyImageButton. Как понятно из названия это кнопка с изображением.

Обязательным её атрибутом должна быть функция обратного вызова (callback function).

Эта функция вызывается тогда, когда пользователь нажимает на кнопку. В моём случае, я передаю кнопке функцию, создающую событие, которое потом можно отследить.

###Используемые библиотеки
- pygame - основная библиотека для создания игр на pygame
- pytmx - библиотека, позволяющая считывать данные из карты, которая была сделана в графическом редакторе
