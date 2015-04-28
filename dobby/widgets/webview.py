from __future__ import print_function, absolute_import, division
from .base import Widget
from ..libs import *

class WebView_impl(object):
    WebViewImpl = ObjCSubclass('WebView', 'WebViewImpl')

    @WebViewImpl.method('v@@')
    def webView_didFinishLoadForFrame_(self, sender, frame):
        if self.interface.on_progress_finish:
            process_callback(self.interface.on_progress_finish())

    def webView_progressStartedNotification_(self, notification):
        if self.interface.on_progress_started:
            process_callback(self.interface.on_progress_started())

WebViewImpl = ObjCClass('WebViewImpl')

class WebView(Widget):
    def __init__(self, url=None, on_progress_started=None, on_progress_finish=None):
        super(WebView, self).__init__()

        self.startup()
        self.url = url
        self.on_progress_started = on_progress_started
        self.on_progress_finish = on_progress_finish

    def startup(self):
        self._impl = WebViewImpl.alloc().init()
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

    def canGoBack(self):
        return self._impl.canGoBack()

    def goBack(self):
        self._impl.goBack()

    def canGoForward(self):
        return self._impl.canGoForward()

    def goForward(self):
        self._impl.goForward()

    def goToBackForwardItem(self, index):
        self._impl.goToBackForwardItem(index)

    def estimatedProgress(self):
        return self._impl.estimatedProgress()

    def reload(self):
        self._impl.reload()

    def stopLoading(self):
        self._impl.stopLoading()
