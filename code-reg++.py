# База пользователей
users = {
 'idishki':{1000:1000},
 'Nikola':{'name':'Nikola','password':'1234','email':'a@a.a','id':1000,'status':'free'}
         }
log = ['username', 'id', 'activity']

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
   password = input('Придумайте пароль: ')
   if username in users:
    print("Пользователь с таким именем уже существует!") 
    continue
   print("Подтвердите корректность данных: ")
   print("Имя:", username + '; ', "Пароль:", password)
   correct = input("Введите «1», если всё верно, или «2», если хотите изменить: ") 
   if correct == "1":
    print('Аккаунт зарегистрирован')
    id1 = list(users['idishki'])[-1]+1 # вычисление айди
    users[username] = {'name':username,'password':password,'email':'None','id':id1,'ststus':'free'} # запись нового пользователя
    users['idishki'][id1] = id1 # запись айди
    log[0],log[1],log[2] = username, id1, 'active' # запись лога
    return username
   elif correct == "2":
    print("Заполните данные с начала")
    continue
   else:
    print("Введите «1», если всё верно, или «2», если хотите изменить.")

def login(): # вход в аккаунт
 while True:
  print(" - - Войдите в аккаунт - - ")
  print('[1] - Назад')
  username1 = input("Введите имя: ")
  if username1 == '1': return username1
  elif username1 not in users:
   print('Пользователя с таким именем не существет!')
   continue
  password1 = input("Введите пароль: ")
  if username1 in users and password1 == users[username1]['password']:
     print("Вход в аккаунт совершён успешно")
     log[0],log[1],log[2] = username1, users[username1]['id'], 'active'
     return username1
  else:
   print("Неверный логин или пароль. повторите попытку") 
   continue

def add_email(): # предложение привязки почты к аккаунту
 while True:
  print("Рекомендуем привязать электронную почту")
  print("С ней у вас будет возможность в случае утери пароля восстановить доступ к аккаунту")
  print(" [«1»] - привязать почту")
  print(" [«2»] - отказаться")
  a = input('>> ')
  if a == "1":
   email = input("Введите адрес электронной почты: ")
   if "@" not in email and "." not in email:
    print("Введите корректный email!")
    add_email
   elif '@' and '.' in email:
    print("Электронная почта успешно привязана!")
    users[log[0]]['email'] = email
    break
  elif a == "2":
   print("Ладно.")  
   break

def menu2(): # финальное меню
 while True:
  print('[1] - Всё')
  print('[2] - Выйти')
  deystvie = input('>> ')
  return deystvie
 
  
# объеденяющий блок
def united ():
 while True:
  a = menu()
  if a == '1':
   username1 = login() 
   if username1 == '1': continue
   if users[username1]['email'] == 'None': add_email()
   if log[2] == 'active': 
    a = menu2()
    if a == '1': exit()
    elif a == '2': 
     log[2] = ('inactive')
     continue
   else: continue
  elif a == '2': 
   username1 = registration()
   if users[username1]['email'] == 'None': add_email()
   if log[2] == 'active': 
    a = menu2()
    if a == '1': exit()
    elif a == '2': 
     log[2] = ('inactive')
     continue
  else: continue

# общий алгоритм процессов
united()

print('system : ', log)
print('system : ', users)
print('system : ', "Всё")
