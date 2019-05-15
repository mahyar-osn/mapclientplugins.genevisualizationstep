import os, platform, time

from scaffoldmaker.utils.zinc_utils import *

from opencmiss.zinc.graphics import Graphics
from opencmiss.zinc.field import Field
from opencmiss.zinc.glyph import Glyph
from opencmiss.utils.maths import vectorops
from opencmiss.zinc.status import OK as ZINC_OK


class ScaffoldModel(object):

    def __init__(self, filename, context, region, material_module):
        super(ScaffoldModel, self).__init__()
        self._filename = filename
        self._context = context
        self._scaffold_region = region
        self._coordinates = None
        self._scale = [1.0, 1.0, 1.0]
        self._material_module = material_module
        self._settings = {'display_surface': True}

    def _create_graphics(self):
        self._create_line_graphics()
        self._create_surface_graphics()

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
        fm = self._scaffold_region.getFieldmodule()
        fm.beginChange()
        self._coordinates = fm.findFieldByName('coordinates')
        self._scene = self._scaffold_region.getScene()
        self._magnitude = fm.createFieldMagnitude(self._coordinates)
        self._magnitude.setName('magnitude')
        self._magnitude.setManaged(True)
        fm.endChange()
        # if self._sceneChangeCallback is not None:
        #     self._sceneChangeCallback()

    def _get_mesh(self):
        fm = self._scaffold_region.getFieldmodule()
        for dimension in range(3, 0, -1):
            mesh = fm.findMeshByDimension(dimension)
            if mesh.getSize() > 0:
                break
        if mesh.getSize() == 0:
            mesh = fm.findMeshByDimension(3)
        return mesh

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
        materialmodule = self._context.getMaterialmodule()

        # view the 1-D line elements on the edges of the cube
        lines = self._scene.createGraphicsLines()
        lines.setCoordinateField(self._coordinates)
        lines.setName('display_lines')
        black = self._material_module.findMaterialByName('heart_lines')
        lines.setMaterial(black)

        # view coordinate axes at the origin
        axes = self._scene.createGraphicsPoints()
        axes.setFieldDomainType(Field.DOMAIN_TYPE_POINT)
        pointAttr = axes.getGraphicspointattributes()
        pointAttr.setGlyphShapeType(Glyph.SHAPE_TYPE_AXES_XYZ)
        pointAttr.setBaseSize([1.2])
        blue = materialmodule.findMaterialByName('blue')
        axes.setMaterial(blue)

        # view the nodes at the corners of the cube as green spheres
        # nodepoints = self._scene.createGraphicsPoints()
        # nodepoints.setFieldDomainType(Field.DOMAIN_TYPE_NODES)
        # nodepoints.setCoordinateField(self._coordinates)
        # pointAttr = nodepoints.getGraphicspointattributes()
        # pointAttr.setGlyphShapeType(Glyph.SHAPE_TYPE_SPHERE)
        # pointAttr.setBaseSize([0.05])
        # green = materialmodule.findMaterialByName('green')
        # nodepoints.setMaterial(green)

        # view 'isosurfaces' where the magnitude of coordinates equals 1.0
        # isosurfaces = self._scene.createGraphicsContours()
        # isosurfaces.setCoordinateField(self._coordinates)
        # isosurfaces.setIsoscalarField(self._magnitude)
        # isosurfaces.setListIsovalues(1.0);
        # gold = materialmodule.findMaterialByName('gold')
        # isosurfaces.setMaterial(gold)
        # # use finer tessellation to see the curvature of the isosurfaces
        # tessellationmodule = self._context.getTessellationmodule()
        # fineTessellation = tessellationmodule.createTessellation()
        # fineTessellation.setName('fine') # name it so it can be found by name later
        # fineTessellation.setManaged(True) # manage its lifetime so it is kept even if not being used
        # fineTessellation.setMinimumDivisions(8) # divide element edges into 8 line segments
        # isosurfaces.setTessellation(fineTessellation)

        surface = self._scene.createGraphicsSurfaces()
        surface.setCoordinateField(self._coordinates)
        surface.setRenderPolygonMode(Graphics.RENDER_POLYGON_MODE_SHADED)
        surface_material = self._material_module.findMaterialByName('heart_tissue')
        surface.setMaterial(surface_material)
        surface.setName('display_surface')
        surface.setVisibilityFlag(self.is_display_surface('display_surface'))

        # self._create_graphics()

        self._scene.endChange()

        # line = self._create_line_graphics()
        # line.setRenderLineWidth(2.5)
        # self._surface = self._create_surface_graphics()

    def set_display_objects(self, surface_name, show):
        self._set_visibility(surface_name, show)

    def _set_visibility(self, graphics_name, show):
        self._initialize_scaffold()
        self._generate_mesh()
        self._setup_scene()
        self._settings[graphics_name] = show
        if 'display_surface' in graphics_name:
            graphics = self._scaffold_region.getScene().findGraphicsByName(graphics_name)
            graphics.setVisibilityFlag(show)
