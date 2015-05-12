from .widget import *

class WebViewDelegate_(object):
    WebViewDelegate = ObjCSubclass('WebView', 'WebViewDelegate')

    @WebViewDelegate.method('v@@')
    def webView_didFinishLoadForFrame_(self, sender, frame):
        if self.interface.on_progress_finish:
            Widget.callback(self.interface.on_progress_finish())

    def webView_progressStartedNotification_(self, notification):
        if self.interface.on_progress_started:
            Widget.callback(self.interface.on_progress_started())

WebViewDelegate = ObjCClass('WebViewDelegate')

class WebView(Widget):
    def __init__(self, url=None, on_progress_started=None, on_progress_finish=None):
        super(WebView, self).__init__()

        self.startup()
        self.url = url
        self.on_progress_started = on_progress_started
        self.on_progress_finish = on_progress_finish

    def startup(self):
        self._impl = WebViewDelegate.alloc().init()
        self._impl.interface = self
        self._impl.setDownloadDelegate_(self._impl)
        self._impl.setFrameLoadDelegate_(self._impl)
        self._impl.setPolicyDelegate_(self._impl)
        self._impl.setResourceLoadDelegate_(self._impl)
        self._impl.setUIDelegate_(self._impl)
        self._impl.setTranslatesAutoresizingMaskIntoConstraints_(False)

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
        if value:
            request = NSURLRequest.requestWithURL_(NSURL.URLWithString_(get_NSString(self._url)))
            self._impl.mainFrame().loadRequest_(request)

    def can_go_back(self):
        return self._impl.canGoBack()

    def go_back(self):
        self._impl.goBack()

    def can_go_forward(self):
        return self._impl.canGoForward()

    def go_forward(self):
        self._impl.goForward()

    def goToItemAtIndex(self, index):
        self._impl.goToBackForwardItem(index)

    def estimated_progress(self):
        return self._impl.estimatedProgress()

    def reload(self):
        self._impl.reload()

    def stop_loading(self):
        self._impl.stopLoading()
