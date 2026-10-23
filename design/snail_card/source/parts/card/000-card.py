from build123d import import_svg
from io import StringIO
card_length = param("card_length", 120.0)
card_width = param("card_width", 73.5)
card_thickness = param("card_thickness", 2.5)
corner_radius = param("corner_radius", 6.0)
relief_height = param("relief_height", 0.8)
slot_length = param("slot_length", 18.0)
slot_width = param("slot_width", 6.0)
slot_y = param("slot_y", 52.0)
logo_width = param("logo_width", 34.0)
logo_y = param("logo_y", 37.0)
name_width = param("name_width", 59.0)
name_y = param("name_y", 22.0)
qr_width = param("qr_width", 52.0)
qr_y = param("qr_y", -20.0)
logo_recess_depth = param("logo_recess_depth", 0.6)
logo_recess_clearance = param("logo_recess_clearance", 0.2)
recess_floor_z = card_thickness - logo_recess_depth
connection_inventory = {"snail_logo_recess":"free:clearance_pocket","snail_lanyard_slot":"free:capsule_through_hole"}
assert set(connection_inventory) == {"snail_logo_recess","snail_lanyard_slot"}
assert 0 < 2*corner_radius < min(card_length,card_width)
assert 0 < slot_width < slot_length < card_width
assert 0 < logo_recess_depth < card_thickness
assert logo_recess_clearance > 0
base = extrude(RectangleRounded(card_width,card_length,corner_radius), amount=card_thickness)
# SlotOverall uses the full end-to-end 18 mm dimension, with 6 mm diameter end arcs.
slot_profile = SlotOverall(slot_length,slot_width)
slot = Pos(0,slot_y,0) * extrude(slot_profile,amount=card_thickness)
assert abs(slot.bounding_box().size.X-slot_length) < 0.00001
assert abs(slot.bounding_box().size.Y-slot_width) < 0.00001
assert slot.bounding_box().max.Y < card_length/2
base = base - slot
# uploaded_logo and snail_name_font: immutable vector outlines, embedded for portable builds.
logo_svg = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"2265\" height=\"889\" viewBox=\"0 0 2265 889\"><path id=\"logo_red\" fill=\"#ff2442\" d=\"M0,423 L0,462 L6,518 L14,555 L30,608 L42,639 L58,671 L84,711 L110,743 L150,782 L178,803 L214,825 L262,849 L303,865 L337,875 L391,885 L432,888 L1850,887 L1909,879 L1951,868 L1988,855 L2019,841 L2056,821 L2093,798 L2116,780 L2142,755 L2165,729 L2189,697 L2207,668 L2218,646 L2231,613 L2245,571 L2255,530 L2261,493 L2264,455 L2263,418 L2257,368 L2248,328 L2233,281 L2218,243 L2203,214 L2178,176 L2149,141 L2123,115 L2089,87 L2059,68 L2009,42 L1975,28 L1922,12 L1864,2 L1829,0 L534,0 L414,1 L350,10 L330,15 L328,17 L326,16 L274,34 L251,44 L202,70 L169,91 L147,109 L119,136 L98,160 L76,189 L60,214 L46,241 L34,270 L20,312 L11,346 L4,385 Z\"/><path id=\"logo_white_0\" fill=\"white\" fill-rule=\"evenodd\" d=\"M805,743 L828,749 L848,751 L989,750 L1049,632 L914,632 L893,629 L870,621 L852,652 Z\"/><path id=\"logo_white_1\" fill=\"white\" fill-rule=\"evenodd\" d=\"M661,279 L660,287 L680,524 L687,564 L698,604 L712,640 L729,672 L746,696 L775,627 L803,571 L806,568 L795,538 L791,513 L773,280 Z\"/><path id=\"logo_white_2\" fill=\"white\" fill-rule=\"evenodd\" d=\"M386,279 L267,278 L264,280 L244,521 L240,542 L230,566 L297,696 L319,665 L335,635 L347,605 L361,559 L367,517 L377,411 L383,325 L388,282 Z\"/><path id=\"logo_white_3\" fill=\"white\" fill-rule=\"evenodd\" d=\"M1145,160 L1145,278 L1221,278 L1223,280 L1223,631 L1109,632 L1049,750 L1458,751 L1459,633 L1340,631 L1340,282 L1342,279 L1418,279 L1419,160 Z\"/><path id=\"logo_white_4\" fill=\"white\" fill-rule=\"evenodd\" d=\"M1984,174 L1965,162 L1948,158 L1938,158 L1922,162 L1912,167 L1900,177 L1890,192 L1885,212 L1885,277 L1947,277 L1958,275 L1975,268 L1990,255 L2000,235 L2002,210 L1998,195 L1993,185 Z\"/><path id=\"logo_white_5\" fill=\"white\" fill-rule=\"evenodd\" d=\"M950,120 L848,329 L842,351 L842,364 L846,376 L855,386 L863,391 L882,396 L952,397 L893,514 L884,537 L882,549 L883,562 L890,576 L898,583 L906,587 L922,591 L1048,592 L1098,494 L1042,493 L1033,490 L1029,486 L1027,478 L1083,371 L1128,279 L1014,279 L1009,283 L1000,298 L995,297 L987,289 L986,284 L1067,121 Z\"/><path id=\"logo_white_6\" fill=\"white\" fill-rule=\"evenodd\" d=\"M580,120 L462,120 L462,650 L388,651 L389,665 L394,688 L399,703 L408,719 L419,731 L429,738 L444,745 L459,749 L476,751 L503,749 L524,743 L542,733 L558,718 L563,711 L572,693 L579,667 Z\"/><path id=\"logo_white_7\" fill=\"white\" fill-rule=\"evenodd\" d=\"M1497,160 L1496,278 L1570,278 L1573,280 L1573,377 L1571,379 L1459,379 L1458,491 L1573,493 L1573,751 L1690,751 L1690,522 L1691,494 L1693,492 L1852,492 L1870,499 L1879,509 L1885,528 L1884,649 L1771,650 L1772,666 L1779,688 L1792,710 L1809,727 L1835,742 L1855,748 L1877,751 L1913,749 L1941,741 L1965,727 L1981,711 L1989,699 L1997,682 L2001,666 L2001,469 L1995,448 L1987,432 L1976,417 L1955,399 L1936,389 L1916,382 L1900,379 L1866,378 L1864,376 L1864,281 L1862,262 L1854,231 L1840,207 L1826,193 L1811,182 L1792,172 L1778,167 L1743,160 L1693,159 L1691,153 L1691,120 L1574,119 L1573,158 L1571,160 Z M1692,278 L1737,278 L1747,283 L1750,287 L1753,297 L1753,375 L1750,379 L1693,379 L1691,377 Z\"/></svg>"
name_svg = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"7000\" height=\"1400\" viewBox=\"0 -1100 7000 1400\"><path id=\"char_0\" d=\"M564 -728H794V-618H564ZM280 -224C288 -194 297 -160 305 -126L267 -119V-272H388V-673H276V-847H174V-673H53V-224H143V-272H176V-103L29 -79L47 23L323 -34C328 -8 332 16 334 37L416 8C406 -63 382 -168 357 -250ZM143 -575H187V-369H143ZM256 -575H298V-369H256ZM421 -447V92H533V-90C555 -74 578 -53 591 -38C638 -86 670 -138 692 -192C729 -144 761 -93 777 -55L838 -108V-30C838 -18 833 -14 819 -13C804 -13 752 -12 707 -15C720 12 735 56 739 85C814 85 865 84 901 69C937 52 947 24 947 -29V-447H740L741 -490V-526H910V-820H455V-526H642V-492L641 -447ZM838 -143C812 -191 768 -248 724 -296L732 -345H838ZM533 -131V-345H631C618 -273 590 -198 533 -131Z\" fill=\"black\"/><path id=\"char_1\" d=\"M1450 -850V-681H1286C1301 -721 1313 -762 1324 -804L1199 -828C1168 -691 1107 -553 1028 -472C1059 -458 1118 -429 1143 -410C1177 -452 1208 -504 1237 -563H1450V-362H1044V-244H1450V89H1577V-244H1958V-362H1577V-563H1900V-681H1577V-850Z\" fill=\"black\"/><path id=\"char_2\" d=\"M2536 -406C2585 -333 2647 -234 2675 -173L2777 -235C2746 -294 2679 -390 2630 -459ZM2585 -849C2556 -730 2508 -609 2450 -523V-687H2295C2312 -729 2330 -781 2346 -831L2216 -850C2212 -802 2200 -737 2187 -687H2073V60H2182V-14H2450V-484C2477 -467 2511 -442 2528 -426C2559 -469 2589 -524 2616 -585H2831C2821 -231 2808 -80 2777 -48C2765 -34 2754 -31 2734 -31C2708 -31 2648 -31 2584 -37C2605 -4 2621 47 2623 80C2682 82 2743 83 2781 78C2822 71 2850 60 2877 22C2919 -31 2930 -191 2943 -641C2944 -655 2944 -695 2944 -695H2661C2676 -737 2690 -780 2701 -822ZM2182 -583H2342V-420H2182ZM2182 -119V-316H2342V-119Z\" fill=\"black\"/><path id=\"char_3\" d=\"M3481 -722C3536 -678 3602 -613 3630 -570L3714 -645C3683 -689 3614 -749 3559 -789ZM3444 -458C3502 -414 3573 -349 3604 -304L3686 -382C3652 -425 3579 -486 3521 -527ZM3363 -841C3280 -806 3154 -776 3040 -759C3053 -733 3068 -692 3072 -666C3108 -670 3147 -676 3185 -682V-568H3033V-457H3169C3133 -360 3076 -252 3020 -187C3039 -157 3065 -107 3076 -73C3115 -123 3153 -194 3185 -271V89H3301V-318C3325 -279 3349 -236 3362 -208L3431 -302C3412 -326 3329 -422 3301 -448V-457H3433V-568H3301V-705C3347 -716 3391 -729 3430 -743ZM3416 -205 3435 -91 3738 -144V88H3857V-164L3975 -185L3956 -298L3857 -281V-850H3738V-260Z\" fill=\"black\"/><path id=\"char_4\" d=\"M4601 -850V-707H4386V-596H4601V-476H4403V-368H4456L4425 -359C4463 -267 4510 -187 4569 -119C4498 -74 4417 -42 4328 -21C4351 5 4379 56 4392 87C4490 58 4579 18 4656 -36C4726 20 4809 62 4907 90C4924 60 4958 11 4984 -13C4894 -35 4816 -69 4751 -114C4836 -199 4900 -309 4938 -449L4861 -480L4841 -476H4720V-596H4945V-707H4720V-850ZM4542 -368H4787C4757 -299 4713 -240 4660 -190C4610 -241 4571 -301 4542 -368ZM4156 -850V-659H4040V-548H4156V-370C4108 -359 4064 -349 4027 -342L4058 -227L4156 -252V-44C4156 -29 4151 -24 4137 -24C4124 -24 4082 -24 4042 -25C4057 6 4072 54 4076 84C4147 84 4195 81 4229 63C4263 44 4274 15 4274 -43V-283L4381 -312L4366 -422L4274 -399V-548H4373V-659H4274V-850Z\" fill=\"black\"/><path id=\"char_5\" d=\"M5048 -192 5059 -88 5397 -112V-74C5397 45 5435 79 5573 79C5603 79 5739 79 5770 79C5882 79 5916 42 5931 -84C5898 -91 5849 -109 5823 -128C5816 -41 5807 -25 5760 -25C5727 -25 5612 -25 5586 -25C5529 -25 5519 -32 5519 -75V-120L5954 -151L5943 -252L5519 -224V-286L5877 -311L5867 -407L5519 -384V-436C5654 -445 5785 -459 5893 -479L5841 -579C5655 -545 5366 -525 5112 -519C5123 -493 5135 -450 5137 -420C5220 -421 5308 -424 5397 -428V-377L5096 -357L5106 -258L5397 -278V-215ZM5583 -858C5561 -792 5525 -727 5482 -675V-767H5265C5274 -787 5282 -808 5290 -828L5175 -858C5143 -765 5087 -670 5023 -610C5051 -595 5101 -563 5124 -544C5154 -577 5184 -620 5212 -667H5227C5252 -625 5276 -575 5286 -542L5389 -583C5381 -606 5366 -637 5348 -667H5475C5460 -650 5444 -634 5428 -620C5456 -604 5506 -571 5529 -551C5561 -582 5593 -622 5621 -667H5660C5681 -632 5701 -592 5709 -564L5813 -602C5807 -620 5795 -644 5781 -667H5952V-767H5675C5684 -787 5693 -807 5700 -828Z\" fill=\"black\"/><path id=\"char_6\" d=\"M6102 -760C6159 -709 6234 -635 6267 -588L6353 -673C6315 -718 6238 -787 6182 -834ZM6038 -543V-428H6184V-120C6184 -66 6155 -27 6133 -9C6152 9 6184 53 6195 78C6213 56 6245 29 6417 -96C6405 -119 6388 -169 6381 -201L6303 -147V-543ZM6413 -785V-666H6791V-462H6434V-91C6434 38 6476 73 6610 73C6638 73 6768 73 6798 73C6922 73 6957 24 6972 -149C6938 -158 6886 -178 6858 -199C6851 -65 6843 -42 6789 -42C6758 -42 6649 -42 6623 -42C6567 -42 6558 -49 6558 -92V-349H6791V-300H6912V-785Z\" fill=\"black\"/></svg>"
logo_shapes = import_svg(StringIO(logo_svg),align=None)
red_profile = Compound(children=[s for s in logo_shapes if s.label == "logo_red"])
white_profile = Compound(children=[s for s in logo_shapes if s.label.startswith("logo_white_")])
assert len(red_profile.faces()) == 1 and len(white_profile.faces()) == 8
logo_scale = logo_width/red_profile.bounding_box().size.X
red_profile = scale(red_profile,by=logo_scale)
white_profile = scale(white_profile,by=logo_scale)
logo_bb = red_profile.bounding_box()
profile_origin = Pos(-(logo_bb.min.X+logo_bb.max.X)/2,-(logo_bb.min.Y+logo_bb.max.Y)/2)
red_profile = profile_origin*red_profile
white_profile = profile_origin*white_profile
recess_profile = offset(red_profile,amount=logo_recess_clearance,kind=Kind.ARC)
pocket = Pos(0,logo_y,recess_floor_z)*extrude(recess_profile,amount=logo_recess_depth)
assert pocket.bounding_box().max.Y < slot.bounding_box().min.Y
base = base - pocket
name_profile = Compound(children=import_svg(StringIO(name_svg)))
name_profile = scale(name_profile,by=name_width/name_profile.bounding_box().size.X)
name_bb = name_profile.bounding_box()
name_profile = Pos(-(name_bb.min.X+name_bb.max.X)/2,name_y-(name_bb.min.Y+name_bb.max.Y)/2)*name_profile
name = Pos(0,0,card_thickness)*extrude(name_profile,amount=relief_height)
assert abs(name.bounding_box().size.X-name_width) < 0.00001
assert name.bounding_box().max.Y < pocket.bounding_box().min.Y
# snail_qr_payload: v3-Q matrix, generated and independently decoded using OpenCV.
qr_rows = ["11111110010100101001101111111","10000010101100010000101000001","10111010101000110010001011101","10111010010011110100101011101","10111010001110110101001011101","10000010001100001101001000001","11111110101010101010101111111","00000000000001010100100000000","01110110011110110010100000110","00110001111001001111110111101","01101011100011000110101110010","10111100111001000001100101001","10110010000100110100010100111","10000001000111000001001101101","01011111000110000011010111011","10110001110101110010001011001","10110110011100010111110011000","00010001100110001111100000100","10110110110111110010001101100","00100000101010100110011011100","01101011101001011111111111101","00000000111110100011100011011","11111110001110101101101010110","10000010110101111000100010000","10111010001001000110111111101","10111010110100111011000011001","10111010101011001110100100101","10000010100000110010100010010","11111110001101110011100100010"]
module_count = len(qr_rows)
module_pitch = qr_width/module_count
quiet_zone = 4*module_pitch
assert qr_width+2*quiet_zone < card_width
assert abs(qr_y)+qr_width/2+quiet_zone < card_length/2
assert name.bounding_box().min.Y > qr_y+qr_width/2+quiet_zone
features = [name]
for r,row in enumerate(qr_rows):
    c = 0
    while c < module_count:
        if row[c] == "0":
            c += 1
            continue
        end = c+1
        while end < module_count and row[end] == "1":
            end += 1
        x = -qr_width/2+(c+end)*module_pitch/2
        y = qr_y+qr_width/2-(r+0.5)*module_pitch
        features.append(Pos(x,y,card_thickness)*Box((end-c)*module_pitch,module_pitch,relief_height,align=(Align.CENTER,Align.CENTER,Align.MIN)))
        c = end
card = base.fuse(*features)
assert len(card.solids()) == 1
assert abs(card.bounding_box().size.X-card_width) < 0.00001
assert abs(card.bounding_box().size.Y-card_length) < 0.00001
assert abs(card.bounding_box().size.Z-card_thickness-relief_height) < 0.00001
card.color = srgb("#faf8f3")
for face in card.faces():
    bb = face.bounding_box()
    if bb.min.Z >= card_thickness-0.00001:
        face.color = srgb("#161616")
print("Card width, length, thickness, relief:",card_width,card_length,card_thickness,relief_height)
print("Slot overall dimensions:",slot.bounding_box().size.X,slot.bounding_box().size.Y)
print("Top web:",card_length/2-slot_y-slot_width/2)
print("QR pitch, quiet zone:",module_pitch,quiet_zone)
publish("card_body",card,"蜗牛挂绳卡",material="pla")
