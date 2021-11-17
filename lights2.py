#!/usr/bin/python3

from gi.repository import Gtk
import sys


class MyWindow(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Scale Example", application=app)
        self.set_default_size(400, 300)
        self.set_border_width(5)

        # two adjustments (initial value, min value, max value,
        # step increment - press cursor keys to see!,
        # page increment - click around the handle to see!,
        # page size - not used here)
        ad1 = Gtk.Adjustment(0, 0, 100, 5, 10, 0)
#        ad2 = Gtk.Adjustment(50, 0, 100, 5, 10, 0)

        # an horizontal scale
        self.h_scale = Gtk.Scale(
            orientation=Gtk.Orientation.HORIZONTAL, adjustment=ad1)
        # of integers (no digits)
        self.h_scale.set_digits(0)
        # that can expand horizontally if there is space in the grid (see
        # below)
        self.h_scale.set_hexpand(True)
        # that is aligned at the top of the space allowed in the grid (see
        # below)
        self.h_scale.set_valign(Gtk.Align.START)

        # we connect the signal "value-changed" emitted by the scale with the callback
        # function scale_moved
        self.h_scale.connect("value-changed", self.scale_moved)

#        # a vertical scale
#        self.v_scale = Gtk.Scale(
#            orientation=Gtk.Orientation.VERTICAL, adjustment=ad2)
#        # that can expand vertically if there is space in the grid (see below)
#        self.v_scale.set_vexpand(True)
#
#        # we connect the signal "value-changed" emitted by the scale with the callback
#        # function scale_moved
#        self.v_scale.connect("value-changed", self.scale_moved)

        # a label
        self.label = Gtk.Label()
        self.label.set_text("Move the scale handles...")

        # a grid to attach the widgets
        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_column_homogeneous(True)
        grid.attach(self.h_scale, 0, 0, 1, 1)
#        grid.attach_next_to(
#            self.v_scale, self.h_scale, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach(self.label, 0, 1, 2, 1)

        self.add(grid)

    # any signal from the scales is signaled to the label the text of which is
    # changed
    def scale_moved(self, event):
        self.label.set_text("Horizontal scale is " + str(int(self.h_scale.get_value())) )
        slide = (str(int(self.h_scale.get_value())))
        print(slide)


class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
