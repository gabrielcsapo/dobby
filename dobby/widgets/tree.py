from .widget import *

NSObject = ObjCClass('NSObject')

class TreeNode(object):
    def __init__(self, *data):
        self._impl = NSObject.alloc().init()
        self._tree = None
        self.data = data
        self.children = []


class TreeDelegate_(object):
    TreeDelegate = ObjCSubclass('NSOutlineView', 'TreeDelegate')

    @TreeDelegate.method('@@i@')
    def outlineView_child_ofItem_(self, tree, child, item):
        if item is None:
            key = None
        else:
            key = id(item)

        node_id = self.interface._data[key]['children'][child]
        node = self.interface._data[node_id]['node']
        return node

    @TreeDelegate.method('B@@')
    def outlineView_isItemExpandable_(self, tree, item):
        if item is None:
            key = None
        else:
            key = id(item)

        return self.interface._data[key]['children'] is not None

    @TreeDelegate.method('i@@')
    def outlineView_numberOfChildrenOfItem_(self, tree, item):
        if item is None:
            key = None
        else:
            key = id(item)

        try:
            return len(self.interface._data[key]['children'])
        except TypeError:
            return 0

    @TreeDelegate.method('i@@@')
    def outlineView_objectValueForTableColumn_byItem_(self, tree, column, item):
        column_index = int(cfstring_to_string(column.identifier))
        return get_NSString(str(self.interface._data[id(item)]['data'][column_index]))

    @TreeDelegate.method('v@')
    def outlineViewSelectionDidChange_(self, notification):
        print ("tree selection changed")


TreeDelegate = ObjCClass('TreeDelegate')

class Tree(Widget):
    def __init__(self, headings):
        super(Tree, self).__init__()
        self.headings = headings

        self._tree = None
        self._columns = None

        self._data = {
            None: {
                'children': []
            }
        }

        self.startup()

    def startup(self):
        self._impl = NSScrollView.alloc().init()
        self._impl.setHasVerticalScroller_(True)
        self._impl.setHasHorizontalScroller_(True)
        self._impl.setAutohidesScrollers_(False)
        self._impl.setBorderType_(NSBezelBorder)
        self._impl.setTranslatesAutoresizingMaskIntoConstraints_(False)

        self._tree = TreeDelegate.alloc().init()
        self._tree.interface = self
        self._tree.setColumnAutoresizingStyle_(NSTableViewUniformColumnAutoresizingStyle)
        self._columns = [
            NSTableColumn.alloc().initWithIdentifier_(get_NSString('%d' % i))
            for i, heading in enumerate(self.headings)
        ]

        for heading, column in zip(self.headings, self._columns):
            self._tree.addTableColumn_(column)
            cell = column.dataCell()
            cell.setEditable_(False)
            cell.setSelectable_(False)
            column.valueForKey_(get_NSString('headerCell')).setStringValue_(get_NSString(heading))

        self._tree.setOutlineTableColumn_(self._columns[0])
        self._tree.setDelegate_(self._tree)
        self._tree.setDataSource_(self._tree)
        self._impl.setDocumentView_(self._tree)

    def reload_data(self):
        self._tree.reloadData()

    def insert(self, parent, index, *data):
        if len(data) != len(self.headings):
            raise Exception('Data size does not match number of headings')

        node = NSObject.alloc().init()
        parent_node = self._data[parent]
        if parent_node['children'] is None:
            parent_node['children'] = []
        if index is None:
            parent_node['children'].append(id(node))
        else:
            parent_node['children'].insert(index, id(node))

        self._data[id(node)] = {
            'node': node,
            'data': data,
            'children': None,
        }
        
        self.reload_data()
        return id(node)
