
# База пользователей
users = {
 'idishki':{1000:1000},
 'Nikola':{'Name':'Nikola','password' : '1234', 'email' : 'a@a.a'}
         }
status  = ['inactive']

def menu(): # меню
  print(" - - Меню - - ")
  print("[1] - Войти")
  print("[2] - Зарегистрироваться")
  deystvie = input('>> ')
  return deystvie

def registration(): # создание учётной записи 
 while True:
   print("Создайте учётную запись")
   username = input('Введите ваше имя: ')
   if username in users:
    print("Пользователь с таким именем уже существует!") 
    continue
   password = input('Придумайте пароль: ')
   print("Подтвердите корректность данных: ")
   print("Имя:", username + '; ', "Пароль:", password)
   correct = input("Введите «1», если всё верно, или «2», если хотите изменить: ") 
   if correct == "1":
    print('Аккаунт зарегистрирован')
    users[username] = {'name' : username, 'password' : password, 'email' : 'None'}
    status[0] = 'active'
    return username
   elif correct == "2":
    print("Заполните данные с начала")
    continue
   else:
    print("Введите «1», если всё верно, или «2», если хотите изменить.")

def login(): # авторизация 
 while True:
  print(" - - Войдите в аккаунт - - ")
  print('[1] - Назад')
  username1 = input("Введите имя: ")
  if username1 not in users:
   print('Пользователя с таким именем не существет!')
   continue
  password1 = input("Введите пароль: ")
  if username1 in users and password1 == users[username1]['password']:
     print("Вход в аккаунт совершён успешно")
     status[0] = 'active'
     return username1
  elif username1 == '1': continue
  else:
   print("Неверный логин или пароль. повторите попытку") 
   continue


def add_email(): # предложение привязки почты к аккаунту
 while True:
  username1 = login()[0] 
  print("Рекомендуем привязать электронную почту")
  print("С ней у вас будет возможность в случае утери пароля восстановить доступ к аккаунту")
  print(" [«1»] - привязать почту")
  print(" [«2»] - отказаться")
  a = input('>> ')
  if a == "1":
   email = input("Введите адрес электронной почты: ")
   if "@" not in email and "." not in email:
    print("Введите корректный email!")
    continue
   elif '@' and '.' in email:
    print("Электронная почта успешно привязана!")
    users[username1]['email'] = email
    break
  elif a == "2":
   print("Ненененененееее.. Это была иллюзия выбора. вы привяжете почту. иначе пожалеете...")  
   continue
  
def menu2():
 while True:
  print('[1] - Всё')
  print('[2] - Выйти')
  deystvie1 = input('>> ')
  if deystvie1 == '1': break
  elif deystvie1 == '2': 
   status[0] = ('inactive')
   united()
  
# объеденяющий блок
def united ():
 a = menu()
 if a == '1':
  username1 = login()
  if users[username1]['email'] == 'None': add_email()
 elif a == '2': 
  username1 = registration()
  if users[username1]['email'] == 'None': add_email()
 else: menu()

# общий алгоритм процессов
united()
menu2()




print(status)
print(users)
print("Всё")
