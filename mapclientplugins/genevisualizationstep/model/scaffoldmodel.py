import os, platform, time

from scaffoldmaker.utils.zinc_utils import *

from opencmiss.zinc.graphics import Graphics
from opencmiss.zinc.field import Field
from opencmiss.utils.maths import vectorops
from opencmiss.zinc.status import OK as ZINC_OK


class ScaffoldModel(object):

    def __init__(self, filename, context, region, material_module):
        self._filename = filename
        self._context = context
        self._scaffold_region = region
        self._initialize_scaffold()

        self._settings = {'display_surface': True}

        self._filedmodule = self._scaffold_region.getFieldmodule()
        self._coordinates = self._filedmodule.findFieldByName('coordinates')

        self._material_module = material_module
        self._scene = self._scaffold_region.getScene()
        self._setup_scene()

        # self._generate_mesh()

    def _create_line_graphics(self):
        lines = self._scene.createGraphicsLines()
        lines.setCoordinateField(self._coordinates)
        lines.setName('display_lines')
        black = self._material_module.findMaterialByName('heart_lines')
        lines.setMaterial(black)
        return lines

    def _create_scene(self):
        return self._scaffold_region.getScene()

    def _create_surface_graphics(self):
        surface = self._scene.createGraphicsSurfaces()
        surface.setCoordinateField(self._coordinates)
        surface.setRenderPolygonMode(Graphics.RENDER_POLYGON_MODE_SHADED)
        surface_material = self._material_module.findMaterialByName('heart_tissue')
        surface.setMaterial(surface_material)
        surface.setName('display_surface')
        surface.setVisibilityFlag(self.is_display_surface('display_surface'))
        return surface

    def _generate_mesh(self):
        self._filedmodule.beginChange()
        self._magnitude = self._filedmodule.createFieldMagnitude(self._coordinates)
        self._magnitude.setName('magnitude')
        self._magnitude.setManaged(True)
        self._filedmodule.endChange()

    def _get_visibility(self, graphics_name):
        return self._settings[graphics_name]

    def _initialize_scaffold(self):
        # tmp = 'D:\sparc\codes\maplcinet_workflows\scaffoldmaker\mesh.exf'
        result = self._scaffold_region.readFile(self._filename)
        if result == ZINC_OK:
            pass
        else:
            print("Scaffold ex file was not read correctly! Check the path.")
        # logger = self._context.getLogger()
        # num = logger.getNumberOfMessages()
        # print(num)
        # for i in range(1, num):
        #     print(logger.getMessageTextAtIndex(i))

    def is_display_surface(self, surface_name):
        return self._get_visibility(surface_name)

    def _setup_scene(self):
        self._scene = self._create_scene()
        self._scene.beginChange()
        line = self._create_line_graphics()
        line.setRenderLineWidth(2.5)
        self._surface = self._create_surface_graphics()

    def set_display_objects(self, surface_name, show):
        self._set_visibility(surface_name, show)

    def _set_visibility(self, graphics_name, show):
        self._settings[graphics_name] = show
        if 'display_surface' in graphics_name:
            graphics = self._scaffold_region.getScene().findGraphicsByName(graphics_name)
            graphics.setVisibilityFlag(show)
