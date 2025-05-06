"""."""

from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget


class MainWindow(QWidget):
  """Main window of the application."""

  def __init__(self) -> None:
    """."""
    super().__init__()
    self.setWindowTitle("Logiciel modulaire")
    self.resize(400, 300)

    self.label = QLabel("Bienvenue !")
    self.button = QPushButton("Action")

    self.button.clicked.connect(self.update_label)

    layout = QVBoxLayout()
    layout.addWidget(self.label)
    layout.addWidget(self.button)

    self.setLayout(layout)

  def update_label(self) -> None:
    """."""
    self.label.setText("Action effectuée !")
