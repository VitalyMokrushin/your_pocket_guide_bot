## Введение
### Телеграм-бот "Your Pocket Guide"

Данный телеграм-бот помогает туристам, решившим посетить Москву, адаптироваться в этом городе быстрее. С его помощью пользователь может получить полезные советы о жизни в городе, освоить фразы на русском языке для туристов и получить голосовые файлы для ознакомления с ними, а также воспользоваться файлом-путеводителем с достопримечательностями Москвы. 
## Команды
* /start - начать использование бота и открыть главное меню.

## Главное меню
После вызова команды /start пользователю высылается приветственное сообщение и главное меню, где он сможет выбрать одну из четырех кнопок ("Advice", "Basic Phrases", "Attractions", "Feedback")
### Кнопка "Advice"
Кнопка "Advice" отвечает за получение пользователем различных советов о жизни в Москве
#### Ввод данных
* Пользователь выбирает одну из 4 категорий советов, либо возврат в главное меню.
#### Получение данных
* Пользователь получает текстовое сообщение, содержащее набор рекомендаций по выбранной им категории

### Кнопка "Basic Phrases"
Данная кнопка отвечает за предоставление пользователю информации о наиболее необходимых для жизни в русскоязычной стране фразах, а также предлагает прослушать их в виде голосового сообщения.
#### Ввод данных
1. Пользователь выбирает одну из пяти категорий фраз, либо возврат в главное меню.
2. В появившейся после выбора категории фраз виртуальной клавиатуре пользователь выбирает номер нужной ему фразы.
#### Вывод данных
* На выходе пользователь получает голосовое сообщение с русскоязычным звучанием выбранной им фразы. 

### Кнопка "Attractions"
Данная кнопка отвечает за предоставление пользователю информации о достопримечательностях в городе Москве
#### Выыод данных
* Пользователь получает файл формата ".docx", в котором представлены фото достопримечательностей, краткое описание каждой из них, а также часы работы, адрес и веб-сайт. После этого пользователь перенаправляется в главное меню.

### Кнопка "Feedback"
Данная кнопка отвечает за обратную связь. Здесь пользователь может оставить отзыв о работе бота, либо предложить, как можно его усовершенствовать
#### Выыод данных
* Бот благодарит пользователя за оставленный отзыв, после чего пользователь перенаправляется в главное меню.

## Получение данных


# Установка и запуск

1. Установите все необходимые зависимости, выполните команду:
         
       pip install pyTelegramBotApi
       pip install python-dotenv
  
2. Создайте бота в Telegram и получите токен доступа.

3. Создайте файл .env в корневой директории проекта и добавьте следующие переменные:

   * BOT_TOKEN=ВАШ ТОКЕН ДОСТУПА К БОТУ

4. Создайте файл "feedback.txt"

5. Запустите программу.

Теперь ваш телеграм-бот работает и готов к использованию.

