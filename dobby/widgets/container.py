from __future__ import print_function, absolute_import, division

from ..utils import Attribute, Constraint
from ..libs import *
from .base import Widget

class NSContainer_impl(object):
    NSContainer = ObjCSubclass('NSView', 'NSContainer')

    @NSContainer.method('B')
    def isFlipped(self):
        return True

    '''Allows key events'''
    @NSContainer.method('B')
    def acceptsFirstResponder(self):
        return True

    @NSContainer.method('v@')
    def mouseDown_(self, event):
        print('mouseDown')

    @NSContainer.method('v@')
    def mouseDragged_(self, event):
        print('mouseDragged')

    @NSContainer.method('v@')
    def mouseUp_(self, event):
        print('mouseUp')

    @NSContainer.method('v@')
    def mouseMoved_(self, event):
        print('mouseMoved')

    @NSContainer.method('v@')
    def mouseEntered_(self, event):
        print('mouseEntered')

    @NSContainer.method('v@')
    def mouseExited_(self, event):
        print('mouseExited')

    @NSContainer.method('v@')
    def rightMouseDragged_(self, event):
        print('rightMouseDragged')

    @NSContainer.method('v@')
    def rightMouseUp_(self, event):
        print('rightMouseUp')

    @NSContainer.method('v@')
    def otherMouseDown_(self, event):
        print('otherMouseDown')

    @NSContainer.method('v@')
    def otherMouseDragged_(self, event):
        print('otherMouseDragged')

    @NSContainer.method('v@')
    def otherMouseUp_(self, event):
        print('otherMouseUp')

    @NSContainer.method('v@')
    def scrollWheel_(self, event):
        print('scrollWheel')

    @NSContainer.method('v@')
    def keyDown_(self, event):
        print('keyDown')

    @NSContainer.method('v@')
    def keyUp_(self, event):
        print('keyUp')

    @NSContainer.method('v@')
    def flagsChanged_(self, event):
        print('flagsChanged')

    @NSContainer.method('v@')
    def tabletPoint_(self, event):
        print('tabletPoint')

    @NSContainer.method('v@')
    def tabletProximity_(self, event):
        print('tabletProximity')


NSContainer = ObjCClass('NSContainer')

class Container(Widget):

    _IDENTIFIER = {
        None: NSLayoutAttributeNotAnAttribute,
        Attribute.LEFT: NSLayoutAttributeLeft,
        Attribute.RIGHT: NSLayoutAttributeRight,
        Attribute.TOP: NSLayoutAttributeTop,
        Attribute.BOTTOM: NSLayoutAttributeBottom,
        Attribute.LEADING: NSLayoutAttributeLeading,
        Attribute.TRAILING: NSLayoutAttributeTrailing,
        Attribute.WIDTH: NSLayoutAttributeWidth,
        Attribute.HEIGHT: NSLayoutAttributeHeight,
        Attribute.CENTER_X: NSLayoutAttributeCenterX,
        Attribute.CENTER_Y: NSLayoutAttributeCenterY,
    }

    _RELATION = {
        Constraint.LTE: NSLayoutRelationLessThanOrEqual,
        Constraint.EQUAL: NSLayoutRelationEqual,
        Constraint.GTE: NSLayoutRelationGreaterThanOrEqual,
    }

    def __init__(self):
        super(Container, self).__init__()
        self.children = []
        self.constraints = {}
        self.startup()

    def startup(self):
        self._impl = NSContainer.alloc().init()
        self._impl.setTranslatesAutoresizingMaskIntoConstraints_(False)

    def add(self, widget):
        self.children.append(widget)
        widget.app = self.app
        self._impl.addSubview_(widget._impl)

    def _set_app(self, app):
        for child in self.children:
            child.app = app

    def _set_window(self, window):
        for child in self.children:
            child.window = window

    def constrain(self, constraint):
        "Add the given constraint to the widget."
        if constraint in self.constraints:
            return

        widget = constraint.attr.widget._impl
        identifier = constraint.attr.identifier

        if constraint.related_attr:
            related_widget = constraint.related_attr.widget._impl
            related_identifier = constraint.related_attr.identifier

            multiplier = constraint.related_attr.multiplier / constraint.attr.multiplier
            constant = (constraint.related_attr.constant - constraint.attr.constant) / constraint.attr.multiplier

        else:
            related_widget = None
            related_identifier = None

            multiplier = constraint.attr.multiplier
            constant = constraint.attr.constant

        constraint._impl = NSLayoutConstraint.constraintWithItem_attribute_relatedBy_toItem_attribute_multiplier_constant_(
            widget, self._IDENTIFIER[identifier],
            self._RELATION[constraint.relation],
            related_widget, self._IDENTIFIER[related_identifier],
            multiplier, constant,
        )

        self._impl.addConstraint_(constraint._impl)
        self.constraints[constraint] = constraint._impl
