import dearpygui.dearpygui as dpg
import os
import subprocess
import time
from sftp_client import SFTP_CLIENT


# create a viewport
vp = dpg.create_viewport(title="Desktop kit", width=900, height=630, clear_color=(186,227,228), x_pos=20, y_pos=10, resizable=False)
dpg.set_viewport_large_icon("heart.ico")
dpg.setup_dearpygui(viewport=vp)
dpg.show_viewport(viewport=vp)


# create font registry
with dpg.font_registry():
    regular_font = dpg.add_font('./font/Roboto-Regular.ttf', 16)
    bold_font = dpg.add_font('./font/Roboto-Bold.ttf', 21)
    score_font = dpg.add_font('./font/ARCADE.ttf', 25)
    play_font = dpg.add_font('./font/PressStart2P-vaV7.ttf', 18)


# create texture registry
with dpg.texture_registry():
    image_connection = dpg.load_image("./image/connection.png")
    conn_button = dpg.add_static_texture(image_connection[0],image_connection[1],image_connection[3])
    image_disconnection = dpg.load_image("./image/disconnect.png")
    disconn_button = dpg.add_static_texture(image_disconnection[0], image_disconnection[1], image_disconnection[3])
    image_upload = dpg.load_image("./image/upload.png")
    upload_bnt = dpg.add_static_texture(image_upload[0],image_upload[1],image_upload[3])
    image_download = dpg.load_image("./image/download.png")
    download_bnt = dpg.add_static_texture(image_download[0],image_download[1], image_download[3])
    image_primary_bg = dpg.load_image("./image/bg2.png")
    primary_bg = dpg.add_static_texture(image_primary_bg[0], image_primary_bg[1], image_primary_bg[3])


# create primary window theme
with dpg.theme() as primary_window_theme:
    dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (220,212,212,79), category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_Button, (188,107,107,201), category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 0, 0, category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize,1,10,category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_FrameRounding,4,category=dpg.mvThemeCat_Core)


# create SFTP window theme
with dpg.theme(id="sftp_window_theme"):
    dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (111, 170, 205, 255), category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_Button,(148, 169, 240, 84), category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered,(141, 219, 223, 202), category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (141, 219, 223, 202), category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_Separator,(51, 120, 189, 172), category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (235, 198, 241, 151),category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_Tab,(197, 196, 185, 227),category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_FrameBg,(117, 188, 225, 225), category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_ChildBorderSize, 0, category=dpg.mvThemeCat_Core)


#create connect host info theme
with dpg.theme() as host_info_theme:
    dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (235, 198, 241, 151), category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_FrameBg,(83, 80, 159, 99), category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_WindowMinSize,5,category=dpg.mvThemeCat_Core)

# create sftp window button theme
with dpg.theme(id="conn_btn_theme"):
    dpg.add_theme_color(dpg.mvThemeCol_Border, (111, 230, 205, 255), category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_FrameRounding,5,category=dpg.mvThemeCat_Core)

#primary window function
def jieqiu(sender, user_data):
    os.system("python ball_game.py")


# create primary window
with dpg.window() as primary_window:
    btn1 = dpg.add_button(label="Color picker", callback=lambda : dpg.configure_item("color_picker_window", show=True), width=85,height=25, pos=(20,10))
    dpg.set_item_font(btn1, regular_font)
    btn2 = dpg.add_button(label="FTP diaglog", id="ssh_connect_window", callback=lambda : dpg.configure_item(sftp_window, show=True), width=85,height=25, pos=(20,50))
    dpg.set_item_font(btn2, regular_font)
    btn3 = dpg.add_button(label="Tetris game", width=85,height=25, pos=(20,90))
    dpg.set_item_font(btn3, regular_font)
    btn4 = dpg.add_button(label="Ball game", width=85, height=25, pos=(20, 130), callback=jieqiu)
    dpg.set_item_font(btn4, regular_font)
    btn5 = dpg.add_button(label="Eyes window", width=85, height=25, pos=(20, 170), callback=lambda : dpg.configure_item(eyes_window, show=True))
    dpg.set_item_font(btn5, regular_font)
    dpg.draw_image(texture_id=primary_bg,pmin=(130,0),pmax=(915,630),color=(255, 255, 255, 255))




# color picker window and function
def get_color_value(sender, app_data):
    dpg.set_value("color_picker_text",str(tuple([int(i*255) for i in app_data])))

with dpg.window(id="color_picker_window", label="color picker", show=False, pos=(380,0)):
    dpg.add_color_picker(width=400, height=500, alpha_bar=True,callback=get_color_value)
    dpg.add_input_text(default_value="show picker value", width=400, id="color_picker_text")


# create SFTP window and function
files_str = None
def get_file_dialog(sender, app_data):
    print(app_data)
    global files_str
    files_str = " ".join(list(app_data["selections"].values()))
    if "files Selected" in app_data["file_name_buffer"]:
        dpg.set_value("select_file_combox_upload", app_data["file_name_buffer"] + ": " + list(app_data["selections"].keys())[0] + "...")
    else:
        if os.path.isfile(list(app_data["selections"].values())[0]):
            dpg.set_value("select_file_combox_upload", "file Selected: " + list(app_data["selections"].keys())[0])
        else:
            dpg.set_value("select_file_combox_upload", "directory Selected: " + list(app_data["selections"].keys())[0])
            dpg.set_value("select_file_combox_download", "directory Selected: " + list(app_data["selections"].keys())[0])


def get_file_value(sender, app_data):
    if app_data == "select files":
        dpg.configure_item("file_dialog", show=True)
    elif app_data == "select directory":
        dpg.configure_item("directory_dialog", show=True)


conn_flag = False
# connect remote host function
def connect_host(sender, user_data):
    global conn_flag
    if conn_flag is True:
        dpg.set_value(warning_text, "disconnect pre host")
        dpg.configure_item(warning_window, show=True)
    else:
        try:
            hostname = dpg.get_value(host_ip)
            username = dpg.get_value(host_user)
            passwd = dpg.get_value(host_pwd)
            global sftp_client
            sftp_client = SFTP_CLIENT(hostname=hostname, username=username, password=passwd)
            conn_flag = True
            dpg.configure_item(c1, fill = (164, 236, 31, 255))
            dpg.configure_item(c2, fill=(164, 236, 31, 255))
            dpg.configure_item(c3, fill=(164, 236, 31, 255))
        except Exception as e:
            dpg.set_value(warning_text, str(e).split("]")[-1])
            dpg.configure_item(warning_window, show=True)

# disconnect remote host function
def disconnect_host(sender, user_data):
    global conn_flag
    if conn_flag is True:
        sftp_client.client_close()
        conn_flag = False
        dpg.configure_item(c1, fill=(232, 88, 47, 255))
        dpg.configure_item(c2, fill=(232, 88, 47, 255))
        dpg.configure_item(c3, fill=(232, 88, 47, 255))
    else:
        dpg.set_value(warning_text, "Don't have any connect")
        dpg.configure_item(warning_window, show=True)
        print("there don't have any connect")

# sftp window upload file
def upload_files(sender, user_data):
    if conn_flag is True:
        if files_str is not None:
            tar_name = "temp_desk.tar"
            if os.path.isdir(files_str):
                # 上传文件夹
                os.chdir( os.path.split( os.path.realpath(files_str) )[0] )
                p10 = subprocess.Popen(f"tar -cf {tar_name} {os.path.split( os.path.realpath(files_str) )[1]}", shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                p10.communicate()
            else:
                # 上传文件
                os.chdir("C:\\Users\\503247565\\Desktop\\py_files\\dear_pygui\\temp_tar")
                for i in files_str.split(" "):
                    p0 = subprocess.Popen(f"xcopy {str(i)} {str(os.getcwd())} ", shell=True, stderr=subprocess.PIPE)
                    p0.communicate()
                tar_files = " ".join(os.listdir())

                p1 = subprocess.Popen(f"tar -cf {tar_name} {tar_files}", shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                p1.communicate()

            remote_dir = dpg.get_value("upload_remote_text")
            remote_path = remote_dir + "/" + tar_name

            try:
                sftp_client.up_file(tar_name, remote_path )
                sftp_client.exct_command(f"cd {remote_dir} ; tar -xf {tar_name}")
                sftp_client.exct_command(f"cd {remote_dir} ; rm -f {tar_name}")
            except Exception as e:
                dpg.set_value(warning_text, e)
                dpg.configure_item(warning_window, show=True)
            finally:
                p2 = subprocess.Popen("del /q *.* ", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                p2.communicate()
                os.chdir("C:\\Users\\503247565\\Desktop\\py_files\\dear_pygui")
        else:
            dpg.set_value(warning_text, "not have selected files")
            dpg.configure_item(warning_window, show=True)
    else:
        dpg.set_value(warning_text, "Don't have any connect")
        dpg.configure_item(warning_window, show=True)

def download_files(sender, app_data):
    if conn_flag:
        if files_str:
            print(files_str)
            try:
                remote_path = dpg.get_value("download_remote_text")
                local_path = files_str + "/" + remote_path.split("/")[-1]
                sftp_client.down_file(remote_path, local_file_path=local_path)
                print("successful download files")
            except Exception as e:
                dpg.set_value(warning_text, e)
                dpg.configure_item(warning_window, show=True)
        else:
            dpg.set_value(warning_text, "not have selected files")
            dpg.configure_item(warning_window, show=True)
    else:
        dpg.set_value(warning_text, "Don't have any connect")
        dpg.configure_item(warning_window, show=True)


with dpg.window(label="SFTP window", show=True, pos=(380, 0), width=480, height=500) as sftp_window:
    with dpg.window(label="warning message", show=False, width=200, height=50, pos=(560,30),no_resize=True ) as warning_window:
        warning_text = dpg.add_text(indent=20)
        dpg.add_button(label="close",indent=70 , callback=lambda : dpg.configure_item(warning_window, show=False))

    dpg.add_text(default_value="connect remote host",indent=100, id="host_title")
    dpg.set_item_font("host_title", score_font)
    dpg.add_separator(pos=(0,55))
    dpg.add_dummy(height=3)
    with dpg.child(width=250, height=110) as host_info:
        dpg.add_dummy(height=10)
        with dpg.group(horizontal=True, horizontal_spacing=20, indent=10):
            dpg.add_text(default_value=" Host IP        : ", id="host_text1")
            dpg.set_item_font("host_text1",regular_font)
            host_ip = dpg.add_input_text(default_value="10.189.130.", width=110,  indent=98)

        with dpg.group(horizontal=True, horizontal_spacing=20,indent=10):
            dpg.add_text(default_value=" User Name :", id="host_text2")
            dpg.set_item_font("host_text2", regular_font)
            dpg.add_same_line()
            host_user = dpg.add_input_text(default_value="sdc", width=110, indent=98)

        with dpg.group(horizontal=True, horizontal_spacing=20, indent=10, id="host_text3"):
            dpg.add_text(default_value=" Password   :", )
            dpg.set_item_font("host_text3", regular_font)
            dpg.add_same_line()
            host_pwd = dpg.add_input_text(default_value="geMRint@adw2", password=True, width=110, indent=98)
    dpg.add_dummy(height=10)

    dpg.add_image_button(label="connect", texture_id=conn_button,height=45, width=45, pos=(290, 80), id="conn_btn", callback=connect_host)
    dpg.add_image_button(label="disconnect", texture_id=disconn_button, height=45, width=45, pos=(380, 80), id="disconn_btn", callback=disconnect_host)
    dpg.add_text(default_value="connect status :", pos=(270,155))
    c1 = dpg.draw_circle(center=(390,138), radius=12, segments=8, color=(217, 215, 66, 241))
    c2 = dpg.draw_circle(center=(415, 138), radius=12, segments=8, color=(217, 215, 66, 241))
    c3 = dpg.draw_circle(center=(440, 138), radius=12, segments=8, color=(217, 215, 66, 241))

    dpg.draw_arrow(p1=(100, 380), p2=(100, 230), thickness=2, size=8, color=(117, 215, 196, 213))
    dpg.draw_arrow(p1=(130, 230), p2=(130, 380), thickness=2, size=8, color=(117, 215, 196, 213))
    dpg.draw_arrow(p1=(160, 380), p2=(160, 230), thickness=2, size=8, color=(117, 215, 196, 213))

    with dpg.tab_bar():
        with dpg.tab(label="upload files"):
            dpg.add_dummy(height=10)
            dpg.add_combo(label="localhost", items=["select files", "select directory"], callback=get_file_value,default_value="select file or directory", id="select_file_combox_upload", indent=10)
            dpg.add_input_text(label="remotehost", default_value="/export/home/sdc", indent=10, pos=(10,410), id="upload_remote_text")
            # dpg.add_combo(label="remotehost", items=["select remote directory"], default_value="/export/home/sdc", indent=10, pos=(10,410))
            dpg.add_image_button(label="upload",id="upload_btn",texture_id=upload_bnt, height=45, width=45, pos=(270, 290), callback=upload_files)
            dpg.add_text(default_value="upload", pos=(275,345))
        with dpg.tab(label="download files"):
            dpg.add_dummy(height=10)
            dpg.add_input_text(label="remotehost", default_value="input the remote file/dir path",indent=10, id="download_remote_text")
            dpg.add_combo(label="localhost", items=["select directory"], callback=get_file_value,
                          default_value="select directory", id="select_file_combox_download", indent=10,pos=(10,410))
            dpg.add_image_button(label="download", id="download_btn", texture_id=download_bnt, height=45, width=45,
                                 pos=(270, 290), callback=download_files)
            dpg.add_text(default_value="download", pos=(270, 345))

with dpg.file_dialog(label="file selector", show=False, id="file_dialog",directory_selector=False ,callback=get_file_dialog):
    dpg.add_file_extension(".*", color=(255, 255, 255, 255))
    dpg.add_file_extension(".py", color=(0,255,0,255))
    dpg.add_file_extension(".sh", color=(255,0,255,255))
    dpg.add_file_extension(".txt", color=(255,255,0,255))
with dpg.file_dialog(label="directory selector", show=False, id="directory_dialog",height=550, directory_selector=True, callback=get_file_dialog):
    pass

# 眼运动函数
def move_eyes(sender, app_data):
    pre_pos = None
    eye_left_center = [50,109]
    eye_right_center = [150,109]
    move_time = 200
    while move_time > 0:

        time.sleep(0.1)
        now_pos = dpg.get_mouse_pos()
        if pre_pos is None:
            pre_pos = now_pos
            continue

        delta = [now_pos[0] - pre_pos[0], now_pos[1] - pre_pos[1]]
        pre_pos = now_pos
        move_time -= 1
        eye_left_center = [eye_left_center[0] + delta[0], eye_left_center[1] + delta[1]]
        eye_right_center = [eye_right_center[0] + delta[0], eye_right_center[1] + delta[1]]
        # x_l = ((1 - (eye_left_center[1] + 109) * (eye_left_center[1] + 109) / 99 / 99 ) / 40 / 40) ** 0.5
        # y_l = ((1 - (eye_left_center[0] + 50) * (eye_left_center[0] + 50) / 40 / 40 ) / 99 / 99) ** 0.5
        # 左眼运动限制
        if eye_left_center[0] < 18:
            eye_left_center[0] = 18
        elif eye_left_center[0] > 72:
            eye_left_center[0] = 72
        if eye_left_center[1] < 18:
            eye_left_center[1] = 18
        elif eye_left_center[1] > 200:
            eye_left_center[1] = 200
        # 右眼运动轨迹限制
        if eye_right_center[0] < 118:
            eye_right_center[0] = 118
        elif eye_right_center[0] > 182:
            eye_right_center[0] = 182
        if eye_right_center[1] < 18:
            eye_right_center[1] = 18
        elif eye_right_center[1] > 200:
            eye_right_center[1] = 200
        dpg.configure_item(eye_left_inside, center=eye_left_center)
        dpg.configure_item(eye_right_inside, center=eye_right_center)


# create eyes window
with dpg.window(show=False, width=220, height=250, pos=(130,0)) as eyes_window:
    eye_left_outside = dpg.draw_ellipse(pmin=(25, 54), pmax=(75, 164), fill=(255, 255, 255))
    dpg.draw_line(p1=(0, 0), p2=(0, 200), color=(255, 0, 0), thickness=2)
    dpg.draw_line(p1=(50,0), p2=(50, 218),color=(255,0,0), thickness=2)

    dpg.draw_line(p1=(0, 0), p2=(200, 0), color=(0, 255, 0), thickness=2)
    dpg.draw_line(p1=(0, 109), p2=(200, 109), color=(0,255,0), thickness=2)
    eye_right_outside = dpg.draw_ellipse(pmin=(125, 54), pmax=(175, 164), fill=(255, 255, 255))
    eye_left_inside = dpg.draw_circle(center=(50, 109), radius=10, fill=(0,0,0))  #dpg.draw_ellipse(pmin=(25, 60), pmax=(35, 75), fill=(0,0,0))
    eye_right_inside = dpg.draw_circle(center=(150, 109), radius=10, fill=(0,0,0))   #dpg.draw_ellipse(pmin=(125, 60), pmax=(135, 75), fill=(0,0,0))

    eyes_button = dpg.add_button(label="move eyes", callback=move_eyes)
    dpg.add_text()
    # dpg.add_hover_handler()



dpg.set_item_theme(primary_window, primary_window_theme)
dpg.set_item_theme(sftp_window,"sftp_window_theme")
dpg.set_item_theme(host_info, host_info_theme)
dpg.set_item_theme("conn_btn", "conn_btn_theme")
dpg.set_item_theme("disconn_btn", "conn_btn_theme")
dpg.set_item_theme("upload_btn", "conn_btn_theme")
dpg.set_item_theme("download_btn", "conn_btn_theme")

dpg.set_primary_window(primary_window, True)

dpg.start_dearpygui()

