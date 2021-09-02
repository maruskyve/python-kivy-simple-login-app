from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

Builder.load_file('login_app.kv')

users = {1: ['user1', 'user1pw'],
         2: ['user2', 'user2pw'],
         3: ['user3', 'user3pw'],
         4: ['user4', 'user4pw']}


class LoginPage(Screen):
    def processLogin(self):
        usernameRoot, passwordRoot = self.ids.username, self.ids.password
        username, password = usernameRoot.text, passwordRoot.text
        userStat, passwordStat = bool(), bool()
        for userId in users:
            loginStatus = self.ids.login_status

            def matching():
                nonlocal userStat, passwordStat
                userData = users[userId]
                userUsername, userPassword = userData[0], userData[1]
                userStat = True if userUsername == username else False
                passwordStat = True if userPassword == password else False
            matching()
            if userStat and passwordStat:
                print('Username and Password match:\n'
                      f'Username = {username}\n'
                      f'Password = {password}\n'
                      f'UserId = {userId}')
                loginStatus.text = 'Data matched\nLogin Success'
                break
            else:
                print('Sorry, Username and Password not match')
                loginStatus.text = 'Data not matched\nLogin Failed'


class MainApp(MDApp):
    def build(self):
        return LoginPage()


MainApp().run()
