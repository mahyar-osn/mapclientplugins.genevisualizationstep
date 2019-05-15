from PySide import QtGui, QtCore

# from mapclientplugins.genevisualizationstep.view.ui_geneview import Ui_GeneVisualizationWidget
from .ui_geneview import Ui_GeneVisualizationWidget


class GeneViewWidget(QtGui.QWidget):

    def __init__(self, model, parent=None):
        super(GeneViewWidget, self).__init__(parent)
        self._scaffold_model = model.get_scaffold_model()
        self._logger = model.logger
        self._model = model
        self._ui = Ui_GeneVisualizationWidget()
        self._ui.setupUi(self)
        self._ui.sceneviewerWidget.set_context(self._model.get_context())
        self._make_connections()

        self._settings = {'view-parameters': {}}
        self._done_callback = None

    def _done_clicked(self):
        self._done_callback()

    def set_settings(self, settings):
        self._settings.update(settings)

    def get_settings(self):
        eye, look_at, up, angle = self._ui.sceneviewerWidget.getViewParameters()
        self._settings['view-parameters'] = {'eye': eye, 'look_at': look_at, 'up': up, 'angle': angle}
        return self._settings

    def _make_connections(self):
        self._ui.sceneviewerWidget.graphics_initialized.connect(self._graphics_initialized)
        self._ui.viewScaffoldButton.clicked.connect(self._show_scaffold)

    def _graphics_initialized(self):
        scene_viewer = self._ui.sceneviewerWidget.get_zinc_sceneviewer()
        if scene_viewer is not None:
            scene = self._model.get_scene()
            self._ui.sceneviewerWidget.set_tumble_rate(0)
            self._ui.sceneviewerWidget.set_scene(scene)
            if len(self._settings['view-parameters']) == 0:
                self._view_all()
            else:
                eye = self._settings['view-parameters']['eye']
                look_at = self._settings['view-parameters']['look_at']
                up = self._settings['view-parameters']['up']
                angle = self._settings['view-parameters']['angle']
                self._ui.sceneviewerWidget.set_view_parameters(eye, look_at, up, angle)

    def _view_all(self):
        if self._ui.sceneviewerWidget.get_zinc_sceneviewer() is not None:
            self._ui.sceneviewerWidget.view_all()

    def register_done_callback(self, done_callback):
        self._done_callback = done_callback

    def _show_scaffold(self):
        self._scaffold_model.set_display_objects('display_surface', True)
