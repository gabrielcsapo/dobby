from .widget import *

class TableDelegate_(object):
    TableDelegate = ObjCSubclass('NSTableView', 'TableDelegate')

    @TableDelegate.method('i@')
    def numberOfRowsInTableView_(self, table):
        return len(self.interface._data)

    @TableDelegate.method('@@@i')
    def tableView_objectValueForTableColumn_row_(self, table, column, row):
        column_index = int(cfstring_to_string(column.identifier))
        return get_NSString(self.interface._data[row][column_index])    

    @TableDelegate.method('@@@@i')
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
        self.interface._table.reload_data()

    @TableDelegate.method('v@')
    def tableViewSelectionIsChanging_(self, notification):
        print('selection changed')

    @TableDelegate.method('v@')
    def tableViewSelectionDidChange_(self, notification):
        if self.interface.on_selection_change:
            Widget.callback(self.interface.on_selection_change(notification))

    @TableDelegate.method('v@')
    def tableViewColumnDidMove_(self, notification):
        if self.interface.on_column_move:
            Widget.callback(self.interface.on_column_move(notification))

    @TableDelegate.method('v@')
    def tableViewColumnDidResize_(self, notification):
        if self.interface.on_column_resize:
            Widget.callback(self.interface.on_column_resize(notification))

TableDelegate = ObjCClass('TableDelegate')

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
        self._impl = NSScrollView.alloc().init()
        self._impl.setHasVerticalScroller_(True)
        self._impl.setHasHorizontalScroller_(True)
        self._impl.setAutohidesScrollers_(False)
        self._impl.setBorderType_(NSBezelBorder)
        self._impl.setTranslatesAutoresizingMaskIntoConstraints_(False)

        self._table = TableDelegate.alloc().init()
        self._table.interface = self
        self._table.setColumnAutoresizingStyle_(NSTableViewUniformColumnAutoresizingStyle)

        self._columns = []
        for i, heading in enumerate(self.headings):
            print(i)
            column = NSTableColumn.alloc().initWithIdentifier_(get_NSString('%d' % i))
            column.valueForKey_(get_NSString('headerCell')).setStringValue_(get_NSString(heading))
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

        self.reload_data()

    def reload_data(self):
        self._table.reloadData()

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data
        self.reload_data()