from ..utils import Attribute, Constraint
from .widget import *

class ContainerDelegate_(object):
    ContainerDelegate = ObjCSubclass('NSView', 'NSContainer')

    @ContainerDelegate.method('B')
    def isFlipped(self):
        return True

    '''Allows key events'''
    @ContainerDelegate.method('B')
    def acceptsFirstResponder(self):
        return True

    @ContainerDelegate.method('v@')
    def mouseDown_(self, event):
        if self.interface.mouseDown:
            Widget.callback(self.interface.mouseDown(event))

    @ContainerDelegate.method('v@')
    def mouseDragged_(self, event):
        if self.interface.mouseDragged:
            Widget.callback(self.interface.mouseDragged(event))

    @ContainerDelegate.method('v@')
    def mouseUp_(self, event):
        if self.interface.mouseUp:
            Widget.callback(self.interface.mouseUp(event))

    @ContainerDelegate.method('v@')
    def mouseMoved_(self, event):
        if self.interface.mouseMoved:
            Widget.callback(self.interface.mouseMoved(event))

    @ContainerDelegate.method('v@')
    def mouseEntered_(self, event):
        if self.interface.mouseEnter:
            Widget.callback(self.interface.mouseEnter(event))

    @ContainerDelegate.method('v@')
    def mouseExited_(self, event):
        if self.interface.mouseExit:
            Widget.callback(self.interface.mouseExit(event))

    @ContainerDelegate.method('v@')
    def rightMouseDragged_(self, event):
        if self.interface.rightMouseDragged:
            Widget.callback(self.interface.rightMouseDragged(event))

    @ContainerDelegate.method('v@')
    def rightMouseUp_(self, event):
        if self.interface.rightMouseUp:
            Widget.callback(self.interface.rightMouseUp(event))

    @ContainerDelegate.method('v@')
    def scrollWheel_(self, event):
        if self.interface.scroll:
            Widget.callback(self.interface.scroll(event))

    @ContainerDelegate.method('v@')
    def keyDown_(self, event):
        if self.interface.keyDown:
            Widget.callback(self.interface.keyDown(event))

    @ContainerDelegate.method('v@')
    def keyUp_(self, event):
        if self.interface.keyUp:
            Widget.callback(self.interface.keyUp(event))

    @ContainerDelegate.method('v@')
    def flagsChanged_(self, event):
        if self.interface.flagsChanged:
            Widget.callback(self.interface.flagsChanged(event))

ContainerDelegate = ObjCClass('NSContainer')

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

    def __init__(self,
        mouseDown=None,
        mouseDragged=None,
        mouseUp=None,
        mouseMoved=None,
        mouseEnter=None,
        mouseExit=None,
        rightMouseDragged=None,
        rightMouseUp=None,
        scroll=None,
        keyDown=None,
        keyUp=None,
        flagsChanged=None
    ):

        super(Container, self).__init__()

        self.children = []
        self.constraints = {}

        self.mouseDown = mouseDown
        self.mouseDragged = mouseDragged
        self.mouseUp = mouseUp
        self.mouseMoved = mouseMoved
        self.mouseEnter = mouseEnter
        self.mouseExit = mouseExit
        self.rightMouseDragged = rightMouseDragged
        self.rightMouseUp = rightMouseUp
        self.scroll = scroll
        self.keyDown = keyDown
        self.keyUp = keyUp
        self.flagsChanged = flagsChanged

        self.startup()

    def startup(self):
        self._impl = ContainerDelegate.alloc().init()
        self._impl.setTranslatesAutoresizingMaskIntoConstraints_(False)
        self._impl.interface = self

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

    def get_view(self):
        return self._impl

    def constrain(self, constraint):
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