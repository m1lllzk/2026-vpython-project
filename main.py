scaffold_floor = box(pos=vec(0, 0, 0), axis=vec(3, 0, 0), radius=0.5)
scaffold_body = box(pos=vec(3, 0, 0), axis=vec(1.5, 0, 0), radius=0.5)
scaffold_body2 = box(pos=vec(3, 0, 0), axis=vec(1.5, 0, 0), radius=0.5)
scaffold_string = box(pos=vec(1.5, 0, 0.6), radius=0.3)


scaffold_floor = box(pos=vec(1, -5, 0), size = vec(7,0.2,3))
scaffold_body = box(pos=vec(3, -1.5, 0), size = vec(0.3,7,0.3))
scaffold_body2 = box(pos=vec(1, 1.6, 0), size = vec(5,0.3,0.3))
scaffold_string = box(pos=vec(1.5, 0, 0.6), axis=vec(0, 1, 0), )

sphere(pos = vec(0,0,0), color = vec(250/255,224/255,180/255), radius = 1)
sphere(pos = vec(-0.28,0.4,0.9), color = vec(0,0,0), radius = 0.07)
sphere(pos = vec(0.28,0.4,0.9), color = vec(0,0,0), radius = 0.07)
ellipsoid(pos=vec(0, 0.1,0.96), color = vec(250/255,175/255,192/255), length=0.5, height=0.4, width=0.14)
cone(pos=vec(0, -2.6, 0), color = vec(0/255,217/255,29/255), axis=vec(0, 1.5, 0), radius=1, size=vec(2.3, 2.7, 1.8))
ellipsoid(pos=vec(-0.5, -3, 0), length=1, height=2, width=1, size=vec(1, 2, 1))
ellipsoid(pos=vec(0.5, -3, 0), length=1, height=2, width=1, size=vec(1, 2, 1))
