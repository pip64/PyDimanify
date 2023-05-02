# PyDimanify
Код - говнянный, знаю. Однако всё создано по рофлу, так что пофиг. Делал я от скуки, точнее не я, а чатгпт, название в честь диманисета.

Начну сразу.
Вывод в консоль:
```вывод("Привет, димани!")```

# Тексты
Класс объявляется так:
```текст("любой текст и т.д.") ```

Список действий с классом:
- ```.вывести()``` выведет содержимое класса
- ```.капс()``` КАПСИТ, ЛОГИЧНО
- ```.низ()``` превращает текст в низкую раскладку
- ```.спросить()``` получает текст введённый пользователем в консоль.
- ```.вернуть()``` ретурнит содержимое класса

# Переменные
Класс объявляется так:
```переменная("str/int/list/bool", содержимое)```

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

# Циклы
Пример цикла:

```py
#переменная, в которой мы будем считать количество повторений
перем = переменная("int", 1)

#через lambda напишем условия, при которых будет работать цикл
циклик = цикл(lambda: перем.значение() <= 10)
циклик.добавить([
#код тоже в ламбда
  lambda: вывод(перем),
  lambda: перем.присвоить(1)
])
циклик.выполнить()
```

# Рандом
Функции:
```py
рандом.выбор(массив) #рандом элемент из массива
рандом.число(от, до) #рандом число от до(напр от 0 до 100)
```
