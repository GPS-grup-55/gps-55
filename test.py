import io
import runpy
import unittest
from unittest.mock import patch

import main
import transform


class TestStringMethods(unittest.TestCase):

    def test_is_upper(self):
        sting = transform.to_upper_case("hello")
        self.assertEqual(sting, "HELLO")

    def test_is_lower(self):
        sting = transform.to_lower_case("HELLO")
        self.assertEqual(sting, "hello")

    def test_is_capitalize(self):
        sting = transform.to_capitalize("HELLO")
        self.assertEqual(sting, "Hello")


class MainTests(unittest.TestCase):
    def run_main_with_inputs(self, inputs):
        """Run main() while feeding the mocked inputs and capture stdout."""
        with patch("builtins.input", side_effect=inputs):
            with patch("sys.stdout", new_callable=io.StringIO) as fake_out:
                main.main()
                return fake_out.getvalue()

    def test_option_upper_prints_uppercase_result(self):
        output = self.run_main_with_inputs(["hello", "1"])
        self.assertIn("HELLO", output)

    def test_option_lower_prints_lowercase_result(self):
        output = self.run_main_with_inputs(["HELLO", "2"])
        self.assertIn("hello", output)

    def test_option_capitalize_prints_capitalized_result(self):
        output = self.run_main_with_inputs(["hELLo", "3"])
        self.assertIn("Hello", output)

    def test_invalid_option_reports_unrecognized_choice(self):
        output = self.run_main_with_inputs(["irrelevant", "4"])
        self.assertIn("opció no reconegudda", output)

    def test_module_entrypoint_executes_when_run_as_script(self):
        """The guard at the bottom should run when the module is executed directly."""
        with patch("builtins.input", side_effect=["runpy", "2"]):
            with patch("sys.stdout", new_callable=io.StringIO) as fake_out:
                runpy.run_module("main", run_name="__main__")
        self.assertIn("Quina transformació vols?", fake_out.getvalue())


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
