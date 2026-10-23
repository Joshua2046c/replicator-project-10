# One continuous logo insert, modelled in a local frame and placed at the pocket floor.
p = part("card")
logo_red_height = param("logo_red_height", 1.0)
logo_letter_relief = param("logo_letter_relief", 0.8)
logo_white_height = logo_red_height+logo_letter_relief
assert 0 < logo_red_height < logo_white_height
red_total_thickness = p.logo_recess_depth+logo_red_height
red_body = extrude(p.red_profile,amount=red_total_thickness)
white_letters = Pos(0,0,red_total_thickness)*extrude(p.white_profile,amount=logo_white_height-logo_red_height)
logo = red_body.fuse(*white_letters.solids())
assert len(logo.solids()) == 1
assert abs(logo.volume-red_body.volume-white_letters.volume) < 0.00001
assert abs(logo.bounding_box().size.Z-(p.logo_recess_depth+logo_white_height)) < 0.00001
logo.color = srgb("#ff2442")
for face in logo.faces():
    bb=face.bounding_box()
    if bb.min.Z >= red_total_thickness-0.00001 and bb.max.Z > red_total_thickness+0.00001:
        face.color = srgb("#ffffff")
publish("joshua_logo",logo,"李山迎卡 Logo",material="pla")
