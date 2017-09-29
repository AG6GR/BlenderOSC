import bpy, json

def osc_export_config(scene):
    config_table = {};
    for osc_item in scene.OSC_keys:
        config_table[osc_item.address] = {
            "data_path" : osc_item.data_path,
            "id" : osc_item.id,
            "type" : osc_item.osc_type
        };
    
    print(json.dumps(config_table));

if __name__ == "__main__":
    osc_export(bpy.context.scene);