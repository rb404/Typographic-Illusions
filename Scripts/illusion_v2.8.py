"""
Author: 'rb404'
Blender v 2.8.0 
Tool: 'Typographic Illusion Script'
"""


import bpy
import os

#Deletes all existing elements
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

#Get font from font library. Change directory here.
fnt = bpy.data.fonts.load('C:\\WINDOWS\\Fonts\\impact.ttf')

#Change text here
firstChar = "A"
secondChar = "B"
size = 3
resizeFactor = 0.986549

#Obj/mtl export directory. Change directory here
directory = "C:\\Users\\Username\\Desktop"

#Create first text object
bpy.ops.object.text_add(enter_editmode=False, location=(0, 0, 0))
first = bpy.data.objects["Text"]
first.data.body = firstChar
bpy.context.object.data.size = size
bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.context.object.data.extrude = 8
first.data.font = fnt
bpy.ops.object.convert(target='MESH', keep_original= False)
bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')

bpy.context.object.location[0] = 0
bpy.context.object.location[1] = 0  

#Create second text object
bpy.ops.object.text_add(enter_editmode=False, location=(0, 0, 0))
second = bpy.data.objects["Text.001"]
second.data.body = secondChar
bpy.context.object.data.size = size
bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.transform.rotate(value=1.5708, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.context.object.data.extrude = 8
second.data.font = fnt
bpy.ops.object.convert(target='MESH', keep_original= False)
bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')

bpy.context.object.location[0] = 0
bpy.context.object.location[1] = 0

bpy.ops.transform.resize(value=(resizeFactor, resizeFactor, resizeFactor), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)


#Apply boolean modifier
bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].operation = 'INTERSECT'
bpy.context.object.modifiers["Boolean"].object = first
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

#Delete first text mesh
bpy.ops.object.select_all(action='DESELECT')
first.select_set(True)
bpy.ops.object.delete()

#Apply normal auto smoothing
bpy.context.object.data.use_auto_smooth = True

#Export obj/mtl to directory
blend_file_path = bpy.data.filepath
directory = os.path.dirname(blend_file_path)
target_file = os.path.join(directory, 'letters.obj')

bpy.ops.export_scene.obj(filepath=target_file)