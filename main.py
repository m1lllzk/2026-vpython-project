261103
scaffold_floor = box(pos=vec(1, -5, 0), size=vec(7, 0.2, 3))
scaffold_body =  box(pos=vec(3, -1.5, 0), size=vec(0.3, 7, 0.3))
scaffold_body2 = box(pos=vec(1, 1.6, 0), size=vec(5, 0.3, 0.3))
scaffold_string = cylinder(pos=vec(0, 0.7, 0), axis=vec(0, 3, 0), size=vec(0.8, 0.2, 0.2))

sphere(pos = vec(0,0,0), color = vec(250/255,224/255,180/255), radius = 1)
sphere(pos = vec(-0.28,0.4,0.9), color = vec(0,0,0), radius = 0.07)
sphere(pos = vec(0.28,0.4,0.9), color = vec(0,0,0), radius = 0.07)
ellipsoid(pos=vec(0, 0.1,0.96), color = vec(250/255,175/255,192/255), length=0.5, height=0.4, width=0.14)
cone(pos=vec(0, -2.6, 0), color = vec(0/255,217/255,29/255), axis=vec(0, 1.5, 0), radius=1, size=vec(2.3, 2.7, 1.8))
ellipsoid(pos=vec(-0.5, -3, 0), length=1, height=2, width=1, size=vec(1, 2, 1))
ellipsoid(pos=vec(0.5, -3, 0), length=1, height=2, width=1, size=vec(1, 2, 1))

261105
# 처형대
s_floor = box(pos=vec(1, -5, 0), size=vec(7, 0.2, 3), color=vec(0.65, 0.65, 0.65))
s_body = box(pos=vec(3, -1.5, 0), size=vec(0.3, 7, 0.3), color=vec(0.55, 0.55, 0.55))
s_body2 = box(pos=vec(1, 1.6, 0), size=vec(5, 0.3, 0.3), color=vec(0.55, 0.55, 0.55))
s_string = cylinder(pos=vec(0, 0.7, 0), axis=vec(0, 3, 0), size=vec(0.8, 0.2, 0.2))
scaffold = compound( [s_floor],[s_body],[s_body2],[s_string]) 
# 행맨
head = sphere(pos=vec(0, 0, 0), color=vec(250/255, 224/255, 180/255), radius=0.85)
left_eye = sphere(pos=vec(-0.28, 0.15, 0.78), radius=0.07,color=vec(0, 0, 0))
right_eye = sphere(pos=vec(0.28, 0.15, 0.78), radius=0.07, color=vec(0, 0, 0))
mouth = ellipsoid(pos=vec(0, -0.22, 0.8),length=0.3, height=0.5, width=0.05, color=vec(0.8, 0.3, 0.35))
body = ellipsoid(pos=vec(0, -1.65, 0), length=1.5, height=1.8, width=0.8, color=vec(0.3, 0.85, 0.4))
left_leg = ellipsoid(pos=vec(-0.4, -2.7, 0), length=0.55, height=1.2, width=0.65, color=vec(0.25, 0.65, 0.95))
right_leg = ellipsoid(pos=vec(0.4, -2.7, 0), length=0.55, height=1.2, width=0.65, color=vec(0.25, 0.65, 0.95))
left_foot = sphere(pos=vec(-0.4, -3.35, 0.1), radius=0.3, color=vec(0.35, 0.25, 0.2))
right_foot = sphere(pos=vec(0.4, -3.35, 0.1), radius=0.3, color=vec(0.35, 0.25, 0.2))
left_arm = cylinder(pos=vec(-0.5, -1.2, 0), axis=vec(-0.8, -0.5, 0), radius=0.17, color=vec(0.3, 0.85, 0.4))
right_arm = cylinder(pos=vec(0.5, -1.2, 0), axis=vec(0.8, -0.5, 0), radius=0.17, color=vec(0.3, 0.85, 0.4))
left_hand = sphere(pos=vec(-1.45, -1.8, 0), radius=0.23, color=vec(250/255, 224/255, 180/255))
right_hand = sphere(pos=vec(1.45, -1.8, 0), radius=0.23, color=vec(250/255, 224/255, 180/255))

Hangman = [head, left_eye, right_eye, mouth, body, left_arm, right_arm, left_hand, right_hand, left_leg, right_leg, left_foot, right_foot]
           
for part in Hangman:
    part.visible = False
