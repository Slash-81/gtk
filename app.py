from UI import login
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


if __name__ == "__main__":
    win = login.LoginWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
