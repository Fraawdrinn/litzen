"""."""

import sys

from PyQt5.QtWidgets import QApplication

from litzen.main_window import MainWindow

app = QApplication(sys.argv)
window = MainWindow()

def main() -> None:
  """."""
  window.show()
  sys.exit(app.exec_())


if __name__ == "__main__":
    main()
