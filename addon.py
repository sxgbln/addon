import bpy
# Specify the material name
mat_name = "MyMaterial"
# Test if material exists, if it does not exist, create it:
mat = (bpy.data.materials.get(mat_name) or 
       bpy.data.materials.new(mat_name))
# Enable 'Use nodes':
mat.use_nodes = True
nodes = mat.node_tree.nodes
links = mat.node_tree.links
# Clear existing nodes (optional, to start with a clean slate)
nodes.clear()
# Add an Output Material node and set its location:
material_output = nodes.new('ShaderNodeOutputMaterial')
material_output.location = (400, 100)
# Link the Principled BSDF to the Material Output
#links.new(image_texture_node.outputs['Color'], material_output.inputs['Surface'])
#add mix node
mix_node = nodes.new("ShaderNodeMixRGB")
mix_node.location = (0, 250) 
#add diffuse node
diff_node = nodes.new("ShaderNodeBsdfDiffuse")
diff_node.location = (183,155)
#create links, diff to output
links.new(diff_node.outputs["BSDF"], material_output.inputs["Surface"])
#link mix to diffuse
links.new(mix_node.outputs["Color"], diff_node.inputs["Color"])
# Add an Image Texture node and set its location:
image_texture_node = nodes.new('ShaderNodeTexImage')
image_texture_node.location = (-300, 350)
#link img node to mix color
links.new(image_texture_node.outputs["Color"], mix_node.inputs["Color1"])
#create second img texture node
image_texture_node1 = nodes.new('ShaderNodeTexImage')
image_texture_node1.location = (-300, 100)
#link second img node
links.new(image_texture_node1.outputs["Color"], mix_node.inputs["Color2"])
#add math node
math_node = nodes.new("ShaderNodeMath")
math_node.location = (0,450)
#set 2 greater than
math_node.operation = "GREATER_THAN"
#link math 2 mix 
links.new(math_node.outputs["Value"], mix_node.inputs["Fac"])
#set thresh 4 math
math_node.inputs[1].default_value = 1
#create value node
value_node = nodes.new("ShaderNodeValue")
value_node.location = (0,550)
#set link value 2 math
links.new(value_node.outputs["Value"], math_node.inputs["Value"])







