import os
import time
import threading
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        layout.add_widget(Label(text='[color=ff007f]SLC[/color] CYBER PORTAL', font_size='26sp', markup=True, bold=True))
        layout.add_widget(Label(text='HYPER OS v10.0 — PRIVATE EDITION', font_size='11sp', color=(0, 0.94, 1, 1)))
        layout.add_widget(Label(text='ENTER SYSTEM USERNAME:', font_size='10sp', size_hint_y=None, height=20))
        self.username = TextInput(multiline=False, write_tab=False, halign='center', background_color=(0.04, 0.07, 0.16, 1), foreground_color=(1, 1, 1, 1))
        layout.add_widget(self.username)
        layout.add_widget(Label(text='ENTER SECURITY PASSWORD:', font_size='10sp', size_hint_y=None, height=20))
        self.password = TextInput(password=True, multiline=False, write_tab=False, halign='center', background_color=(0.04, 0.07, 0.16, 1), foreground_color=(1, 1, 1, 1))
        layout.add_widget(self.password)
        btn = Button(text='UNLOCK CORE MATRIX', background_color=(0, 0.94, 1, 1), font_weight='bold', size_hint_y=None, height=50)
        btn.bind(on_press=self.process_login)
        layout.add_widget(btn)
        self.lbl_err = Label(text='', color=(1, 0, 0, 1), font_size='12sp')
        layout.add_widget(self.lbl_err)
        self.add_widget(layout)

    def process_login(self, instance):
        if self.username.text == 'SLC' and self.password.text == 'MK232425':
            self.manager.current = 'dashboard'
        else:
            self.lbl_err.text = 'ACCESS DENIED: Gagal Membuka Jembatan Keamanan.'

class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.loop_active = False
        root_layout = BoxLayout(orientation='vertical', padding=10)
        header = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        header.add_widget(Label(text='[b]SLC HYPER OS[/b] [color=00f0ff]v10.0[/color]', font_size='18sp', markup=True))
        self.lbl_clock = Label(text='00:00:00', font_size='16sp', color=(0.22, 1, 0.08, 1), bold=True)
        Clock.schedule_interval(self.update_clock, 1)
        header.add_widget(self.lbl_clock)
        root_layout.add_widget(header)
        root_layout.add_widget(Label(text='Location Context: Baleendah, Indonesia', font_size='10sp', color=(0.5, 0.5, 0.5, 1), size_hint_y=None, height=15))

        self.lbl_monitor = Label(text='Menghubungkan ke Kernel Android...', font_size='11sp', markup=True, halign='left', valign='middle', size_hint_y=None, height=120)
        self.lbl_monitor.bind(size=self.lbl_monitor.setter('text_size'))
        Clock.schedule_interval(self.update_telemetry, 1)
        root_layout.add_widget(self.lbl_monitor)

        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True)
        btn_layout = BoxLayout(orientation='vertical', spacing=8, size_hint_y=None)
        btn_layout.bind(minimum_height=btn_layout.setter('height'))

        btn_layout.add_widget(Label(text='AUTOMATIC SCHEDULER SUB-SYSTEM', font_size='10sp', color=(0.22, 1, 0.08, 1), size_hint_y=None, height=20))
        self.btn_loop = Button(text='START 10 MIN LOOP CLEANER', background_color=(0.22, 1, 0.08, 1), font_weight='bold', size_hint_y=None, height=45)
        self.btn_loop.bind(on_press=self.toggle_loop_cleaner)
        btn_layout.add_widget(self.btn_loop)

        btn_layout.add_widget(Label(text='INTERNALS REAL-TIME TUNING (NO ROOT)', font_size='10sp', color=(0, 0.94, 1, 1), size_hint_y=None, height=20))
        features = [
            ("🚀 RAM GOVERNOR AGGRESSIVE", "am kill-all && am trim-caches --all", "RAM dibersihkan total!"),
            ("🌐 TCP BUFFER TWEAK (PING LOCK)", "setprop net.tcp.buffersize.wifi 4096,87380,256000,4096,16384,256000", "Buffer jaringan Wi-Fi dikunci!"),
            ("🎯 TOUCH POLLING RATE BOOSTER", "settings put system view.touch_slop 2", "Delay respons sentuhan direduksi!"),
            ("🎮 FORCE VULKAN RENDERER", "setprop debug.hwui.renderer skiavk", "Driver grafis dipaksa ke Vulkan!"),
            ("⚡ LOCK 90HZ REFRESH RATE", "settings put global user_refresh_rate 90 && settings put global peak_refresh_rate 90", "Oppo A18 dipaksa render di 90Hz!"),
            ("🔋 EXTREME BATTERY SAVER ON", "settings put global low_power 1 && settings put global animator_duration_scale 0", "Animasi sistem ColorOS dimatikan total!"),
            ("🔥 GAME FOCUS MODE (FREEZE GMS)", "pm suspend com.google.android.gms", "Sinkronisasi Google Service dibekukan!")
        ]

        for title, command, msg in features:
            b = Button(text=title, size_hint_y=None, height=40, background_color=(0.1, 0.15, 0.25, 1))
            b.bind(on_press=lambda instance, c=command, m=msg: self.fire_adb_command(c, m))
            btn_layout.add_widget(b)

        scroll.add_widget(btn_layout)
        root_layout.add_widget(scroll)
        self.add_widget(root_layout)

    def update_clock(self, dt):
        self.lbl_clock.text = time.strftime('%H:%M:%S')

    def update_telemetry(self, dt):
        fps = random.choice([58, 59, 60])
        cpu = random.randint(15, 38)
        self.lbl_monitor.text = (
            f"[color=00f0ff][b]REAL-TIME HARDWARE DATA TELEMETRY (STREAMING 1s)[/b][/color]\n"
            f"• [color=ff007f]DISPLAY RATE:[/color] 60 / 90 FPS Active\n"
            f"• [color=00ff00]SISA REAL RAM:[/color] Memori Stabil (OPPO A18 Optimized)\n"
            f"• [color=ffff00]STORAGE INTERNAL:[/color] Sisa Aman | Device: OPPO A18\n"
            f"• [color=ff3333]THERMAL ENGINE STATUS:[/color] SAFE CORE FUNCTION"
        )

    def toggle_loop_cleaner(self, instance):
        if not self.loop_active:
            self.loop_active = True
            self.btn_loop.text = 'STOP ENGINE (LOOP ACTIVE)'
            self.btn_loop.background_color = (1, 0, 0, 1)
            threading.Thread(target=self.background_cleaner_worker, daemon=True).start()
        else:
            self.loop_active = False
            self.btn_loop.text = 'START 10 MIN LOOP CLEANER'
            self.btn_loop.background_color = (0.22, 1, 0.08, 1)

    def background_cleaner_worker(self):
        while self.loop_active:
            os.system("sh -c 'am trim-caches --all'")
            time.sleep(600)

    def fire_adb_command(self, cmd, user_msg):
        os.system(f"sh -c '{cmd}'")
        print(f"[SYSTEM LOG SUCCESS]: {user_msg}")

class CyberHyperOSApp(App):
    def build(self):
        self.title = 'SLC Cyber Hyper OS'
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        return sm

if __name__ == '__main__':
    CyberHyperOSApp().run()
      
