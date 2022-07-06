import arcade#导入游戏库arcade

SCREEN_WIDTH=600
SCREEN_HEIGHT=600
SCREEN_TITLE="Happy Face Example"
arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)#窗口设置

arcade.set_background_color(arcade.color.WHITE)#背景颜色

arcade.start_render()#开始 渲染，render渲染
left=130
right=480
top=500
bottom=130
arcade.draw_lrtb_rectangle_filled(left,right,top,bottom,arcade.color.DARK_GOLDENROD)#棕色脸

start_x=130
start_y=500
end_x=480
height=300
arcade.draw_parabola_filled(start_x,start_y,end_x,height,arcade.color.BLACK)#黑色抛物线头发

x=370
y=350
radius=20
arcade.draw_circle_filled(x,y,radius,arcade.color.BLACK)#右眼

x=250
y=350
radius=20
arcade.draw_circle_filled(x,y,radius,arcade.color.BLACK)#左眼

x=300
y=280
width=120
heigh=100
start_angle=190
end_angle=350
arcade.draw_arc_outline(x,y,width,heigh,arcade.color.BLACK,start_angle,end_angle,10)#嘴嘴

arcade.finish_render()#游戏库.停止渲染()
arcade.run()



