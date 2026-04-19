"""
Project-level pytest configuration.

Forces UTF-8 as the default text encoding for Path.read_text() / write_text()
calls that omit an explicit encoding argument.  On Windows the locale default
is cp1252, which cannot round-trip Unicode characters (e.g. emoji) produced
by the session-log writer.  Patching io.text_encoding here is equivalent to
running pytest with PYTHONUTF8=1, but scoped to the test process only.
"""
import io as _io

_orig_text_encoding = _io.text_encoding


def _utf8_text_encoding(encoding, stacklevel=2):
    if encoding is None:
        return "utf-8"
    return _orig_text_encoding(encoding, stacklevel)


_io.text_encoding = _utf8_text_encoding
