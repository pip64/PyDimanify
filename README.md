# PyDimanify
Код - говнянный, знаю. Однако всё создано по рофлу, так что пофиг. Делал я от скуки, точнее не я, а чатгпт, название в честь диманисета.

# Начало
В начале файла название.dim импортируйте язык
```py
использовать 'dimanify'
```

Напишем в файле команду для вывода в консоль:
```py
вывод("Привет, димани!")
```

Для запуска файла напишите в консоли(заранее войдя в папку dimanify)
```py
python3 start.py название.dim
```

И увидим в консоли: ```Привет, димани!```

# Тексты
Класс объявляется так:
```py
текст("любой текст и т.д.")
```

Список действий с классом:
- ```.вывести()``` выведет содержимое класса
- ```.капс()``` КАПСИТ, ЛОГИЧНО
- ```.низ()``` превращает текст в низкую раскладку
- ```.спросить()``` получает текст введённый пользователем в консоль.
- ```.вернуть()``` ретурнит содержимое класса

# Переменные
```py
переменная название = тип, содержимое #первый способ
название = содержимое #второй способ
```

Список действий с классом:
- ```.присвоить(число)``` Прибавляет число и меняет значение
- ```.прибавить(число)``` Не меняет значение, просто прибавляет
- ```.уравнить(новое значение)``` Меняет значение переменной на то, что вы написали
- ```.вывести()``` аналогично с текстами - выводит содержимое переменной
- ```.значение()``` ретурнит содержимое переменной

# Функции
Создание функции без аргументов:

```py
функция = функ("название функции")
функция.добавить([
  'вывод("Функция вызвана!")' 
])
функция.выполнить()
```

С аргументами:

```py
функция = функ("название функции", "аргумент1", ...)
функция.добавить([
  'вывод("Значение аргумента: ;аргумент1")',
  'вывод("Экранизация: \;аргумент1")'
])
функция.выполнить("значение аргумента1", ...)
```

Получить имя функции - ```.название()```

# Условия
Благодаря условиям вы впринципе можете сделать проверку чего нибудь, например, если 5 < 10

```py
#в лямбде пишем само условие
условие1 = условие(лямбд: 5 < 10)
#код если это верно
условие1.если([
  лямбд: вывод("всё ок бро, 5 меньше 10")
])
#иначе
условие1.иначе([
  лямбд: вывод("чооо 5 не меньше 10???"),
])
#и выполним условие
условие1.выполнить()
```

# Циклы
Пример цикла **когда**:

```py
#переменная, в которой мы будем считать количество повторений
перем = переменная("int", 1)

#через лямбд напишем условия, при которых будет работать цикл
циклик = когда(лямбд: перем.значение() <= 10)
циклик.добавить([
#код тоже в ламбда
  лямбд: вывод(перем),
  лямбд: перем.присвоить(1)
])
циклик.выполнить()
```

Пример цикла **для**:

```py
#второй аргумент - название аргумента для цикла
фор = для(диапазон(11), "pon")
фор.добавить([
#.вернуть_название_аргумента() всё понятно
#.вернуть_аргумент() возращает значение вашего аргумента, указанного в первой строке цикла
  лямбд: вывод(f"{фор.вернуть_название_аргумента()}: {фор.вернуть_аргумент()}")
])
фор.выполнить()
```

# Исключения
Благодаря исключениям мы можем убрать плохие некрасивые ошибки в консоли и тд!!!

Для начала напишем сам кодик и поместим его в класс "попытка"
```py
пон = попытка([
  лямбд: вывод("прив"),
  лямбд: в
])
```

Далее напишем код того, что будет, если в какой то из строк кода нашей попытки будет ошибка
```py
пон.добавить_кроме([
  лямбд: вывод("ошибка")
])
```

И, если попытка и кроме выполнились, можно добавить окончательное действие, но не обязательно
```py
пон.добавить_окончательно([
  лямбд: вывод("я все сделал можно домой")
])
```

А далее выполним код
```py
пон.выполнить()
```

# Файлы
Работа с файлами теперь возможна на... кириллице!

Открыть файл: 
```py
файл("путь", "тип") # типы такие же как в open
```

Дальнейшие действия:
- ```.читать(сколько символов/пусто)``` читать файл
- ```.читать_строки()``` читать построчно
- ```.записать("содержимое")``` записать в конец файла чо нибудь
- ```.записать_строку(список)``` записать список в файл

# Рандом
Функции:
```py
рандом.выбор(массив) #рандом элемент из массива
рандом.число(от, до) #рандом число от до(напр от 0 до 100)
```

# Запросы

Создаем объект запрос с адресом URL

```py
мой_запрос = запрос("https://jsonplaceholder.typicode.com/posts")
```

GET запрос

```py
ответ = мой_запрос.получить()
вывод(ответ.json())
```

POST запрос

```py
данные = {'title': 'foo', 'body': 'bar', 'userId': 1}
ответ = мой_запрос.пост(жсон=данные)
вывод(ответ.json())
```

PUT запрос

```py
данные = {'title': 'foo', 'body': 'bar', 'userId': 1}
ответ = мой_запрос.положить(данные=данные)
вывод(ответ.json())
```

DELETE запрос

```py
ответ = мой_запрос.удалить()
вывод(ответ.status_code)
```

# Цепи маркова

Це́пь Ма́ркова — последовательность случайных событий с конечным или счётным числом исходов, где вероятность наступления каждого события зависит от состояния, достигнутого в предыдущем событии. Характеризуется тем свойством, что, говоря нестрого, при фиксированном настоящем будущее независимо от прошлого.(Ааа викепедия)

Пример кода на диманифи, в котором мы сгенерируем чо то с помощью цепи маркова
```py
использовать 'dimanify'

файлик = файл("dataset.txt", "r").читать()

# создадим модель, первый аргумент - текст, на основе которого мы будем генерировать текст
# как первый аргумент я сделал содержимое файла dataset.txt
# размер состояния - размер состояния в цепи маркова пон
цепь = марков(файлик, размер_состояния=2)

#генерируем
#аргумент "слов" - количество слов, которые мы сгенерируем
результат = цепь.создать(слов = 5)

#выведем результат
вывод(результат)
```

# Disetify
Disetify - это мини библиотека для создания бота на PyDimanify пон
Чтобы подключить, зайдите в файл dimanify.py и добавьте строку 
```py
использовать 'dimanify'
```

Для начала создадим переменную бота с классом Бот со всеми интентами лол
```py
интенты = disnake.Intents.all()

бот = Бот(
  префикс = "ваш префикс",
  токен = "ваш токен",
  интенты = интенты
)
```

Создадим парочку команд
```py
бот.команда(
  название="кинь кота",
  ответ="https://tenor.com/view/byuntear-sad-sad-cat-cat-meme-gif-25617057",
  пинг=True #ответит ли бот или тупо отправит сообщение
)

бот.команда(
  название="кинь собаку",
  ответ="https://tenor.com/view/dog-meme-gif-25326537",
  пинг=False
)
```

И запустим
```py
бот.запустить()
```

Вуаля!

<img width="948" alt="Без названия 6" src="https://user-images.githubusercontent.com/76626915/235769484-d2e2ef40-4c0a-4117-b342-a84bde447fd7.png">

# И наконец...
Димани, выходи за меня замуж!
Всё это создано для тебя! Я так старался!
