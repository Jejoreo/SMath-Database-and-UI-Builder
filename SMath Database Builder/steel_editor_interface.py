import io
import sqlite3
import PySimpleGUI as sg
import steel_backend as sb
from PIL import Image

'''
#* ---------------------First Section: Index Path ----------------------------------------------------------
#  TODO:
#* Note:
#? Question: 
#! Error: 
#* ---------------------------------------------------------------------------------------------------------
'''
w_path = r'C:\Users\jevon\OneDrive\Documents\God Knows What\Code Palace\Steel Profiler Project\WF_INDEX.PNG'
l_path = r'C:\Users\jevon\OneDrive\Documents\God Knows What\Code Palace\Steel Profiler Project\L_INDEX.PNG'
c_path = r'C:\Users\jevon\OneDrive\Documents\God Knows What\Code Palace\Steel Profiler Project\C_INDEX.PNG'

'''
#* ---------------------Second Section: Image Method --------------------------------------------------------
#  TODO:
#* Note: Resize and store the image before sticking it to sg.Image()
#? Question: 
#! Error: 
#* ---------------------------------------------------------------------------------------------------------
'''
def load_img(img_path):
    image = Image.open(img_path)
    image.thumbnail((190, 250))
    bio = io.BytesIO()
    #! Actually store the image in memory in binary 
    image.save(bio, format="PNG")
    return bio.getvalue()  #* return the contents of the stream

'''
#* ---------------------Third Section: Index Path ----------------------------------------------------------
#  TODO:Fix edit_section_name() 
#* Note: This section contains the W profile layout
#? Question:  
#! Error: Popup returns None due to spagetti backend code
#* ---------------------------------------------------------------------------------------------------------
'''
def make_w_layout():
    #* W Profile action layout
    action_layout = [
        [sg.Button('Refresh', key='-W_REFRESH-', size=(15,1))],
        [sg.Button('Submit Profile', key='-W_SUBMIT-', size=(15,1))],
        [sg.Button('Delete by Name', key='-W_DELETE-', size=(15,1))],
        [sg.Button('Clear Window', key='-W_CLEAR-', size=(15,1))],
        [sg.Button('Exit', key='-W_EXIT-', size=(15,1))],
    ]
    action_frame = [sg.Frame(
        'Action',
        action_layout,
        element_justification='center',
        key='-W_ACTION-',
    ),]
    
    #* Index + Action layout
    themes = sg.theme_list()
    
    layout_1 = [
        [sg.T('W Profile Index', font='Arial 12')],
        [sg.Image(
            source=load_img(w_path),
            size = (190, 220),
            tooltip='W Profile Image Index',
            )],
        [sg.T('Choose Theme: '),
        sg.Combo(
            themes,
            key='-W_THEME-',
            # default_value = 'LightGrey1',
            size=(12,1),
            enable_events=True,
            )],
        action_frame,
    ]

    tooltip_list = [
        'Enter WF Profile Name (Ex: W 300x400x5x2)',
        'Enter Profile Weight (Ex: 300 Kgf/m)',
        'Enter Profile Height (Ex: 15 cm)',
        'Enter Profile Width (Ex: 30 cm)',
        'Enter Flage Thickness (Ex: 5.2 cm)',
        'Enter Web Thickness (Ex: 3 cm)',
        'Enter Radius (Ex: 2.5 cm)',
        'Enter Area (Ex: 1000 cm^2)',
        'Enter Moment of Inertia -X (Ex: 12789 cm^4)',
        'Enter Moment of Inertia -Y (Ex: 6789 cm^4)',
        'Enter Radius of Gyration - X (Ex: 15 cm )',
        'Enter Radius of Gyration - Y (Ex: 20 cm)',
        'Enter Section Modulii - X (Ex: 3840 cm^3)',
        'Enter Section Modulii - Y (Ex: 3840 cm^3)',
    ]

    # Data Input layout
    name = sb.get_w_name_cb()
    cb_value = [item for sublist in name for item in sublist]

    layout_2 = [
        [sg.T('Quick Edit: ', pad=((5,5),(20,10))),
        sg.Combo(
                values= cb_value,
                enable_events=True,
                size=(25, 1),
                key='-W_CB_WPROFILE-',
                tooltip='Select Profile',
                pad=((5,5),(20,10)),
            )],
        [sg.T('Section Name: '), 
        sg.Input(key='-W_SECTION_NAME-', size=(15,1), pad=((60,5),(5,5)), tooltip=tooltip_list[0], do_not_clear=True), 
        sg.Button('Edit', key='-W_EDIT_NAME-', size=(5,1), pad=(9,0))],
        
        [sg.T('Weight: '), 
        sg.Input(key='-W_WEIGHT-', size=(15,1), pad=((100,5),(5,5)), tooltip=tooltip_list[1], do_not_clear=True), 
        sg.Button('Edit', key='-W_EDIT_WEIGHT-', size=(5,1), pad=(9,0))],
        
        [sg.T('Height (H): '), 
        sg.Input(key='-W_HEIGHT-', size=(15,1), pad=((83,5),(5,5)), tooltip=tooltip_list[2], do_not_clear=True), 
        sg.Button('Edit', key='-W_EDIT_HEIGHT-', size=(5,1), pad=(9,0))],
        
        [sg.T('Width (B): '), 
        sg.Input(key='-W_WIDTH-', size=(15,1), pad=((86,5),(5,5)), tooltip=tooltip_list[3], do_not_clear=True), 
        sg.Button('Edit', key='-W_EDIT_WIDTH-', size=(5,1), pad=(9,0))],
        
        [sg.T('Flange Thickness (tf): '), 
        sg.Input(key='-W_TF-', size=(15,1), pad=((20,5),(5,5)), tooltip=tooltip_list[4], do_not_clear=True), 
        sg.Button('Edit', key='-W_EDIT_TF-', size=(5,1), pad=(9,0))],
        
        [sg.T('Web Thickness (tw): '), 
        sg.Input(key='-W_TW-', size=(15,1), pad=((26,5),(5,5)), tooltip=tooltip_list[5], do_not_clear=True), 
        sg.Button('Edit', key='-W_EDIT_TW-', size=(5,1), pad=(9,0))],
        
        [sg.T('Radius (R): '), 
        sg.Input(key='-W_R-', size=(15,1), pad=((79,5),(5,5)), tooltip=tooltip_list[6], do_not_clear=True), 
        sg.Button('Edit', key='-W_EDIT_R-', size=(5,1), pad=(10,0))],
        
        [sg.T('Area (A): '), 
        sg.Input(key='-W_A-', size=(15,1), pad=((92,5),(0,0)), tooltip=tooltip_list[7], do_not_clear=True), 
        sg.Button('Edit', key='-W_EDIT_A-', size=(5,1), pad=(9,0))],
        
        [sg.T('X-Moment of Inertia (Jx): '), 
        sg.Input(key='-W_JX-', size=(15,1), pad=((4,5),(5,5)), tooltip=tooltip_list[8], do_not_clear=True), 
        sg.Button('Edit', key='-W_EDIT_JX-', size=(5,1), pad=(9,0))],
        
        [sg.T('Y-Moment of Inertia (Jy): '), 
        sg.Input(key='-W_JY-', size=(15,1), pad=((2,5),(5,5)), tooltip=tooltip_list[9], do_not_clear=True), 
        sg.Button('Edit', key='-W_EDIT_JY-', size=(5,1), pad=(9,0))],
        
        [sg.T('X-Radius of Gyration: '), 
        sg.Input(key='-W_IX-', size=(15,1), pad=((22,5),(5,5)), tooltip=tooltip_list[10], do_not_clear=True), 
        sg.Button('Edit', key='-W_EDIT_IX-', size=(5,1), pad=(9,0))],
        
        [sg.T('Y-Radius of Gyration: '), 
        sg.Input(key='-W_IY-', size=(15,1), pad=((19,5),(5,5)), tooltip=tooltip_list[11], do_not_clear=True), 
        sg.Button('Edit', key='-W_EDIT_IY-', size=(5,1), pad=(10,0))],
        
        [sg.T('X-Section Modulii (Zx): '), 
        sg.Input(key='-W_ZX-', size=(15,1), pad=((13,5),(5,5)), tooltip=tooltip_list[12], do_not_clear=True), 
        sg.Button('Edit', key='-W_EDIT_ZX-', size=(5,1), pad=(10,0))],
        
        [sg.T('Y-Section Modulii (Zy): '), 
        sg.Input(key='-W_ZY-', size=(15,1), pad=((11,5),(5,5)), tooltip=tooltip_list[13], do_not_clear=True), 
        sg.Button('Edit', key='-W_EDIT_ZY-', size=(5,1), pad=(10,0))],
    ]

    # Table Layout
    steel_data_array = sb.retrieve_w_profile()
    w_headings = ['section_name', 'weight', 'H', 'B', 't_f', 't_w', 'r', 'A', 'J_x', 'J_y', 'I_x', 'I_y', 'Z_x', 'Z_y']
    layout_3 = [
        [sg.Table(
                values = steel_data_array,
                headings = w_headings,
                auto_size_columns=False,
                justification = 'center',
                num_rows = 25,
                key='-W_TABLE-',
                tooltip='W Profile Table',
                col_widths=[12, 7, 6, 6, 6, 6, 6, 6, 8, 8, 5, 5, 6, 6],
                size = (70, 70),
                vertical_scroll_only=False,
                font = 'Default 9',
                pad=((5,0), (15,0))
            )],
    ]
    
    layout = [
        [
            sg.Column(layout_1),
            sg.Column(layout_2),
            sg.Column(layout_3),
        ]
    ]

    return layout

'''
#* ---------------------Fourth Section: L Section Layout --------------------------------------------------------
#  TODO:
#* Note: Working Smoothly
#? Question: 
#! Error: 
#* ---------------------------------------------------------------------------------------------------------
'''
def make_l_layout():
    
    action_layout = [
        [sg.Button('Refresh', key='-L_REFRESH-', size=(15,1))],
        [sg.Button('Submit Profile', key='-L_SUBMIT-', size=(15,1))],
        [sg.Button('Delete by Name', key='-L_DELETE-', size=(15,1))],
        [sg.Button('Clear Window', key='-L_CLEAR-', size=(15,1))],
        [sg.Button('Exit', key='-L_EXIT-', size=(15,1))],
    ]
    
    action_frame =[sg.Frame(
        'Action',
        action_layout,
        element_justification = 'center',
        key='-L_ACTION-',
    )]
    
    # Index + Action layout
    themes = sg.theme_list()
    
    # Index and action column
    layout_1 = [
        [sg.T('L Profile Index', font='Arial 12')],
        [sg.Image(
            source=load_img(l_path),
            size = (190, 220),
            tooltip='L Profile Image Index'
        )],
        [sg.T('Choose Theme: '),
         sg.Combo(
             themes,
             key = '-L_THEME-',
             size = (12,1),
             enable_events=True,
         )
         ],
        action_frame,
    ]
    
    tooltip_list = [
        'Enter Section name: (Ex: L 40x40x3)',
        'Enter Profile Height (H) (Ex: 40 mm)',
        'Enter Profile Width (B) (Ex: 40 mm)',
        'Enter Profile Thickness (Ex: 3 mm)',
        'Enter Profile Radius (Ex: 2 mm)',
        'Enter End Radius (Ex: 1 mm)',
        'Enter Area (Ex: 100 cm^2)',
        'Enter weight (Ex: 1.82 kgf/m)',
        'Enter x dir. central point (Ex: 0.48 cm)',
        'Enter Central Point (Ex: 1.06 cm)',
        'Enter y dir. central point (Ex: 0.5 cm)',
        'Enter Inertia (x-dir) Ex: (0.15 cm^4)',
        'Enter Inertia (y-dir) Ex: (0.5 cm^4)',
    ]
    
    # Data Input Layout
    name = sb.get_l_name_cb()
    cb_value = [item for sublist in name for item in sublist]
    
    layout_2 = [
        [sg.T('Quick Edit: ', pad=((5,5),(20,10))),
         sg.Combo(
             values = cb_value,
             enable_events=True,
             size=(25, 1),
             key= '-L_CB_LPROFILE-',
             tooltip='Select Profile',
             pad = ((5,5),(20,10)),
         )],
        
        [sg.T('Section Name:'),
         sg.Input(key='-L_SECTION_NAME-', size=(15,1), pad=((60,5),(5,5)), tooltip=tooltip_list[0], do_not_clear=True),
         sg.Button('Edit', key='-L_EDIT_NAME-', size=(5,1), pad=(9,0))],
        
        [sg.T('Height:'),
         sg.Input(key='-L_HEIGHT-', size=(15,1), pad=((105,5),(5,5)), tooltip=tooltip_list[1], do_not_clear=True),
         sg.Button('Edit', key='-L_EDIT_HEIGHT-', size=(5,1), pad=(9,0))],
        
        [sg.T('Width:'),
         sg.Input(key='-L_WIDTH-', size=(15,1), pad=((107,5),(5,5)), tooltip=tooltip_list[2], do_not_clear=True),
         sg.Button('Edit', key='-L_EDIT_WIDTH-', size=(5,1), pad=(9,0))
         ],
        
        [sg.T('Thickness:'),
         sg.Input(key='-L_T-', size=(15,1), pad=((82,5),(5,5)), tooltip=tooltip_list[3], do_not_clear=True),
         sg.Button('Edit', key='-L_EDIT_T-', size=(5,1), pad=(9,0))],
        
        [sg.T('Radius (R):'),
         sg.Input(key='-L_R-', size=(15,1), pad=((80,5),(5,5)), tooltip=tooltip_list[4], do_not_clear=True),
         sg.Button('Edit', key='-L_EDIT_R-', size=(5,1), pad=(9,0))],
        
        [sg.T('End Radius (R_end):'),
         sg.Input(key='-L_R_END-', size=(15,1), pad=((24,5),(5,5)), tooltip=tooltip_list[5], do_not_clear=True),
         sg.Button('Edit', key='-L_EDIT_R_END-', size=(5,1), pad=(9,0))],
        
        [sg.T('Area (A):'),
         sg.Input(key='-L_A-', size=(15,1), pad=((92,5),(5,5)), tooltip=tooltip_list[6], do_not_clear=True),
         sg.Button('Edit', key='-L_EDIT_A-', size=(5,1), pad=(9,0))],
        
        [sg.T('Weight:'),
         sg.Input(key='-L_WEIGHT-', size=(15,1), pad=((99,5),(5,5)), tooltip=tooltip_list[7], do_not_clear=True),
         sg.Button('Edit', key='-L_EDIT_WEIGHT-', size=(5,1), pad=(9,0))],
        
        [sg.T('X central point (e):'),
         sg.Input(key='-L_E-', size=(15,1), pad=((39,5),(5,5)), tooltip=tooltip_list[8], do_not_clear=True),
         sg.Button('Edit', key='-L_EDIT_E-', size=(5,1), pad=(9,0))],
        
        [sg.T('Central Point (w):'),
         sg.Input(key='-L_W-', size=(15,1), pad=((44,5),(5,5)), tooltip=tooltip_list[9], do_not_clear=True),
         sg.Button('Edit', key='-L_EDIT_W-', size=(5,1), pad=(9,0))],
        
        [sg.T('Y central point (v):'),
         sg.Input(key='-L_V-', size=(15,1), pad=((39,5),(5,5)), tooltip=tooltip_list[10], do_not_clear=True),
         sg.Button('Edit', key='-L_EDIT_V-', size=(5,1), pad=(9,0))],
        
        [sg.T('X-Moment of Inertia (Ix):'),
         sg.Input(key='-L_IX-', size=(15,1), pad=((7,5),(5,5)), tooltip=tooltip_list[11], do_not_clear=True), 
         sg.Button('Edit', key='-L_EDIT_IX-', size=(5,1), pad=(9,0))],
        
        [sg.T('Y-Moment of Inertia (Iy):'),
         sg.Input(key='-L_IY-', size=(15,1), pad=((5,5),(5,5)), tooltip=tooltip_list[12], do_not_clear=True), 
         sg.Button('Edit', key='-L_EDIT_IY-', size=(5,1), pad=(9,0))],
    ]
    
    # Table Layout
    steel_data_array = sb.retrieve_l_profile()
    l_headings = ['section_name', 'H', 'B', 't', 'r', 'r_end', 'A', 'weight', 'e', 'w', 'v', 'I_x', 'I_y']
    layout_3 = [
        [sg.Table(
                values = steel_data_array,
                headings= l_headings,
                auto_size_columns=False,
                justification='center',
                num_rows=25,
                key='-L_TABLE-',
                tooltip='L profile Table',
                col_widths=[12, 7, 7, 6, 6, 7, 8, 8, 6, 6, 6, 10, 10],
                size = (70,70),
                vertical_scroll_only=False,
                font = 'Default 9',
                pad = ((5,0), (15,0))
            )],
    ]
    
    
    layout = [
        [
            sg.Column(layout_1),
            sg.Column(layout_2),
            sg.Column(layout_3),
        ]
    ]
    return layout

'''
#* ---------------------Fifth Section: C Section Layout --------------------------------------------------------
#  TODO: Complete this one
#* Note: 
#? Question: 
#! Error: 
#* -------------------------------------------------------------------------------------------------------------
'''
def make_c_layout():
    
    action_layout = [
        [sg.Button('Refresh', key='-C_REFRESH-', size=(15,1))],
        [sg.Button('Submit Profile', key='-C_SUBMIT-', size=(15,1))],
        [sg.Button('Delete by Name', key='-C_DELETE-', size=(15,1))],
        [sg.Button('Clear Window', key='-C_CLEAR-', size=(15,1))],
        [sg.Button('Exit', key='-C_EXIT-', size=(15,1))],
    ]
    
    action_frame =[sg.Frame(
        'Action',
        action_layout,
        element_justification = 'center',
        key='-C_ACTION-',
    )]
    
    # Index + Action layout
    themes = sg.theme_list()
    
    # Index and action column
    layout_1 = [
        [sg.T('L Profile Index', font='Arial 12')],
        [sg.Image(
            source=load_img(c_path),
            size = (190, 220),
            tooltip='C Profile Image Index'
        )],
        [sg.T('Choose Theme: '),
         sg.Combo(
             themes,
             key = '-C_THEME-',
             size = (12,1),
             enable_events=True,
         )
         ],
        action_frame,
    ]
    
    tooltip_list = [
        'Enter Section Name: (Ex: C 75x40x5x7)',
        'Enter Height : (Ex: 30 cm)',
        'Enter Width : (Ex: 40 cm)',
        'Enter Web Thickness: (Ex: 5 mm)',
        'Enter Flange Thickness: (Ex: 3 mm)',
        'Enter Profile Area: (Ex: 8.92 cm^2)',
        'Enter Weight: (Ex:6.92 kgf/m)',
        'Enter centroid: (Ex: 1.27 cm)',
        'Enter X dir Inertia: (Ex: 75.9 cm^4)',
        'Enter Y dir Inertia: (Ex: 12.4 cm^4)',
        'Enter X dir modulii: (Ex: 20.2 cm^3)',
        'Enter Y dir modulii: (Ex: 4.54 cm^3)'
    ]
    
    name = sb.get_c_name_cb()
    cb_value = [item for sublist in name for item in sublist]

    layout_2 = [
        [sg.T('Quick Edit: ', pad=((5,5),(20,10))),
         sg.Combo(
             values = cb_value,
             enable_events=True,
             size=(25, 1),
             key= '-C_CB_CPROFILE-',
             tooltip='Select Profile',
             pad = ((5,5),(20,10)),
         )],
        
        [sg.T('Section Name:'),
         sg.Input(key='-C_SECTION_NAME-', size=(15,1), pad=((60,5),(5,5)), tooltip=tooltip_list[0], do_not_clear=True),
         sg.Button('Edit', key='-C_EDIT_NAME-', size=(5,1), pad=(9,0))],
        
        [sg.T('Height:'),
         sg.Input(key='-C_HEIGHT-', size=(15,1), pad=((105,5),(5,5)), tooltip=tooltip_list[1], do_not_clear=True),
         sg.Button('Edit', key='-C_EDIT_HEIGHT-', size=(5,1), pad=(9,0))],
        
        [sg.T('Width:'),
         sg.Input(key='-C_WIDTH-', size=(15,1), pad=((107,5),(5,5)), tooltip=tooltip_list[2], do_not_clear=True),
         sg.Button('Edit', key='-C_EDIT_WIDTH-', size=(5,1), pad=(9,0))
         ],
        
        [sg.T('Web Thickness (tw): '), 
         sg.Input(key='-C_TW-', size=(15,1), pad=((22,5),(5,5)), tooltip=tooltip_list[3], do_not_clear=True), 
         sg.Button('Edit', key='-C_EDIT_TW-', size=(5,1), pad=(9,0))],
        
        [sg.T('Flange Thickness (tf): '), 
         sg.Input(key='-C_TF-', size=(15,1), pad=((16,5),(5,5)), tooltip=tooltip_list[4], do_not_clear=True), 
         sg.Button('Edit', key='-C_EDIT_TF-', size=(5,1), pad=(9,0))],
        
        [sg.T('Area (A):'),
         sg.Input(key='-C_A-', size=(15,1), pad=((93,5),(5,5)), tooltip=tooltip_list[5], do_not_clear=True),
         sg.Button('Edit', key='-C_EDIT_A-', size=(5,1), pad=(9,0))],
        
        [sg.T('weight:'),
         sg.Input(key='-C_WEIGHT-', size=(15,1), pad=((104,5),(5,5)), tooltip=tooltip_list[6], do_not_clear=True),
         sg.Button('Edit', key='-C_EDIT_WEIGHT-', size=(5,1), pad=(9,0))],
        
        [sg.T('Centroid (yc): '),
         sg.Input(key='-C_Y_C-', size=(15,1), pad=((63,5),(5,5)), tooltip=tooltip_list[7], do_not_clear=True),
         sg.Button('Edit', key='-C_EDIT_Y_C-', size=(5,1), pad=(9,0))],
        
        [sg.T('X-Moment of Inertia (Ix): '), 
        sg.Input(key='-C_IX-', size=(15,1), pad=((4,5),(5,5)), tooltip=tooltip_list[8], do_not_clear=True), 
        sg.Button('Edit', key='-C_EDIT_IX-', size=(5,1), pad=(9,0))],
        
        [sg.T('Y-Moment of Inertia (Iy): '), 
        sg.Input(key='-C_IY-', size=(15,1), pad=((2,5),(5,5)), tooltip=tooltip_list[9], do_not_clear=True), 
        sg.Button('Edit', key='-C_EDIT_IY-', size=(5,1), pad=(9,0))],
        
        [sg.T('X-Section Modulii (Zx): '), 
        sg.Input(key='-C_ZX-', size=(15,1), pad=((10,5),(5,5)), tooltip=tooltip_list[10], do_not_clear=True), 
        sg.Button('Edit', key='-C_EDIT_ZX-', size=(5,1), pad=(10,0))],
        
        [sg.T('Y-Section Modulii (Zy): '), 
        sg.Input(key='-C_ZY-', size=(15,1), pad=((8,5),(5,5)), tooltip=tooltip_list[11], do_not_clear=True), 
        sg.Button('Edit', key='-C_EDIT_ZY-', size=(5,1), pad=(10,0))],
        
    ]
    
    steel_data_array = sb.retrieve_c_profile()
    c_headings = ['section_name', 'H', 'B', 't_w', 't_f', 'A', 'weight', 'y_c', 'I_x', 'I_y', 'Z_x', 'Z_y']
    layout_3 = [
         [sg.Table(
                values = steel_data_array,
                headings = c_headings,
                auto_size_columns=False,
                justification = 'center',
                num_rows = 25,
                key='-C_TABLE-',
                tooltip='C Profile Table',
                col_widths=[12, 7, 7, 7, 7, 8, 8, 7, 7, 9, 10, 10],
                size = (70, 70),
                vertical_scroll_only=False,
                font = 'Default 9',
                pad=((5,0), (15,0))
            )],
    ]
    
    layout = [
        [
            sg.Column(layout_1),
            sg.Column(layout_2),
            sg.Column(layout_3),
        ]
    ]
    return layout


#* Window Layout
def make_window():
    sg.set_options(font='Default 10') #Default font
    # Action Layout (Frame)
    tab_1 = make_w_layout()
    tab_2 = make_l_layout()
    tab_3 = make_c_layout()
    
    layout = [
        [sg.TabGroup([
            [sg.Tab('W profile', tab_1)],
            [sg.Tab('L profile', tab_2)],
            [sg.Tab('C profile', tab_3)],
        ]
        )]
    ]
    window = sg.Window('Profile editor 1.0', layout, resizable=True, finalize=False)
    return window


def main_window():
    sg.theme('LightGrey1')  #Default theme
    window = make_window()  #Calling the window method()
    # Event handling
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, '-W_EXIT-', '-L_EXIT-', '-C_EXIT-'):
            break
        
        # TODO This would be meddled in later on 
        elif event in ('-W_THEME-', '-L_THEME-', '-C_THEME-'):
            window.close()
            if values['-W_THEME-']:
                sg.theme(values['-W_THEME-'])
                window = make_window()
            if values['-L_THEME-']:
                sg.theme(values['-L_THEME-'])
                window = make_window()
            if values['-C_THEME-']:
                sg.theme(values['-C_THEME-'])
                window = make_window()

        # TODO This would be meddled in later
        elif event == '-W_REFRESH-':
            window.refresh()
            new_name = sb.get_w_name_cb()
            cb_value = [item for sublist in new_name for item in sublist]
            # print(cb_value)
            values['-W_CB_WPROFILE-'] = cb_value
            window.refresh()
            window['-W_CB_WPROFILE-'].update(values = cb_value)

        #* Submit Event
        elif event == '-W_SUBMIT-':
            validation_result = sb.w_validate(values)
            try:
                if validation_result["is_valid"]:
                    sb.insert_w_data(values['-W_SECTION_NAME-'],
                                    values['-W_WEIGHT-'],
                                    values['-W_HEIGHT-'],
                                    values['-W_WIDTH-'],
                                    values['-W_TF-'],
                                    values['-W_TW-'],
                                    values['-W_R-'],
                                    values['-W_A-'],
                                    values['-W_JX-'],
                                    values['-W_JY-'],
                                    values['-W_IX-'],
                                    values['-W_IY-'],
                                    values['-W_ZX-'],
                                    values['-W_ZY-']
                                    )
                    sb.w_update_table_data(window)
                    sg.popup(f"{values['-W_SECTION_NAME-']} data has been sucessfully inserted")

                else:
                    error_msg = sb.pop_error_msg(validation_result["values_invalid"])
                    sg.popup(error_msg)
            except sqlite3.IntegrityError:
                sg.popup_error(f"A section with name '{values['-W_SECTION_NAME-']}' already exists.")
            finally:
                new_name = sb.get_w_name_cb()
                cb_value = [item for sublist in new_name for item in sublist]
                values['-W_CB_WPROFILE-'] = cb_value
                window['-W_CB_WPROFILE-'].update(values = cb_value) 
              
        elif event == '-L_SUBMIT-':
            validation_result = sb.l_validate(values)
            try:
                if validation_result["is_valid"]:
                    sb.insert_l_data(values['-L_SECTION_NAME-'],
                                    values['-L_HEIGHT-'],
                                    values['-L_WIDTH-'],
                                    values['-L_T-'],
                                    values['-L_R-'],
                                    values['-L_R_END-'],
                                    values['-L_A-'],
                                    values['-L_WEIGHT-'],
                                    values['-L_E-'],
                                    values['-L_W-'],
                                    values['-L_V-'],
                                    values['-L_IX-'],
                                    values['-L_IY-']
                                    )
                    sb.l_update_table_data(window)
                    sg.popup(f"{values['-L_SECTION_NAME-']} data has been sucessfully inserted")

                else:
                    error_msg = sb.pop_error_msg(validation_result["values_invalid"])
                    sg.popup(error_msg)
            except sqlite3.IntegrityError:
                sg.popup_error(f"A section with name '{values['-L_SECTION_NAME-']}' already exists.")
            finally:
                new_name = sb.get_l_name_cb()
                cb_value = [item for sublist in new_name for item in sublist]
                values['-L_CB_LPROFILE-'] = cb_value
                window['-L_CB_LPROFILE-'].update(values = cb_value) 
        
        elif event == '-C_SUBMIT-':
            validation_result = sb.c_validate(values)
            try:
                if validation_result["is_valid"]:
                    sb.insert_c_data(values['-C_SECTION_NAME-'],
                                     values['-C_HEIGHT-'],
                                     values['-C_WIDTH-'],
                                     values['-C_TW-'],
                                     values['-C_TF-'],
                                     values['-C_A-'],
                                     values['-C_WEIGHT-'],
                                     values['-C_Y_C-'],
                                     values['-C_IX-'],
                                     values['-C_IY-'],
                                     values['-C_ZX-'],
                                     values['-C_ZY-'] 
                                            )
                    sb.c_update_table_data(window)
                    sg.popup(f"{values['-C_SECTION_NAME-']} data has been sucessfully inserted")
                else:
                    error_msg = sb.pop_error_msg(validation_result['values_invalid'])
                    sg.popup(error_msg)
            except sqlite3.IntegrityError:
                sg.popup(f"A section with name '{values['-C_SECTION_NAME-']}' already exists.")
            finally:
                new_name = sb.get_c_name_cb()
                cb_value = [item for sublist in new_name for item in sublist]
                values['-C_CB_CPROFILE-'] = cb_value
                window['-C_CB_CPROFILE-'].update(values = cb_value)
        
        #* Clear Event
        if event in ('-W_CLEAR-', '-L_CLEAR-', '-C_CLEAR-'):
            prefix = event[1]
            for key in values.keys():
                if len(str(key)) >= 2 and key[1] == prefix and isinstance(window[key], sg.Input):
                    window[key].update('')
                  
        # elif event == '-W_CLEAR-':
        #     for key in values.keys():
        #         if len(str(key)) >= 2 and str(key)[1]=='W' and isinstance(window[key], sg.Input):
        #             window[key].update('')

        # elif event == '-L_CLEAR-':
        #     for key in values.keys():
        #         if len(str(key)) >= 2 and str(key)[1]=='L' and isinstance(window[key], sg.Input):
        #             window[key].update('')

        # elif event == '-C_CLEAR-':
        #     for key in values.keys():
        #         if len(str(key)) >= 2 and str(key)[1]=='C' and isinstance(window[key], sg.Input):
        #             window[key].update('')

        elif event == '-W_CB_WPROFILE-':
            data = sb.fill_input_wdata(str(values['-W_CB_WPROFILE-']))
            input_list = ['-W_SECTION_NAME-', '-W_WEIGHT-', '-W_HEIGHT-', 
                        '-W_WIDTH-', '-W_TF-', '-W_TW-', 
                        '-W_R-', '-W_A-', '-W_JX-', 
                        '-W_JY-', '-W_IX-', '-W_IY-', 
                        '-W_ZX-', '-W_ZY-']

            for i,j in enumerate(input_list):
                window[j].update(data[0][i])
        
        elif event == '-L_CB_LPROFILE-':
            data = sb.fill_input_ldata(str(values['-L_CB_LPROFILE-']))
            input_list = ['-L_SECTION_NAME-', '-L_HEIGHT-', '-L_WIDTH-',
                          '-L_T-', '-L_R-', '-L_R_END-', '-L_A-',
                          '-L_WEIGHT-', '-L_E-', '-L_W-', '-L_V-',
                          '-L_IX-', '-L_IY-']
            
            for i, j in enumerate(input_list):
                window[j].update(data[0][i])
        
        elif event == '-C_CB_CPROFILE-':
            data = sb.fill_input_cdata(str(values['-C_CB_CPROFILE-']))
            input_list = [
                '-C_SECTION_NAME-', '-C_HEIGHT-', '-C_WIDTH-',
                '-C_TW-', '-C_TF-', '-C_A-', '-C_WEIGHT-', '-C_Y_C-', 
                 '-C_IX-', '-C_IY-', '-C_ZX-', '-C_ZY-'
            ]
            # print(data) #[['C DEMO', 12.0, 412.0, 41.0, 41.0, 411.0, 12.0, 15.0, 12.0, 512.0, 125.0, 125.0]]
            for i, j in enumerate(input_list):
                window[j].update(data[0][i])
        
        #* ------------------------------------------------------------------------------------------------------------------             
        #* W Elif Event for Changing Props
        #* ------------------------------------------------------------------------------------------------------------------ 
        elif event == '-W_EDIT_NAME-':
            old_section_name = values['-W_SECTION_NAME-']
            new_section_name = sg.popup_get_text('Enter new name for the profile:', default_text=values['-W_SECTION_NAME-'])
            sb.edit_name('w_data', old_section_name, new_section_name)
            values['-W_SECTION_NAME-'] = new_section_name  # Update the values dictionary
            window['-W_SECTION_NAME-'].update(new_section_name)  # Update the input element in the window
            sb.w_update_table_data(window)
            sg.popup(f"{new_section_name} is the profile name")
            window.refresh()
            
        elif event == '-W_EDIT_WEIGHT-':
            section_name = values['-W_SECTION_NAME-']
            weight = sg.popup_get_text('Enter new weight:', default_text=values['-W_WEIGHT-'])
            if weight is not None:
                sb.edit_weight_by_name('w_data', section_name, weight)
                values['-W_WEIGHT-'] = weight # Update the values dictionary
                window['-W_WEIGHT-'].update(weight) # Update the input element in the window
                sb.w_update_table_data(window)
                sg.popup(f"Weight has sucessfully been updated")
    
        elif event == '-W_EDIT_HEIGHT-':
            section_name = values['-W_SECTION_NAME-']
            height = sg.popup_get_text('Enter new height:', default_text=values['-W_HEIGHT-'])
            if height is not None:
                sb.edit_H_by_name('w_data', section_name, height)
                values['-W_HEIGHT-'] = height # Update the values dictionary
                window['-W_HEIGHT-'].update(height) # Update the input element in the window
                sb.w_update_table_data(window)
                sg.popup(f"Height has sucessfully been updated")

        elif event == '-W_EDIT_WIDTH-':
            section_name = values['-W_SECTION_NAME-']
            width = sg.popup_get_text('Enter new width:', default_text=values['-W_WIDTH-'])
            if width is not None:
                sb.edit_B_by_name('w_data', section_name, width)
                values['-W_WIDTH-'] = width # Update the values dictionary
                window['-W_WIDTH-'].update(width) # Update the input element in the window
                sb.w_update_table_data(window)
                sg.popup(f"Width has sucessfully been updated")

        elif event == '-W_EDIT_TF-':
            section_name = values['-W_SECTION_NAME-']
            t_f = sg.popup_get_text('Enter new flange thickness:', default_text=values['-W_TF-'])
            if t_f is not None:
                sb.edit_tf_by_name('w_data', section_name, t_f)
                values['-W_TF-'] = t_f # Update the values dictionary
                window['-W_TF-'].update(t_f) # Update the input element in the window
                sb.w_update_table_data(window)
                sg.popup(f"Flange Thickness has sucessfuly been updated")

        elif event == '-W_EDIT_TW-':
            section_name = values['-W_SECTION_NAME-']
            t_w = sg.popup_get_text('Enter new flange thickness:', default_text=values['-W_TW-'])
            if t_w is not None:
                sb.edit_tw_by_name('w_data', section_name, t_f)
                values['-W_TW-'] = t_w # Update the values dictionary
                window['-W_TW-'].update(t_w) # Update the input element in the window
                sb.w_update_table_data(window)
                sg.popup(f"Web Thickness has sucessfuly been updated")

        elif event == '-W_EDIT_R-':
            section_name = values['-W_SECTION_NAME-']
            r = sg.popup_get_text('Enter new radius:', default_text=values['-W_R-'])
            if r is not None:
                sb.edit_r_by_name('w_data', section_name, r)
                values['-W_R-'] = r # Update the values dictionary
                window['-W_R-'].update(r) # Update the input element in the window
                sb.w_update_table_data(window)
                sg.popup(f"Radius has sucessfuly been updated")

        elif event == '-W_EDIT_A-':
            section_name = values['-W_SECTION_NAME-']
            Area = sg.popup_get_text('Enter new area:', default_text=values['-W_A-'])
            if Area is not None:
                sb.edit_A_by_name('w_data', section_name, Area)
                values['-W_A-'] = Area # Update the values dictionary
                window['-W_A-'].update(Area) # Update the input element in the window
                sb.w_update_table_data(window)
                sg.popup(f"Area has sucessfuly been updated") 
            
        elif event == '-W_EDIT_JX-':
            section_name = values['-W_SECTION_NAME-']
            J_x = sg.popup_get_text('Enter new x-moment of inertia:', default_text=values['-W_JX-'])
            if J_x is not None:
                sb.edit_Jx_by_name('w_data', section_name, J_x)
                values['-W_JX-'] = J_x # Update the values dictionary
                window['-W_JX-'].update(J_x) # Update the input element in the window
                sb.w_update_table_data(window)
                sg.popup(f"Moment of inertia (x) has sucessfuly been updated") 
            
        elif event == '-W_EDIT_JY-':
            section_name = values['-W_SECTION_NAME-']
            J_y = sg.popup_get_text('Enter new y-moment of inertia:', default_text=values['-W_JY-'])
            if J_y is not None:
                sb.edit_Jy_by_name('w_data', section_name, J_y)
                values['-W_JY-'] = J_y # Update the values dictionary
                window['-W_JY-'].update(J_y) # Update the input element in the window
                sb.w_update_table_data(window)
                sg.popup(f"Moment of inertia (y) has sucessfuly been updated") 

        elif event == '-W_EDIT_IX-':
            section_name = values['-W_SECTION_NAME-']
            I_x = sg.popup_get_text('Enter new x- gyration radius:', default_text=values['-W_IX-'])
            if I_x is not None:
                sb.edit_Ix_by_name('w_data', section_name, I_x)
                values['-W_IX-'] = I_x # Update the values dictionary
                window['-W_IX-'].update(I_x) # Update the input element in the window
                sb.w_update_table_data(window)
                sg.popup(f"Gyration radius (x) has sucessfuly been updated") 
        
        elif event == '-W_EDIT_IY-':
            section_name = values['-W_SECTION_NAME-']
            I_y = sg.popup_get_text('Enter new y- gyration radius:', default_text=values['-W_IY-'])
            if I_y is not None:
                sb.edit_Iy_by_name('w_data', section_name, I_y)
                values['-W_IY-'] = I_y # Update the values dictionary
                window['-W_IY-'].update(I_y) # Update the input element in the window
                sb.w_update_table_data(window)
                sg.popup(f"Gyration radius (y) has sucessfuly been updated") 
        
        elif event == '-W_EDIT_ZX-':
            section_name = values['-W_SECTION_NAME-']
            Z_x = sg.popup_get_text('Enter new x-modulii:', default_text=values['-W_ZX-'])
            if Z_x is not None:
                sb.edit_Zx_by_name('w_data', section_name, Z_x)
                values['-W_ZX-'] = Z_x # Update the values dictionary
                window['-W_ZX-'].update(Z_x) # Update the input element in the window
                sb.w_update_table_data(window)
                sg.popup(f"Section Modulii (x) has sucessfuly been updated") 
        
        elif event == '-W_EDIT_ZY-':
            section_name = values['-W_SECTION_NAME-']
            Z_y = sg.popup_get_text('Enter new y-modulii:', default_text=values['-W_ZY-'])
            if Z_y is not None:
                sb.edit_Zy_by_name('w_data', section_name, Z_y)
                values['-W_ZY-'] = Z_y # Update the values dictionary
                window['-W_ZY-'].update(Z_y) # Update the input element in the window
                sb.w_update_table_data(window)
                sg.popup(f"Section Modulii (y) has sucessfuly been updated") 
        
        #* ------------------------------------------------------------------------------------------------------------------             
        #* L Elif Event for Changing Props
        #* ------------------------------------------------------------------------------------------------------------------ 
        elif event == '-L_EDIT_NAME-':
            section_name = values['-L_SECTION_NAME-']
            new_name = sg.popup_get_text('Enter new name:', default_text=values['-L_SECTION_NAME-'])
            if new_name is not None:
                sb.edit_name('l_data', section_name, new_name)
                values['-L_SECTION_NAME-'] = new_name # Update the values dictionary
                window['-L_SECTION_NAME-'].update(new_name) # Update the input element in the window
                sb.l_update_table_data(window)
                sg.popup(f"L Section Name has been Updated") 
            #* Update list content
            new_name = sb.get_l_name_cb()
            cb_value = [item for sublist in new_name for item in sublist]
            values['-L_CB_LPROFILE-'] = cb_value
            window['-L_CB_LPROFILE-'].update(values = cb_value) 
        
        elif event == '-L_EDIT_HEIGHT-':
            section_name = values['-L_SECTION_NAME-']
            height = sg.popup_get_text('Enter new height:', default_text=values['-L_HEIGHT-'])
            if height is not None:
                sb.edit_H_by_name('l_data', section_name, height)
                values['-L_HEIGHT-'] = height # Update the values dictionary
                window['-L_HEIGHT-'].update(height) # Update the input element in the window
                sb.l_update_table_data(window)
                sg.popup(f"Height has sucessfully been updated")

        elif event == '-L_EDIT_WIDTH-':
            section_name = values['-L_SECTION_NAME-']
            width = sg.popup_get_text('Enter new width:', default_text=values['-L_WIDTH-'])
            if width is not None:
                sb.edit_B_by_name('l_data', section_name, width)
                values['-L_WIDTH-'] = width # Update the values dictionary
                window['-L_WIDTH-'].update(width) # Update the input element in the window
                sb.l_update_table_data(window)
                sg.popup(f"Width has sucessfully been updated")

        elif event  == '-L_EDIT_T-':
            section_name = values['-L_SECTION_NAME-']
            new_t = sg.popup_get_text('Enter Thickness:', default_text=values['-L_T-'])
            if new_t is not None:
                sb.edit_t_by_name('l_data', section_name, new_t)
                values['-L_T-'] = new_t # Update the values dictionary
                window['-L_T-'].update(new_t) # Update the input element in the window
                sb.l_update_table_data(window)
                sg.popup(f"Thickness of {values['-L_SECTION_NAME-']} has sucesfully been updated") 

        elif event == '-L_EDIT_R-':
            section_name = values['-L_SECTION_NAME-']
            new_r = sg.popup_get_text('Enter Radius:', default_text=values['-L_R-'])
            if new_r is not None:
                sb.edit_r_by_name('l_data', section_name, new_r)
                values['-L_R-'] = new_r # Update the values dictionary
                window['-L_R-'].update(new_r) # Update the input element in the window
                sb.l_update_table_data(window)
                sg.popup(f"Radius of {values['-L_SECTION_NAME-']} has sucesfully been updated") 

        elif event == '-L_EDIT_R_END-':
            section_name = values['-L_SECTION_NAME-']
            new_r_end = sg.popup_get_text('Enter End Radius:', default_text=values['-L_R_END-'])
            if new_r_end is not None:
                sb.edit_rend_by_name('l_data', section_name, new_r_end)
                values['-L_R_END-'] = new_r_end # Update the values dictionary
                window['-L_R_END-'].update(new_r_end) # Update the input element in the window
                sb.l_update_table_data(window)
                sg.popup(f"End Radius of {values['-L_SECTION_NAME-']} has sucesfully been updated")

        elif event == '-L_EDIT_A-':
            section_name = values['-L_SECTION_NAME-']
            new_A = sg.popup_get_text('Enter Area: ', default_text=values['-L_A-'])
            if new_A is not None:
                sb.edit_A_by_name('l_data', section_name, new_A)
                values['-L_A-'] = new_A
                window['-L_A-'].update(new_A)
                sb.l_update_table_data(window)
                sg.popup(f"Area of {section_name} has been updated")

        elif event == '-L_EDIT_WEIGHT-':
            section_name = values['-L_SECTION_NAME-']
            new_weight = sg.popup_get_text('Enter Weight:', default_text=values['-WEIGHT-'])
            if new_weight is not None:
                sb.edit_weight_by_name('l_data', section_name, new_weight)
                values['-L_WEIGHT-'] = new_weight
                window['-L_WEIGHT-'].update(new_weight)
                sb.l_update_table_data(window)
                sg.popup(f"Weight of {section_name} has been updated")

        elif event == '-L_EDIT_E-':
            section_name = values['-L_SECTION_NAME-']
            new_e = sg.popup_get_text('Enter X Central Point:', default_text=values['-L_E-'])
            if new_e is not None:
                sb.edit_e_by_name('l_data', section_name, new_e)
                values['-L_E-'] = new_e
                window['-L_E-'].update(new_e)
                sb.l_update_table_data(window)
                sg.popup(f"X central point of {values['-L_SECTION_NAME-']} has been updated")

        elif event == '-L_EDIT_W-':
            section_name = values['-L_SECTION_NAME-']
            new_w = sg.popup_get_text('Enter New Central Point:', default_text=values['-L_W-'])
            if new_w is not None:
                sb.edit_w_by_name('l_data', section_name, new_w)
                values['-L_W-'] = new_w
                window['-L_W-'].update(new_w)
                sb.l_update_table_data(window)
                sg.popup(f"Central Point of {values['-L_SECTION_NAME-']} has been updated")
        
        elif event == '-L_EDIT_V-':
            section_name = values['-L_SECTION_NAME-']
            new_v = sg.popup_get_text('Enter Y Central point:', default_text=values['-L_V-'])
            if new_v is not None:
                sb.edit_v_by_name('l_data', section_name, new_v)
                values['-L_V-'] = new_v
                window['-L_V-'].update(new_v)
                sb.l_update_table_data(window)
                sg.popup(f"Y central point of {section_name} has been updated")

        elif event == '-L_EDIT_IX-':
            section_name = values['-L_SECTION_NAME-']
            new_IX = sg.popup_get_text('Enter X-Inertia value:', default_text=values['-L_IX-'])
            if new_IX is not None:
                sb.edit_Ix_by_name('l_data', section_name, new_IX)
                values['-L_IX-'] = new_IX
                window['-L_IX-'].update(new_IX)
                sb.l_update_table_data(window)
                sg.popup(f"X Inertia of {section_name} has been updated")
                
        elif event == '-L_EDIT_IY-':
            section_name = values['-L_SECTION_NAME-']
            new_IY = sg.popup_get_text('Enter Y-Inertia value:', default_text=values['-L_IY-'])
            if new_IY is not None:
                sb.edit_Iy_by_name('l_data', section_name, new_IY)
                values['-L_IY-'] = new_IY
                window['-L_IY-'].update(new_IY)
                sb.l_update_table_data(window)
                sg.popup(f"Y Inertia of {section_name} has been updated")
        
        #* ------------------------------------------------------------------------------------------------------------------             
        #* C Elif Event for Changing Props
        #* ------------------------------------------------------------------------------------------------------------------ 
        elif event == '-C_EDIT_NAME-':
            section_name = values['-C_SECTION_NAME-']
            new_name = sg.popup_get_text('Enter new name:', default_text=values['-C_SECTION_NAME-'])
            if new_name is not None:
                sb.edit_name('c_data', section_name, new_name)
                values['-C_SECTION_NAME-'] = new_name # Update the values dictionary
                window['-C_SECTION_NAME-'].update(new_name) # Update the input element in the window
                sb.c_update_table_data(window)
                sg.popup(f"C Section Name has been Updated") 
            #* Update list content
            new_name = sb.get_l_name_cb()
            cb_value = [item for sublist in new_name for item in sublist]
            values['-C_CB_CPROFILE-'] = cb_value
            window['-C_CB_CPROFILE-'].update(values = cb_value) 
        
        elif event == '-C_EDIT_HEIGHT-':
            section_name = values['-C_SECTION_NAME-']
            new_height = sg.popup_get_text('Enter new height:', default_text=values['-C_HEIGHT-'])
            if new_height is not None:
                sb.edit_H_by_name('c_data', section_name, new_height)
                values['-C_HEIGHT-'] = new_height
                window['-C_HEIGHT-'].update(new_height)
                sb.c_update_table_data(window)
                sg.popup(f"Height of {section_name} has been updated")

        elif event == '-C_EDIT_WIDTH-':
            section_name = values['-C_SECTION_NAME-']
            new_width = sg.popup_get_text('Enter new height:', default_text=values['-C_WIDTH-'])
            if new_width is not None:
                sb.edit_B_by_name('c_data', section_name, new_width)
                values['-C_WIDTH-'] = new_width
                window['-C_WIDTH-'].update(new_width)
                sb.c_update_table_data(window)
                sg.popup(f"Width of {section_name} has been updated")

        elif event == '-C_EDIT_TW-':
            section_name = values['-C_SECTION_NAME-']
            new_tw = sg.popup_get_text('Enter new web thickness:', default_text=values['-C_TW-'])
            if new_tw is not None:
                sb.edit_tw_by_name('c_data', section_name, new_width)
                values['-C_TW-'] = new_tw
                window['-C_TW-'].update(new_tw)
                sb.c_update_table_data(window)
                sg.popup(f"Web Thickness of {section_name} has been updated")              
        
        elif event == '-C_EDIT_TF-':
            section_name = values['-C_SECTION_NAME-']
            new_tf = sg.popup_get_text('Enter Flange Thickness:', default_text=values['-C_TF-'])
            if new_tf is not None:
                sb.edit_tf_by_name('c_data', section_name, new_tf)
                values['-C_TF-'] = new_tf
                window['-C_TF-'].update(new_tf)
                sb.c_update_table_data(window)
                sg.popup(f"Flange thickness of {section_name} has been updated")
        
        elif event == '-C_EDIT_A-':
            section_name = values['-C_SECTION_NAME-']
            new_A = sg.popup_get_text('Enter Area:', default_text=values['-C_A-'])
            if new_A is not None:
                sb.edit_A_by_name('c_data', section_name, new_A)
                values['-C_A-'] = new_A
                window['-C_A-'].update(new_A)
                sb.c_update_table_data(window)
                sg.popup(f"Area of {section_name} has been updated")

        elif event == '-C_EDIT_WEIGHT-':
            section_name = values['-C_SECTION_NAME-']
            new_weight = sg.popup_get_text('Enter Weight:',default_text=values['-C_WEIGHT-'])
            if new_weight is not None:
                sb.edit_weight_by_name('c_data', section_name, new_weight)
                values['-C_WEIGHT-'] = new_weight
                window['-C_WEIGHT-'].update(new_weight)
                sb.c_update_table_data(window)
                sg.popup(f"Weight of {section_name} has been updated")
                
        elif event == '-C_EDIT_Y_C-':
            section_name = values['-C_SECTION_NAME-']
            new_yc = sg.popup_get_text('Enter y centroid:', default_text=values['-C_Y_C-'])
            if new_yc is not None:
                sb.edit_yc_by_name('c_data', section_name, new_yc)
                values['-C_Y_C-'] = new_yc
                window['-C_Y_C-'].update(new_yc)
                sb.c_update_table_data(window)
                sg.popup(f"Centroid of {section_name} has been updated")
        
        elif event == '-C_EDIT_IX-':
            section_name = values['-C_SECTION_NAME-']
            new_Ix = sg.popup_get_text('Enter X Inertia:', default_text=values['-C_IX-'])
            if new_Ix is not None:
                sb.edit_Ix_by_name('c_data', section_name, new_Ix)
                values['-C_IX-'] = new_Ix
                window['-C_IX-'].update(new_Ix)
                sb.c_update_table_data(window)
                sg.popup(f"X Inertia of {section_name} has been updated")
                
        elif event == '-C_EDIT_IY-':
            section_name = values['-C_SECTION_NAME-']
            new_Iy = sg.popup_get_text('Enter Y Inertia:', default_text=values['-C_IY-'])
            if new_Iy is not None:
                sb.edit_Iy_by_name('c_data', section_name, new_Iy)
                values['-C_IY-'] = new_Iy
                window['-C_IY-'].update(new_Iy)
                sb.c_update_table_data(window)
                sg.popup(f"Y Inertia of {section_name} has been updated")
        
        elif event == '-C_EDIT_ZX-':
            section_name = values['-C_SECTION_NAME-']
            new_Zx = sg.popup_get_text('Enter X Modulii:', default_text=values['-C_ZX-'])
            if new_Zx is not None:
                sb.edit_Zx_by_name('c_data', section_name, new_Zx)
                values['-C_ZX-'] = new_Zx
                window['-C_ZX-'].update(new_Zx)
                sb.c_update_table_data(window)
                sg.popup(f"X Modulii of {section_name} has been updated")
                
        elif event == '-C_EDIT_ZY-':
            section_name = values['-C_SECTION_NAME-']
            new_Zy = sg.popup_get_text('Enter Y Modulii:', default_text=values['-C_ZY-'])
            if new_Zy is not None:
                sb.edit_Zy_by_name('c_data', section_name, new_Zy)
                values['-C_ZY-'] = new_Zy
                window['-C_ZY-'].update(new_Zy)
                sb.c_update_table_data(window)
                sg.popup(f"Y Modulii of {section_name} has been updated")
        
        #* ------------------------------------------------------------------------------------------------------------------             
        #* Deletion method
        #* ------------------------------------------------------------------------------------------------------------------ 
        elif event ==  '-W_DELETE-':
            section_name = values['-W_SECTION_NAME-']
            # Define the layout of the pop-up window
            layout = [[sg.Text('Are you sure you want to delete this file?')],
                    [sg.Button('Ok', key='-OK-'), sg.Cancel()]]

            # Create the pop-up window and display it to the user
            confirm_window = sg.Window('Delete File', layout)                                          
            event, confirm_values = confirm_window.read()
            
            # Event control
            if event == '-OK-':
                sb.delete_by_name( 'w_data', section_name)
                sb.w_update_table_data(window)
                
                for key in values.keys():
                    if isinstance(window[key], sg.Input):
                        window[key].update('')
                        
                new_name = sb.get_w_name_cb()
                cb_value = [item for sublist in new_name for item in sublist]
                values['-W_CB_WPROFILE-'] = cb_value
                window['-W_CB_WPROFILE-'].update(values = cb_value) 
                sg.popup('Profile has been removed')
                confirm_window.close()
            else:
                sg.popup('Command cancelled')
                confirm_window.close()
    
        elif event ==  '-L_DELETE-':
            section_name = values['-L_SECTION_NAME-']
            # Define the layout of the pop-up window
            layout = [[sg.Text('Are you sure you want to delete this file?')],
                    [sg.Button('Ok', key='-OK-'), sg.Cancel()]]

            # Create the pop-up window and display it to the user
            confirm_window = sg.Window('Delete File', layout)                                          
            event, confirm_values = confirm_window.read()
            
            # Event control
            if event == '-OK-':
                sb.delete_by_name( 'l_data', section_name)
                sb.l_update_table_data(window)
                
                for key in values.keys():
                    if isinstance(window[key], sg.Input):
                        window[key].update('')
                        
                new_name = sb.get_l_name_cb()
                cb_value = [item for sublist in new_name for item in sublist]
                values['-L_CB_LPROFILE-'] = cb_value
                window['-L_CB_LPROFILE-'].update(values = cb_value) 
                sg.popup('Profile has been removed')
                confirm_window.close()
            else:
                sg.popup('Command cancelled')
                confirm_window.close()
    
        elif event ==  '-C_DELETE-':
            section_name = values['-C_SECTION_NAME-']
            # Define the layout of the pop-up window
            layout = [[sg.Text('Are you sure you want to delete this file?')],
                    [sg.Button('Ok', key='-OK-'), sg.Cancel()]]

            # Create the pop-up window and display it to the user
            confirm_window = sg.Window('Delete File', layout)                                          
            event, confirm_values = confirm_window.read()
            
            # Event control
            if event == '-OK-':
                sb.delete_by_name( 'c_data', section_name)
                sb.c_update_table_data(window)
                
                for key in values.keys():
                    if isinstance(window[key], sg.Input):
                        window[key].update('')
                        
                new_name = sb.get_c_name_cb()
                cb_value = [item for sublist in new_name for item in sublist]
                values['-C_CB_CPROFILE-'] = cb_value
                window['-C_CB_CPROFILE-'].update(values = cb_value) 
                sg.popup('Profile has been removed')
                confirm_window.close()
            else:
                sg.popup('Command cancelled')
                confirm_window.close()
    window.close()
    
if __name__ == '__main__':
    main_window()