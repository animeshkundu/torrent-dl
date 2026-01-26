"""Unit tests for Pyflix.utils.decorators module.

These tests characterize the existing behavior of decorators.
They capture BEHAVIOR, not correctness.
"""

import pytest
from unittest.mock import patch, MagicMock


class TestWithConfigDir:
    """Tests for with_config_dir decorator."""

    def test_decorator_returns_callable(self):
        """with_config_dir should return a callable."""
        from Pyflix.utils.decorators import with_config_dir
        
        @with_config_dir
        def dummy_func():
            pass
        
        assert callable(dummy_func)

    def test_decorated_function_is_called(self):
        """Decorated function should be called."""
        from Pyflix.utils.decorators import with_config_dir
        
        call_count = [0]
        
        @with_config_dir
        def counting_func():
            call_count[0] += 1
            return "result"
        
        result = counting_func()
        assert call_count[0] == 1
        assert result == "result"

    def test_decorated_function_receives_arguments(self):
        """Decorated function should receive its arguments."""
        from Pyflix.utils.decorators import with_config_dir
        
        @with_config_dir
        def echo_func(a, b, c=None):
            return (a, b, c)
        
        result = echo_func(1, 2, c=3)
        assert result == (1, 2, 3)

    @patch('Pyflix.utils.decorators.set_config_dir')
    def test_calls_set_config_dir(self, mock_set_config):
        """with_config_dir should call set_config_dir."""
        from Pyflix.utils.decorators import with_config_dir
        
        @with_config_dir
        def dummy_func():
            return "done"
        
        dummy_func()
        mock_set_config.assert_called_once()

    @patch('Pyflix.utils.decorators.set_config_dir')
    def test_config_dir_set_before_function_execution(self, mock_set_config):
        """Config dir should be set before the decorated function runs."""
        from Pyflix.utils.decorators import with_config_dir
        
        order = []
        mock_set_config.side_effect = lambda: order.append('config')
        
        @with_config_dir
        def func():
            order.append('func')
        
        func()
        assert order == ['config', 'func']
