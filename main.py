from uiautomator import Device
import time
import subprocess


class InstaShare(object):
    def __init__(self, tags):
        self.tags = tags
        self.d = Device('ZY223DGTCG', adb_server_host='127.0.0.1', adb_server_port='5037')
        self.package = "com.instagram.android"
        self.main_activity = "com.instagram.android.activity.MainTabActivity"

    def check_screen(self):
        if self.d.screen == "on":  # or d.screen != "on"
            # do something in case of screen off
            return True
        elif self.d.screen == 'off':
            return False
        else:
            print("Can't get screen status")

    def launcher(self):

        if not self.d(packageName=self.package).exists:
            print("Launching Instagram.")
            subprocess.Popen("adb shell am start -n " + self.package + "/" + self.main_activity, shell=True)
        else:
            print("App already opened.")

    def wait_for_element(self, element):
        rep = 5
        while not element.exists:
            if rep:
                print("Waiting for element")
                rep -= 1
                time.sleep(2)
            else:
                print("Element could not be found!")
                return False
        else:
            return True

    def search_tab(self):

        search_btn = self.d(className="com.instagram.base.activity.tabactivity.IgTabWidget").child(
                    description="Search and Explore")

        if self.wait_for_element(self.d(packageName=self.package)):
            search_btn.click()
        else:
            print("Can't see search icon.")


tag_names = ['desiviners', 'indianviners']

instagram = InstaShare(tag_names)

if instagram.check_screen():
    instagram.launcher()

    instagram.search_tab()
