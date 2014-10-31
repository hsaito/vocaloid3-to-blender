import bpy


def read_some_data(context, filepath, use_some_setting):
    print("running Vocaloid3 Importer...")
    f = open(filepath, 'r', encoding='utf-8')
    data = f.read()
    f.close()

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
    bpy.ops.import_test.some_data('INVOKE_DEFAULT')
