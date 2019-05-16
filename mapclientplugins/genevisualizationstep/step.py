
"""
MAP Client Plugin Step
"""
import os
import json

from PySide import QtGui

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from .configuredialog import ConfigureDialog
from .utils.visualization import VisualizationHandler
from .model.master import MasterModel
from .view.geneview import GeneViewWidget


class GeneVisualizationStep(WorkflowStepMountPoint):
    """
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    """

    def __init__(self, location):
        super(GeneVisualizationStep, self).__init__('Gene Visualization', location)
        self._configured = False # A step cannot be executed until it has been configured.
        self._category = 'Image Processing'
        # Add any other initialisation code here:
        self._icon = QtGui.QImage(':/genevisualizationstep/images/image-processing.png')
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'data_frame'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'))
        # Port data:
        self._dataframe = None # data_frame
        self._scaffold = None # data_frame
        self._xml = None # data_frame
        # Config:
        self._config = {}
        self._config['identifier'] = ''

        self._model = None
        self._view = None
        self._visual_handler = None

    def execute(self):
        """
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        """
        # Put your execute step code here before calling the '_doneExecution' method.
        self._visual_handler = VisualizationHandler(self._dataframe)
        # vis.viewTable()

        all_settings = {}
        try:
            with open(self._getSettingsFileName()) as f:
                all_settings = json.loads(f.read())
        except EnvironmentError:
            pass

        self._model = MasterModel(self._scaffold)
        self._view = GeneViewWidget(self._model, self._visual_handler)

        if 'view' in all_settings:
            self._view.set_settings(all_settings['view'])

        self._view.register_done_callback(self._interactionDone)
        self._setCurrentWidget(self._view)

    def _interactionDone(self):
        all_settings = {'view': self._view.get_settings()}
        settings_in_string_form = json.dumps(all_settings, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        with open(self._getSettingsFileName(), 'w') as f:
            f.write(settings_in_string_form)

        self._view = None
        self._doneExecution()

    def _getSettingsFileName(self):
        return os.path.join(self._location, self._config['identifier'] + '.settings')

    def setPortData(self, index, dataIn):
        """
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.

        :param index: Index of the port to return.
        :param dataIn: The data to set for the port at the given index.
        """
        if index == 0:
            self._dataframe = dataIn  # electrode_positions
        elif index == 1:
            self._scaffold = dataIn  # scaffold_parameters
        elif index == 2:
            self._xml = dataIn  # 2d_image_dimension

    def configure(self):
        """
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        """
        dlg = ConfigureDialog(self._main_window)
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()

        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        """
        The identifier is a string that must be unique within a workflow.
        """
        return self._config['identifier']

    def setIdentifier(self, identifier):
        """
        The framework will set the identifier for this step when it is loaded.
        """
        self._config['identifier'] = identifier

    def serialize(self):
        """
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        """
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        """
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.

        :param string: JSON representation of the configuration in a string.
        """
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()


