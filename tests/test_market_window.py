import unittest
from unittest import mock

from ui.market.market_window import MarketWindow


class _DummyMarketWindow:
    def __init__(self, minimized=False):
        self.minimized = minimized
        self.calls = []

    def refresh_market_data(self, force_remote=True):
        self.calls.append(('refresh_market_data', force_remote))

    def isMinimized(self):
        return self.minimized

    def showNormal(self):
        self.calls.append('showNormal')

    def parentWidget(self):
        return 'parent'


class MarketWindowTests(unittest.TestCase):
    def test_show_window_reuses_shared_window_launcher(self):
        window = _DummyMarketWindow(minimized=True)

        with mock.patch(
            'ui.market.market_window.center_window_on_widget_screen',
        ) as center_window_on_widget_screen:
            with mock.patch(
                'ui.market.market_window.show_and_activate_overlay',
            ) as show_and_activate_overlay:
                MarketWindow.show_window(window)

        self.assertEqual(
            window.calls,
            [('refresh_market_data', True), 'showNormal'],
        )
        center_window_on_widget_screen.assert_called_once_with(window, 'parent')
        show_and_activate_overlay.assert_called_once_with(
            window,
            log_prefix='脚本共享平台',
            focus=True,
        )
