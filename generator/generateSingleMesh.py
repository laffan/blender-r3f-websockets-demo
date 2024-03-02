import bpy
import os
import sys

text_content = "Loading..."
text_path = sys.argv[-1]  # Path to text file 
output_path = sys.argv[-2]  # Save to ... 

print( "TEXT PATH: " )
print( text_path )
print( "OUTPUT PATH: " )
print( output_path )

try:
    with open(text_path, 'r') as file:
        text_content = file.read().strip()
except Exception as e:
    print("FILE OPEN FAIL")
    print(f"Failed to open file: {e}")

print( "TEXT CONTENT: " )
print( text_content )

# Select the right layer
bpy.data.objects['SingleMesh'].select_set(True)
# Chnage the text in the geonodes
bpy.data.node_groups["SimpleTextToCurve"].nodes["InputText"].string = text_content
# Apply geonodes 
bpy.ops.object.modifier_apply(modifier="GeometryNodes")

# Continue with the export operation
bpy.ops.export_scene.gltf(filepath=output_path,
                          check_existing=False,
                          export_format='GLTF_SEPARATE',
                          export_colors=False)
