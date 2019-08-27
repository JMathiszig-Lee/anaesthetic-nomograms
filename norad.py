from pynomo.nomographer import *


ml_hr = {
    #mls an hour of single strength
    'u_min': 0,
    'u_max': 40.0,
    'function': lambda u: u * 80 ,
    'title': r'mls/hr (4mg/50mls)',
    'tick_levels': 3,
    'tick_text_levels': 2,
    'title_draw_center': True,
    'title_distance_center': 1.5,

}

ml_hr_dbl = {
    #mls an hour for double strength norad
    #mls an hour of single strength
    'u_min': 0,
    'u_max': 20,
    'function': lambda u: u * 160 ,
    'align_func': lambda u: u/2,
    'title': r'mls/hr (8mg/50mls)',
    'tick_levels': 2,
    'tick_text_levels': 1,
    'tick_side': 'left',
    'title_draw_center': True,
    'title_distance_center': -1.5,
    


}

wt_kg = {
    #patient weight in kg
    'u_min': 0,
    'u_max': 120,
    'function': lambda u: 60 * u ,
    'title': r'weight (kg)',
    'tick_levels': 3,
    'tick_text_levels': 2,

}

mcg_kg_min = {
    #mcg per kg per min
    'u_min': 0.05,
    'u_max': 1,
    'function': lambda u: 1/ u ,
    'title': r'mcg/kg/min',
    'tick_levels': 3,
    'tick_text_levels': 2,
    'extra_params':[{
        'u_min': 0.55,
        'u_max': 1,
        'tick_levels': 1,
        'tick_text_levels': 0,
    }],
    'scale_type': 'log',
    
    


}

block_SI = {
    'block_type': 'type_2',
    'f1_params': wt_kg,
    'f2_params': ml_hr,
    'f3_params': mcg_kg_min,
}
block_DBL = {
    'block_type': 'type_2',
    'f1_params': wt_kg,
    'f2_params': ml_hr_dbl,
    'f3_params': mcg_kg_min,
}


main_params = {
    'filename': 'norad.pdf',
    'paper_height':15.0,
    'paper_width':10,
    'block_params': [block_SI, block_DBL],
    'transformations': [('rotate', 0.01), ('scale paper',)],
    'title_str': r'\LARGE Noradrenaline calculator',
}


Nomographer(main_params)
