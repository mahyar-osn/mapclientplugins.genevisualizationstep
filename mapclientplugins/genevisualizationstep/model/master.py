from opencmiss.zinc.context import Context
from opencmiss.zinc.field import Field
from opencmiss.zinc.glyph import Glyph
from opencmiss.zinc.material import Material

from opencmiss.utils.zinc import define_standard_visualisation_tools
from opencmiss.utils.zinc import create_finite_element_field

from .scaffoldmodel import ScaffoldModel


class MasterModel(object):

    def __init__(self, scaffold_filename):
        self._mbf_region = None

        self._context = Context('RNA Mapping')
        self.logger = self._context.getLogger()
        define_standard_visualisation_tools(self._context)
        self._material_module = self._context.getMaterialmodule()

        self._initialize_material()

        self._scaffold_region = self._context.getDefaultRegion().createChild('scaffold')
        self._mbf_region = self._context.getDefaultRegion().createChild('mbf')

        self._scaffold = ScaffoldModel(scaffold_filename, self._context, self._scaffold_region, self._material_module)

    def _initialize_material(self):
        # self._coordinate_field = create_finite_element_field(self._mbf_region)
        tess = self._context.getTessellationmodule().getDefaultTessellation()
        tess.setRefinementFactors(12)
        self._material_module.defineStandardMaterials()
        solidTissue = self._material_module.createMaterial()
        solidTissue.setName('heart_tissue')
        solidTissue.setManaged(True)
        solidTissue.setAttributeReal3(Material.ATTRIBUTE_AMBIENT, [0.8, 0.43, 0.33])
        solidTissue.setAttributeReal3(Material.ATTRIBUTE_DIFFUSE, [0.8, 0.43, 0.33])
        solidTissue.setAttributeReal3(Material.ATTRIBUTE_EMISSION, [0.0, 0.0, 0.0])
        solidTissue.setAttributeReal3(Material.ATTRIBUTE_SPECULAR, [0.2, 0.2, 0.3])
        solidTissue.setAttributeReal(Material.ATTRIBUTE_ALPHA, 1.0)
        solidTissue.setAttributeReal(Material.ATTRIBUTE_SHININESS, 0.6)
        glyphmodule = self._context.getGlyphmodule()
        glyphmodule.defineStandardGlyphs()

    def get_context(self):
        return self._context

    def get_scene(self):
        return self._scaffold_region.getScene()

    def get_scaffold_model(self):
        return self._scaffold
