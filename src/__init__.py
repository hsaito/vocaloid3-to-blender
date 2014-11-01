bl_info={
    'category': 'Import-Export',
    'name': 'Vocaloid3 (vsqx) importer',
    'author': 'Hideki Saito',
    'blender': (2, 7, 2),
    'location': 'File > Import-Export',
    'description': 'Import Vocaloid3 files for lipsync',
    'warning': 'Vocaloid3 importer is still pre-alpha.', 
    'wiki_url': 'https://github.com/hsaito/vocaloid3-to-blender',
    'support': 'COMMUNITY',
}

if "bpy" in locals():
    import imp
    if "import_vocaloid3" in locals():
        imp.reload(import_vocaloid3)

import bpy
from bpy.props import (StringProperty,
                       FloatProperty,
                       IntProperty,
                       BoolProperty,
                       EnumProperty,
                       )

from bpy_extras.io_utils import (ImportHelper,
                                 ExportHelper,
                                 axis_conversion,
                                 )


class Vocaloid3ImportMenu(bpy.types.Menu):
    bl_label = "Choose a track to import"
    bl_idname = "OBJECT_MT_vocaloid3_ipmort"

    def draw(self, context):
        layout = self.layout

        # layout.label(text="Hello world!", icon='WORLD_DATA')

        # use an operator enum property to populate a sub-menu
        # TODO: Code to populate Vocaloid track
        # HOW?: Parase by, vsTrackNo -- display name would be "<vsTrackNo>: <trackName>"
        # The tricky part is that Vocaloid3 editor allows non-vocaloid track (e.g. WAV) to be there, so we need to separate those.
        # (or leave them up to users and gracefully fail?)


def draw_item(self, context):
    layout = self.layout
    layout.menu(Vocaloid3ImportMenu.bl_idname)


def register():
    bpy.utils.register_class(Vocaloid3ImportMenu)

    # lets add ourselves to the main header
    #bpy.types.INFO_HT_header.append(draw_item)


def unregister():
    bpy.utils.unregister_class(Vocaloid3ImportMenu)

    bpy.types.INFO_HT_header.remove(draw_item)

if __name__ == "__main__":
    register()

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=Vocaloid3ImportMenu.bl_idname)

def read_some_data(context, filepath, use_some_setting):
    print("running Vocaloid3 Importer...")
    f = open(filepath, 'r', encoding='utf-8')
    data = f.read()
    f.close()
    bpy.ops.wm.call_menu(name=Vocaloid3ImportMenu.bl_idname)
    # would normally load the data here
    print(data)

    return {'FINISHED'}


# ImportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


class ImportSomeData(Operator, ImportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "import_vocaloid3.vsqx_data"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Import Vocaloid3 Data"

    # ImportHelper mixin class uses this
    filename_ext = ".vsqx"

    filter_glob = StringProperty(
            default="*.vsqx",
            options={'HIDDEN'},
            )

    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.
    use_setting = BoolProperty(
            name="Placeholder",
            description="Placeholder",
            default=True,
            )

    type = EnumProperty(
            name="Import Options",
            description="Choose between two items",
            items=(('OPT_A', "Option 1 Placeholder", "Description one"),
                   ('OPT_B', "Option 2 Placeholder", "Description two")),
            default='OPT_A',
            )

    def execute(self, context):
        return read_some_data(context, self.filepath, self.use_setting)


# Only needed if you want to add into a dynamic menu
def menu_func_import(self, context):
    self.layout.operator(ImportSomeData.bl_idname, text="Vocaloid3 Import Operator")


def register():
    bpy.utils.register_class(ImportSomeData)
    bpy.types.INFO_MT_file_import.append(menu_func_import)


def unregister():
    bpy.utils.unregister_class(ImportSomeData)
    bpy.types.INFO_MT_file_import.remove(menu_func_import)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.import_vocaloid3.vsqx_data('INVOKE_DEFAULT')

