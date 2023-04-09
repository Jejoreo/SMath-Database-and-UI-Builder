'''
This would be the backend of our program
'''
import sqlite3

db_path = r'C:\Users\jevon\OneDrive\Documents\God Knows What\Code Palace\Steel Profiler Project\STEEL_DB.db'

# SQLite commands
def insert_w_data(section_name, weight, H, B, t_f, t_w, r, A, J_x, J_y, I_x, I_y, Z_x, Z_y):
    values = [section_name, weight, H, B, t_f, t_w, r, A, J_x, J_y, I_x, I_y, Z_x, Z_y]
    with sqlite3.connect(db_path) as conn:
        conn.execute('''
                     INSERT INTO w_data(
                         section_name, weight, H, B, t_f, t_w, r, A, J_x, J_y, I_x, I_y, Z_x, Z_y
                     )
                     VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                     ''', values)
    conn.commit()
    conn.close()
    
def insert_c_data(section_name, H, B, t_w, t_f, A, weight, y_c, I_x, I_y, Z_x, Z_y):
    values = [section_name, H, B, t_w, t_f, A, weight, y_c, I_x, I_y, Z_x, Z_y]
    with sqlite3.connect(db_path) as conn:
        conn.execute('''
            INSERT INTO c_data(
                section_name, H, B, t_w, t_f, A, weight, y_c, I_x, I_y, Z_x, Z_y
            )
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        ''', values)
    conn.commit()
    conn.close()

def insert_l_data(section_name, H, B, t, r, r_end, A, weight, e, w, v, I_x, I_y):
    conn = sqlite3.connect(db_path)
    conn.executemany('''
                        INSERT INTO l_data(
                            section_name, 
                            H, B, t, 
                            r, r_end, A, 
                            weight, e, w, 
                            v, I_x, I_y
                        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
                     ''', [(section_name, H, B, t, r, r_end, A, weight, e, w, v, I_x, I_y)])
    conn.commit()
    conn.close()


'''
#* Getting name for combo box
#* The methods are in this section
'''
def get_w_name_cb():
    name_list = []
    conn = sqlite3.connect(db_path)
    cursor = conn.execute("SELECT section_name FROM w_data")
    for row in cursor:
        name_list.append(list(row)) # append the first element of each row (i.e., the section name)
    return name_list

def get_l_name_cb():
    name_list = []
    conn = sqlite3.connect(db_path)
    cursor = conn.execute("SELECT section_name FROM l_data")
    for row in cursor:
        name_list.append(list(row))
    return name_list

def get_c_name_cb():
    name_list = []
    conn = sqlite3.connect(db_path)
    cursor = conn.execute("SELECT section_name FROM c_data")
    for row in cursor:
        name_list.append(list(row))
    return name_list
'''
#* Getting name for combo box
#* The methods are in this section
'''
def fill_input_wdata(name):
    results = []
    conn = sqlite3.connect(db_path)
    cursor = conn.execute('''SELECT section_name, weight, H, 
                          B, t_f, t_w, r, A, J_x, J_y, I_x, 
                          I_y, Z_x, Z_y FROM w_data WHERE section_name = ?''', (name,))
    
    for row in cursor:
        results.append(list(row))
    return results

def fill_input_ldata(name):
    results = []
    conn = sqlite3.connect(db_path)
    cursor = conn.execute('''SELECT section_name, H, B, 
                          t, r, r_end, A, weight, e, w, v, 
                          I_x, I_y FROM l_data WHERE section_name = ?''', (name,))

    for row in cursor:
        results.append(list(row))
    return results

def fill_input_cdata(name):
    results = []
    conn = sqlite3.connect(db_path)
    cursor = conn.execute('''SELECT section_name, H, B,
                          t_w, t_f, A, weight, y_c, I_x, I_y, 
                          Z_x, Z_y FROM c_data WHERE section_name = ?''', (name,))

    for row in cursor:
        results.append(list(row))
    return results

#* Retrieve would be for table ??
def retrieve_w_profile():
    results = []
    conn = sqlite3.connect(db_path)
    cursor = conn.execute('''SELECT section_name, weight, H, 
                          B, t_f, t_w, r, A, J_x, J_y, I_x, 
                          I_y, Z_x, Z_y FROM w_data''')
    
    for row in cursor:
        results.append(list(row))
    return results

def retrieve_c_profile():
    results = []
    conn = sqlite3.connect(db_path)
    cursor = conn.execute('''SELECT section_name, H, B, 
                          t_w, t_f, A, weight, y_c, I_x, 
                          I_y, Z_x, Z_y FROM c_data''')
    
    for row in cursor:
        results.append(list(row))
    return results

def retrieve_l_profile():
    results = []
    conn = sqlite3.connect(db_path)
    cursor = conn.execute("SELECT section_name, H, B, t, r, r_end, A, weight, e, w, v, I_x, I_y FROM l_data")
    
    for row in cursor:
        results.append(list(row))
    return results

def delete_by_name(table, section_name):
    conn = sqlite3.connect(db_path)
    conn.execute(f"DELETE from {table} WHERE section_name = ?", (section_name,))
    conn.commit()
    conn.close()

# Editting queries method
def edit_name(table, old_section_name, new_section_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Check if the new section name already exists in the table
    cursor.execute(f"SELECT * FROM {table} WHERE section_name = ?", (new_section_name,))
    result = cursor.fetchone()
    if result is not None:
        raise ValueError("The new section name already exists in the table")

    # Update the section name in the table
    cursor.execute(f"UPDATE {table} SET section_name = ? WHERE section_name = ? AND section_name != ?", (new_section_name, old_section_name, new_section_name))
    conn.commit()
    conn.close()


def edit_weight_by_name(table, section_name, weight):
    conn = sqlite3.connect(db_path)
    conn.execute(f"UPDATE {table} SET weight = ? WHERE section_name = ?", (weight,section_name))
    conn.commit()
    conn.close()

def edit_H_by_name(table, section_name, H):
    conn = sqlite3.connect(db_path)
    conn.execute(f"UPDATE {table} SET H = ? WHERE section_name = ?", (H,section_name))
    conn.commit()
    conn.close()

def edit_B_by_name(table, section_name, B):
    conn = sqlite3.connect(db_path)
    conn.execute(f"UPDATE {table} SET B = ? WHERE section_name = ?", (B, section_name))
    conn.commit()
    conn.close()

def edit_tw_by_name(table, section_name, t_w):
    conn = sqlite3.connect(db_path)
    conn.execute(f"UPDATE {table} SET t_w = ? WHERE section_name = ?", (t_w, section_name))
    conn.commit()
    conn.close()

def edit_tf_by_name(table, section_name, t_f):
    conn = sqlite3.connect(db_path)
    conn.execute(f"UPDATE {table} SET t_f = ? WHERE section_name = ?", (t_f, section_name))
    conn.commit() 
    conn.close()

def edit_r_by_name(table, section_name, r):
    conn = sqlite3.connect(db_path)
    conn.execute(f"UPDATE {table} SET r = ? WHERE section_name = ?", (r, section_name))
    conn.commit()
    conn.close()

def edit_A_by_name(table, section_name, A):
    conn = sqlite3.connect(db_path)
    conn.execute(f"UPDATE {table} SET A = ? WHERE section_name = ?", (A, section_name))
    conn.commit()
    conn.close()

def edit_Jx_by_name(table, section_name, J_x):
    conn = sqlite3.connect(db_path)
    conn.execute(f"UDPATE {table} SET J_x = ? WHERE section_name = ?", (J_x, section_name))
    conn.commit()
    conn.close()

def edit_Jy_by_name(table, section_name, J_y):
    conn = sqlite3.connect(db_path)
    conn.execute(f"UPDATE {table} SET J_y = ? WHERE section_name = ?", (J_y, section_name))
    conn.commit()
    conn.close()

def edit_Ix_by_name(table, section_name, I_x):
    conn = sqlite3.connect(db_path)
    conn.execute(f"UPDATE {table} SET I_x = ? WHERE section_name = ?", (I_x, section_name))
    conn.commit()
    conn.close()

def edit_Iy_by_name(table, section_name, I_y):
    conn = sqlite3.connect(db_path)
    conn.execute(f"UPDATE {table} SET I_y = ? WHERE section_name = ?", (I_y, section_name))
    conn.commit()
    conn.close()

def edit_Zx_by_name(table, section_name, Z_x):
    conn = sqlite3.connect(db_path)
    conn.execute(f"UPDATE {table} SET Z_x = ? WHERE section_name = ?", (Z_x, section_name))
    conn.commit()
    conn.close()
    
def edit_Zy_by_name(table, section_name, Z_y):
    conn = sqlite3.connect(db_path)
    conn.execute(f"UPDATE {table} SET Z_y = ? WHERE section_name = ?", (Z_y, section_name))
    conn.commit()
    conn.close()    

def edit_yc_by_name(table, section_name, y_c):
    conn = sqlite3.connect(db_path)
    conn.execute(f"UPDATE {table} SET y_c = ? WHERE section_name = ?", (y_c, section_name))
    conn.commit()
    conn.close()

def edit_e_by_name(table, section_name, e):
    conn = sqlite3.connect(db_path)
    conn.execute(f"UPDATE {table} SET e = ? WHERE section_name = ?", (e, section_name))
    conn.commit()
    conn.close()

def edit_w_by_name(table, section_name, w):
    conn = sqlite3.connect(db_path)
    conn.execute(f"UPDATE {table} SET w = ? WHERE section_name = ?", (w, section_name))
    conn.commit()
    conn.close()

def edit_v_by_name(table, section_name, v):
    conn = sqlite3.connect(db_path)
    conn.execute(f"UPDATE {table} SET v = ? WHERE section_name = ?", (v, section_name))
    conn.commit()
    conn.close()

def edit_t_by_name(table, section_name, t):
    conn = sqlite3.connect(db_path)
    conn.execute(f"UPDATE {table} SET t = ? WHERE section_name = ?", (t, section_name))
    conn.commit()
    conn.close()

def edit_rend_by_name(table, section_name, r_end):
    conn = sqlite3.connect(db_path)
    conn.execute(f"UPDATE {table} SET r_end = ? WHERE section_name = ?", (r_end, section_name))
    conn.commit()
    conn.close()

'''
#* This section would act as the safety control
'''
# Safety Method
def w_validate(values):
    is_valid = True
    values_invalid = []
    
    if len(values['-W_SECTION_NAME-']) == 0:
        values_invalid.append('Section Name')
        is_valid = False
    if len(values['-W_WEIGHT-']) == 0:
        values_invalid.append('Weight')
        is_valid = False
    if len(values['-W_HEIGHT-']) == 0:
        values_invalid.append('Height')
        is_valid = False
    if len(values['-W_WIDTH-']) == 0:
        values_invalid.append('Width')
        is_valid = False
    if len(values['-W_TF-']) == 0:
        values_invalid.append('Flange Thickness')
        is_valid = False
    if len(values['-W_TW-']) == 0:
        values_invalid.append('Web Thickness')
        is_valid = False
    if len(values['-W_R-']) == 0:
        values_invalid.append('Radius')
        is_valid = False
    if len(values['-W_A-']) == 0:
        values_invalid.append('Area')
        is_valid = False
    if len(values['-W_JX-']) == 0:
        values_invalid.append('X Inertia')
        is_valid = False
    if len(values['-W_JY-']) == 0:
        values_invalid.append('Y Inertia')
        is_valid = False
    if len(values['-W_IX-']) == 0:
        values_invalid.append('X - Gyration')
        is_valid = False
    if len(values['-W_IY-']) == 0:
        values_invalid.append('Y - Gyration')
        is_valid = False
    if len(values['-W_ZX-']) == 0:
        values_invalid.append('X - Modulii')
        is_valid = False
    if len(values['-W_ZY-']) == 0:
        values_invalid.append('Y - Modulii')
        is_valid = False
    
    result = {"is_valid": is_valid, "values_invalid" : values_invalid}
    return result

def l_validate(values):
    is_valid = True
    values_invalid = []
    
    if len(values['-L_SECTION_NAME-']) == 0:
        values_invalid.append('Section Name')
        is_valid = False
    if len(values['-L_HEIGHT-']) == 0:
        values_invalid.append('Height')
        is_valid = False
    if len(values['-L_WIDTH-']) == 0:
        values_invalid.append('Width')
        is_valid = False
    if len(values['-L_T-']) == 0:
        values_invalid.append('Thickness')
        is_valid = False
    if len(values['-L_R-']) == 0:
        values_invalid.append('Radius')
        is_valid = False
    if len(values['-L_R_END-']) == 0:
        values_invalid.append('End Radius')
        is_valid = False
    if len(values['-L_A-']) == 0:
        values_invalid.append('Area')
        is_valid = False
    if len(values['-L_WEIGHT-']) == 0:
        values_invalid.append('Weight')
        is_valid = False
    if len(values['-L_E-']) == 0:
        values_invalid.append('X Central Point')
        is_valid = False
    if len(values['-L_W-']) == 0:
        values_invalid.append('Central Point')
        is_valid = False
    if len(values['-L_V-']) == 0:
        values_invalid.append('Y Central Point')
        is_valid = False
    if len(values['-L_IX-']) == 0:
        values_invalid.append('X inertia')
        is_valid = False
    if len(values['-L_IY-']) == 0:
        values_invalid.append('Y inertia')
        is_valid = False
        
    result = {"is_valid": is_valid, "values_invalid" : values_invalid}
    return result

def c_validate(values):
    is_valid = True
    values_invalid = []
    
    if len(values['-C_SECTION_NAME-']) == 0:
        values_invalid.append('Section Name')
        is_valid = False
    if len(values['-C_HEIGHT-']) == 0:
        values_invalid.append('Height')
        is_valid = False
    if len(values['-C_WIDTH-']) == 0:
        values_invalid.append('Width')
        is_valid = False
    if len(values['-C_TW-']) == 0:
        values_invalid.append('Web Thickness')
        is_valid = False
    if len(values['-C_TF-']) == 0:
        values_invalid.append('Radius')
        is_valid = False
    if len(values['-C_A-']) == 0:
        values_invalid.append('Area')
        is_valid = False
    if len(values['-C_WEIGHT-']) == 0:
        values_invalid.append('Weight')
        is_valid = False  
    if len(values['-C_Y_C-']) == 0:
        values_invalid.append('Centroid')
        is_valid = False
    if len(values['-C_IX-']) == 0:
        values_invalid.append('X inertia')
        is_valid = False
    if len(values['-C_IY-']) == 0:
        values_invalid.append('Y inertia')
        is_valid = False
    if len(values['-C_ZX-']) == 0:
        values_invalid.append('X modulii')
        is_valid = False
    if len(values['-C_ZY-']) == 0:
        values_invalid.append('Y modulii')
        is_valid = False
    result = {"is_valid": is_valid, "values_invalid" : values_invalid}
    return result

def pop_error_msg(values_invalid):
    error_message = ''
    for i in values_invalid:
        error_message += (f'\nInvalid items: {i}')
    return error_message

'''
#* Update Table Method
#* 
'''

def w_update_table_data(window):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM w_data")
    data = cursor.fetchall()
    conn.close()
    window['-W_TABLE-'].update(values=data)

def l_update_table_data(window):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM l_data")
    data = cursor.fetchall()
    conn.close()
    window['-L_TABLE-'].update(values=data)
    
def c_update_table_data(window):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM c_data")
    data = cursor.fetchall()
    conn.close()
    window['-C_TABLE-'].update(values=data)       