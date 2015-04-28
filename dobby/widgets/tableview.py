from __future__ import print_function, absolute_import, division

from ..libs import *
from .base import Widget
from ..utils import process_callback

class TableImpl_impl(object):
    TableImpl = ObjCSubclass('NSTableView', 'TableImpl')

    @TableImpl.method('i@')
    def numberOfRowsInTableView_(self, table):
        return len(self.interface._data)

    @TableImpl.method('@@@i')
    def tableView_objectValueForTableColumn_row_(self, table, column, row):
        column_index = int(cfstring_to_string(column.identifier))
        return get_NSString(self.interface._data[row][column_index])    

    @TableImpl.method('@@@@i')
    def tableView_setObjectValue_forTableColumn_row_(self, table, newValue, column, row): 
        column_index = int(cfstring_to_string(column.identifier))
        oldValue = cfstring_to_string(self.tableView_objectValueForTableColumn_row_(table, column, row))
        newValue = cfstring_to_string(newValue)
        newRow = []
        for i, value in enumerate(self.interface._data[row]):
            if(i == column_index):
                newRow.append(newValue)
            else:
                newRow.append(value)

        self.interface._data[row] = newRow
        self.interface._table.reloadData()

    @TableImpl.method('v@')
    def tableViewSelectionIsChanging_(self, notification):
        print('selection changed')

    @TableImpl.method('v@')
    def tableViewSelectionDidChange_(self, notification):
        if self.interface.on_selection_change:
            process_callback(self.interface.on_selection_change(notification))

    @TableImpl.method('v@')
    def tableViewColumnDidMove_(self, notification):
        if self.interface.on_column_move:
            process_callback(self.interface.on_column_move(notification))

    @TableImpl.method('v@')
    def tableViewColumnDidResize_(self, notification):
        if self.interface.on_column_resize:
            process_callback(self.interface.on_column_resize(notification))

TableImpl = ObjCClass('TableImpl')

class TableView(Widget):
    def __init__(self, headings, on_selection_change=None, on_column_move=None, on_column_resize=None):
        super(TableView, self).__init__()
        
        self.headings = headings
        self._data = []

        self.on_selection_change = on_selection_change
        self.on_column_move = on_column_move
        self.on_column_resize = on_column_resize

        self.startup()

    def startup(self):
        # Create a table view, and put it in a scroll view.
        # The scroll view is the _impl, because it's the outer container.
        self._impl = NSScrollView.alloc().init()
        self._impl.setHasVerticalScroller_(True)
        self._impl.setHasHorizontalScroller_(True)
        self._impl.setAutohidesScrollers_(False)
        self._impl.setBorderType_(NSBezelBorder)
        self._impl.setTranslatesAutoresizingMaskIntoConstraints_(False)

        self._table = TableImpl.alloc().init()
        self._table.interface = self
        self._table.setColumnAutoresizingStyle_(NSTableViewUniformColumnAutoresizingStyle)

        # Create columns for the table
        self._columns = []
        for i, heading in enumerate(self.headings):
            print(i)
            column = NSTableColumn.alloc().initWithIdentifier_(get_NSString('%d' % i))
            column.valueForKey_(get_NSString('headerCell')).setStringValue_(get_NSString(heading))
            # column.headerCell.setStringValue(get_NSString(heading))
            self._columns.append(column)
            self._table.addTableColumn_(column)

        self._table.setDelegate_(self._table)
        self._table.setDataSource_(self._table)
        self._impl.setDocumentView_(self._table)

    def insert(self, index, *data):
        if len(data) != len(self.headings):
            raise Exception('Data size does not match number of headings')

        if index is None:
            self._data.append(data)
        else:
            self._data.insert(index, data)

        self.reloadData()

    def reloadData(self):
        self._table.reloadData()

    def getData(self):
        return self._data

    def setData(self, data):
        self._data = data
        self.reloadData()