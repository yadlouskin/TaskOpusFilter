# Tестовое задание для вакансии Junior Python Developer


Установите эту библиотеку для фильтрации датасетов.

https://github.com/Helsinki-NLP/OpusFilter

 
И отфильтруйте этот датасет, как можно лучше используя фильтры Opus.  Датасет состоит из 2 текстовых файлов и содержит в себе перевод предложений с английского языка на русский.


Ссылка на скачивание датасета:

https://drive.google.com/file/d/1vj5QS6LW9NVhbK0V5WRi_HpdpRF8geg9/view?usp=sharing

 
Ваша задача - удалить строки, где неправильный перевод с английского на русский, те, где есть ошибки (грамматические, лексические итд). После чего прислать датасет только с хорошим переводом.


Пример строки потенциально правильного перевода (кол-во предложений слева и справа совпадает, а также приблизительное соотношение количества слов)


I went for a walk - я пошел гулять


Один из примеров неправильного перевода (слева одно предложение,  справа два)


How are you?  - Привет! Как твои дела?


Еще один пример неправильного перевода (четыре слова английского языка практически никогда не переводятся в 20 слов русского. Это косвенный признак того, что перевод неправильный)


Do you like pizza?  - Пицца это традиционное итальянское блюдо, изначально в виде круглой дрожжевой лепёшки, выпекаемой с уложенной сверху начинкой из томатного соуса


Все плохие строки удалить очень сложно, отфильтруйте сколько сможете, используя любые фильтры Opus. Можете написать свой кастомный фильтр через Regex. Покажите все что умеете.

 
Описание фильтров можно почитать здесь

https://helsinki-nlp.github.io/OpusFilter/filters/length_filters.html