from manim import *
from manim_slides import Slide
import numpy as np



class Introduction(Slide,MovingCameraScene,Scene):
    def SinxAndCosXVisualize(self):
        self.acc_time = 0
        def sceneUpdater(dt):
            self.acc_time += dt
        self.add_updater(sceneUpdater)

        outputScope2 = VGroup()
        plta = FunctionGraph( lambda x: 0, x_range=[-2,2], color=YELLOW )
        pltb = FunctionGraph( lambda x: 0, x_range=[-2,2], color=BLUE )
        def outputdater2(mobj):            
            plta.become(FunctionGraph( lambda x: +0.20*np.sin(5*(x + self.acc_time)), x_range=[-2,2], color=YELLOW ).move_to(mobj))
            pltb.become(FunctionGraph( lambda x: -1.5*np.sin(5*(x + self.acc_time)), x_range=[-2,2], color=BLUE ).move_to(mobj))
        outputScope2.add_updater(outputdater2)
        rect = Rectangle(color=WHITE,height=4,width=4,grid_xstep=.8,grid_ystep=4/6, stroke_width=3)
        for mobj in rect[1]:
            mobj.set(stroke_width=1)
        for mobj in rect[2]:
            mobj.set(stroke_width=1)
        outputScope2.add(rect)
        outputScope2.add(plta,pltb)  
        self.update_self(self.acc_time)
        return outputScope2
    def construct(self):
        sinxcos=self.SinxAndCosXVisualize()
        self.add(sinxcos)
        nhom6=Text("NHÓM 6")
        nhom6.next_to(sinxcos[0],DOWN,0.25)
        self.play(Write(nhom6),run_time=1)
        for _ in range(1):  # You can adjust the number of loops here
            self.start_loop()
            self.wait()
            self.end_loop()
            self.clear()
            self.start_loop()

class Introduction2(Slide):
    def construct(self):
        Title=Text("Một bài thuyết trình ngắn gọn về",font_size=52,color=BLUE)
        Title.to_edge(ORIGIN)
        self.play(Write(Title),run_time=1)
        PhepViTu=Text("PHÉP VỊ TỰ",stroke_width=1,color=YELLOW)
        PhepViTu.next_to(Title,DOWN,buff=0.25)
        print(PhepViTu.get_center())
        PhepViTu.shift(np.array([5.0,0,0])) 
        self.play(Write(PhepViTu),run_time=0.5)
        self.next_slide()

        posforPHEPVITU=Text("mimi")
        posforPHEPVITU.to_edge(ORIGIN)
        posforPHEPVITU.to_edge(UP)

        self.play(PhepViTu.animate.move_to(posforPHEPVITU),FadeOut(Title),rate_functions=smooth)
        modau=Text("MỞ ĐẦU").match_style(PhepViTu)
        modau.to_edge(UP)
        self.play(ReplacementTransform(PhepViTu,modau))
        

class BaiToanMoDau(Slide):
    def construct(self):
        modau=Text("MỞ ĐẦU",stroke_width=1,color=YELLOW)
        modau.to_edge(UP)
        self.add(modau)
        sq01=Rectangle(width=2,height=4,fill_opacity=1,fill_color=BLUE)
        self.play(DrawBorderThenFill(sq01))
        self.next_slide()
        sq02=Rectangle(width=1,height=2,fill_opacity=1,fill_color=YELLOW)
        grp=VGroup(sq01,sq02)
        sq02.next_to(sq01,RIGHT,buff=0.25)
        self.play(Create(sq02),grp.animate.arrange(RIGHT,buff=2))
        self.next_slide()
        dot_B_sq1=self.createDot(1,UP,sq01,"$B'$",WHITE)
        dot_A_sq1=self.createDot(2,UP,sq01,"$A'$",WHITE)
        dot_D_sq1=self.createDot(3,DOWN,sq01,"$D'$",WHITE)
        dot_C_sq1=self.createDot(4,DOWN,sq01,"$C'$",WHITE)
        gr=VGroup(dot_A_sq1[0],dot_B_sq1[0],dot_C_sq1[0],dot_D_sq1[0])
        gr1=VGroup(dot_A_sq1[1],dot_B_sq1[1],dot_C_sq1[1],dot_D_sq1[1])

        dot_B_sq2=self.createDot(1,UP,sq02,"$B$",WHITE)
        dot_A_sq2=self.createDot(2,UP,sq02,"$A$",WHITE)
        dot_D_sq2=self.createDot(3,DOWN,sq02,"$D$",WHITE)
        dot_C_sq2=self.createDot(4,DOWN,sq02,"$C$",WHITE)
      
        gr_2=VGroup(dot_A_sq2[0],dot_B_sq2[0],dot_C_sq2[0],dot_D_sq2[0])
        gr1_2=VGroup(dot_A_sq2[1],dot_B_sq2[1],dot_C_sq2[1],dot_D_sq2[1])
        self.play(Create(dot_A_sq1[0]), Create(dot_B_sq1[0]), Create(dot_C_sq1[0]), Create(dot_D_sq1[0]))
        self.play(Create(dot_A_sq2[0]), Create(dot_B_sq2[0]), Create(dot_C_sq2[0]), Create(dot_D_sq2[0]))
        self.play(Write(gr1))
        self.play(Write(gr1_2))
        self.next_slide()
        DECAUA=Text(f"Giải thích vì sao các đường thẳng AA’, BB’, CC’, DD’ cùng đi qua một điểm O?",font_size=25)
        DECAUA.to_corner(DOWN)
        self.play(Write(DECAUA))
        smaler=VGroup(gr,gr1,gr_2,gr1_2,grp,DECAUA)
        self.next_slide()
        oldsmallerpos=smaler.get_center()
        self.play(smaler.animate.scale(.5))
        self.play(smaler.animate.to_edge(LEFT))
        self.next_slide()
        
        chiachac=Line(UP,DOWN*2)
        self.play(Create(chiachac))


        intersection_point = self.calculateIntersection(dot_A_sq1[0].get_center(), dot_A_sq2[0].get_center(), dot_B_sq1[0].get_center(), dot_B_sq2[0].get_center())
        O=Dot(point=intersection_point)
        Otext=Tex("$O$")
        O.scale(.5)
        Otext.scale(.5)
        always_redraw(lambda:Otext.next_to(O,UP))
        self.play(Create(O),Write(Otext))
        AprimeOBprime=Polygon(dot_A_sq1[0].get_center(),O.get_center(),dot_B_sq1[0].get_center(),fill_opacity=0,color=WHITE)
        self.play(Create(AprimeOBprime))
        self.next_slide()
        #proofing
        #Xét tam giác OA'B' có AB // A'B'

        gr=VGroup(AprimeOBprime.copy(),dot_A_sq1[0].copy(),dot_A_sq1[1].copy(),dot_B_sq1[0].copy(),dot_B_sq1[1].copy(),dot_A_sq2[0].copy(),dot_A_sq2[1].copy(),dot_B_sq2[0].copy(),dot_B_sq2[1].copy(),O.copy(),Otext.copy())
        self.play(gr.animate.next_to(chiachac,RIGHT,buff=1))
        self.next_slide()
        l1=self.CreateLineBetweenPoints(gr[1],gr[3])
        l2=self.CreateLineBetweenPoints(gr[5],gr[7])

        g_l1l2=VGroup(l1,l2)
        self.play(g_l1l2.animate.set_color(RED),rate_functions=smooth)

        self.next_slide()
        self.play(FadeOut(gr),FadeOut(g_l1l2),run_time=1)
        thales = Tex(r"$$\frac{OA}{OA'}=\frac{OB}{OB'}=\frac{1}{2}$$", font_size=16)
        ketluan=Text(f"=> A,B lần lượt là trung điểm của A'O và B'O",font_size=16)
        
        loi_thoai=VGroup(Text("Xét tam giác OA'B',theo Thales, ta có:",font_size=16),thales,ketluan)
        loi_thoai.arrange(DOWN,0.25)
        loi_thoai.next_to(chiachac,RIGHT,0.25)
        y=loi_thoai.get_center()+UP
        self.play(Write(loi_thoai))
        self.play(loi_thoai.animate.move_to(loi_thoai.get_center() +UP))
        self.next_slide()
        DprimeOCprime=Polygon(dot_D_sq1[0].get_center(),O.get_center(),dot_C_sq1[0].get_center(),fill_opacity=0,color=WHITE)
        self.play(Create(DprimeOCprime))
        self.next_slide()
        q=["Gọi E là giao điểm của BC và OC’","Xét tam giác OB’C’, ta có:","B trung điểm OB’","BE//B’C’","=> E trung điểm 0C’=>BE=1/2B’C’","Mà B,C,E thẳng hàng BE=1/2B’C’, BC=1/2B’C’","C trùng với E => C trung điểm OC’"]
        loi_thoat2=VGroup()
        for te in q:
            loi_thoat2.add(Text(text=te,font_size=16))
        loi_thoat2.arrange(DOWN,0.25)
        loi_thoat2.next_to(loi_thoai.get_bottom(),DOWN,buff=0.25)
        self.play(Write(loi_thoat2))
        self.next_slide()
        q12=VGroup(loi_thoai,loi_thoat2)
        self.play(q12.animate.shift(UP))
        ketbai=Text("Chứng minh tương tự ta được D trung điểm OC’",font_size=16)
        ketbai.next_to(loi_thoat2.get_bottom(),DOWN,buff=0.25)
        self.play(Write(ketbai))
        self.next_slide()
        DECAUB = Text("Hãy tính các tỉ số OA/OA', OB/OB', OC/OC', OD/OD'",font_size=25)
        DECAUB.move_to(DECAUA)
        DECAUB.scale(.75)
        self.play(ReplacementTransform(DECAUA,DECAUB))
        loi_thoai.add(loi_thoat2)
        loi_thoai.add(ketbai)
        self.play(FadeOut(loi_thoai),FadeOut(loi_thoat2),FadeOut(ketbai))
        thalesq1 = Text(r"Vì A, B, C, D lần lượt là trung điểm của OA', OB', OC', OD' nên", font_size=16)
        thalesq1.next_to(chiachac,RIGHT,0.25)
        self.play(Write(thalesq1))
        kq = Tex(r"$$\frac{OA}{OA'}=\frac{OB}{OB'}=\frac{OC}{OC'}=\frac{1}{2}$$", font_size=16)
        kq.next_to(thalesq1,DOWN,buff=0.25)
        self.play(Write(kq))
        self.next_slide()
        self.play(FadeOut(chiachac),FadeOut(thalesq1),FadeOut(kq))
        smaler.add(O)
        smaler.add(Otext)
        smaler.add(AprimeOBprime)
        smaler.add(DprimeOCprime)
        self.play(smaler.animate.move_to(oldsmallerpos))
        self.play(smaler.animate.scale(1.5))
        DECAUC=Text(f"Dùng thước thẳng nối hai điểm tương ứng nào đó trên hai bức tranh,đường thẳng đó có đi qua O hay không?",font_size=18)
        DECAUC.move_to(DECAUB)
        self.play(ReplacementTransform(DECAUB,DECAUC))
        q=Dot(sq01.get_center())
        q1=Dot(sq02.get_center())
        gr111=VGroup(q,q1)
        self.play(Create(gr111))
        self.wait()
        l=always_redraw(lambda:Line(q.get_center(),O.get_center(),color=RED))
        self.play(Create(l))
    def calculateIntersection(self, point1, point2, point3, point4):
        x1, y1 = point1[0], point1[1]
        x2, y2 = point2[0], point2[1]
        x3, y3 = point3[0], point3[1]
        x4, y4 = point4[0], point4[1]

        intersection_x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        intersection_y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

        return np.array([intersection_x, intersection_y, 0])
    def CreateLineBetweenPoints(self,From,To):
        l=Line(From,To)
        self.add(l)
        return l
    
    
    def createDot(self,index,dir,sq,text,colorA,bufff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER):
        dot=always_redraw(lambda:Dot(sq.get_vertices()[index-1],color=colorA))
        texttt=Tex(text)
        always_redraw(lambda:texttt.next_to(dot,dir,buff=bufff))
        return [dot,texttt]

class DINHNGHIAVACHUY(Slide):
    def construct(self):
        modau=Text("ĐỊNH NGHĨA",stroke_width=1,color=YELLOW)
        modau.to_edge(UP)
        self.play(Write(modau))
        image=ImageMobject("./dinhnghia.png")
        image.scale(.5)
        image.to_edge(RIGHT,buff=1)
        self.play(FadeIn(image))
        self.wait()
        self.next_slide()
        self.play(image.animate.to_edge(LEFT,buff=1))
        self.wait()
        text_lines = [
            "Cho điểm O và số thực k khác 0.",
            "Phép biến hình biến mỗi điểm M thành điểm M'",
            "sao cho OM' = kOM được gọi là phép vị tự tâm O, tỉ số k,",
            "kí hiệu là V(O, k).",
            "Điểm O gọi là tâm vị tự k gọi là tỉ số vị tự."
        ]
        text_obj=VGroup()
        for tex in text_lines:
            text_obj.add(Text(text=tex,font_size=16))
        text_obj.arrange(DOWN, aligned_edge=RIGHT)
        text_obj.to_edge(RIGHT,buff=1)
        self.play(Write(text_obj))
        self.wait()
        self.next_slide()
        self.play(FadeOut(text_obj),FadeOut(image))
        tinh_chat_title=Text("TÍNH CHẤT").match_style(modau)
        tinh_chat_title.move_to(modau)
        self.play(ReplacementTransform(modau,tinh_chat_title))
        self.next_slide()
        tinh_chat_anh=ImageMobject("tinh_chat.png")
        tinh_chat_anh.scale(.75)
        self.play(FadeIn(tinh_chat_anh))
        self.next_slide()
        self.play(tinh_chat_anh.animate.to_edge(UP,buff=1.5))
        self.next_slide()
        loi_giai=Tex("$A) \overrightarrow{OM'}=k\overrightarrow{OM},\overrightarrow{ON'}=kON$")
        loi_giai.next_to(tinh_chat_anh,DOWN,buff=.25)
        self.play(Write(loi_giai))
        self.next_slide()
        loi_giai_b=Tex("B) $\overrightarrow{M'N'}=\overrightarrow{ON'}-\overrightarrow{OM'}=k(\overrightarrow{ON}-\overrightarrow{OM})=k\overrightarrow{MN}$",font_size=DEFAULT_FONT_SIZE-10)
        loi_giai_b.next_to(loi_giai,DOWN,buff=0.25)
        self.play(Write(loi_giai_b))
        self.next_slide()
        vg=VGroup(loi_giai,loi_giai_b)
        self.play(FadeOut(vg),FadeOut(tinh_chat_anh))
        tc_1=ImageMobject("tc_1.png")
        tc_1.scale(2)
        tc_1_tex=Text("Biến ba điểm thẳng hàng thành ba điểm thẳng hàng và bảo toàn thứ tự giữa các điểm ấy.",font_size=21)
        tc_1_tex.next_to(tc_1,DOWN,buff=0.25)
        self.play(FadeIn(tc_1),FadeIn(tc_1_tex))
        self.next_slide()
        self.play(FadeOut(tc_1,tc_1_tex))
        tc_1q=ImageMobject("tc_22.png")
        tc_1q.scale(2)
        tc_1q_tex=Text("Biến tam giác thành tam giác đồng dạng với nó, biến góc thành góc bằng nó.",font_size=21)
        tc_1q_tex.next_to(tc_1q,DOWN,buff=0.25)
        self.play(FadeIn(tc_1q),FadeIn(tc_1q_tex))
        self.next_slide()
        self.play(FadeOut(tc_1q,tc_1q_tex))
        tc_1_1=ImageMobject("tc3.png")
        tc_1_1.scale(2)
        tc_1_1_tex=Text("Biến đường tròn bán kính R thành đường tròn có bán kính |k|.R.",font_size=21)
        tc_1_1_tex.next_to(tc_1,DOWN,buff=0.25)
        self.play(FadeIn(tc_1_1),FadeIn(tc_1_1_tex))
        self.next_slide()
        self.play(FadeOut(tc_1_1),FadeOut(tc_1_1_tex))
        last=Text("Biến đường thẳng thành đường thẳng song song hoặc trùng với nó, biến tia thành tia, biến đoạn thẳng thành đoạn thẳng.",font_size=16)
        self.play(Write(last))
        self.next_slide()
        self.play(FadeOut(last))
    def CreateLineBetweenPoints(self,From,To):
        l=Line(From,To)
        self.add(l)
        return l
    def calculateIntersection(self, point1, point2, point3, point4):
        x1, y1 = point1[0], point1[1]
        x2, y2 = point2[0], point2[1]
        x3, y3 = point3[0], point3[1]
        x4, y4 = point4[0], point4[1]

        intersection_x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        intersection_y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

        return np.array([intersection_x, intersection_y, 0])


    def createDot(self,index,dir,sq,text,colorA,bufff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER):
        dot=always_redraw(lambda:Dot(sq.get_vertices()[index-1],color=colorA))
        texttt=Tex(text)
        always_redraw(lambda:texttt.next_to(dot,dir,buff=bufff))
        return [dot,texttt]

class ViDu(Slide):
    def construct(self):
        modau=Text("ĐỊNH NGHĨA",stroke_width=1,color=YELLOW)
        modau.to_edge(UP)
        self.add(modau)
        modau1=Text("VÍ DỤ",stroke_width=1,color=YELLOW)
        modau1.to_edge(UP)
        self.play(ReplacementTransform(modau,modau1))
        self.next_slide()
        db=Text("Cho hình thang ABCD có hai đáy AB và CD, CD = 2AB. Gọi O là giao của hai cạnh bên và I là giao của hai đường chéo.\nTìm ảnh của đoạn thẳng AB qua các phép vị tự V(O, 2), V(I, – 2).",font_size=16)
        self.play(Write(db))   
        self.play(db.animate.to_edge(UP,buff=1.5))
        hinhhoc=ImageMobject("hinhhoc.png").scale(1.25)         
        hinhhoc.next_to(db,DOWN,buff=.25)
        self.play(FadeIn(hinhhoc))
        self.next_slide()
        gg=Group(hinhhoc,db)
        self.play(hinhhoc.animate.scale(0.75))
        self.play(hinhhoc.animate.to_edge(RIGHT,buff=1))
        cm_1=Text("Xét hình tam giác ODC có AB//DC, ad định lý ta-let ta có:",font_size=16)
        cm_1.to_edge(LEFT,buff=0.25)
        self.play(Write(cm_1))
        self.play(cm_1.animate.shift(UP))
        formula = Tex(
            r"$\frac{AB}{CD}=\frac{OA}{OD}=\frac{OB}{OC}=\frac{1}{2}$",font_size=25  # Use MathTex for mathematical expressions
        )
        formula1 = Tex(
            r"$=> OD=2OA, OC=2OB$", font_size=25 # Use MathTex for mathematical expressions
        )



        formula.next_to(cm_1,DOWN,buff=0.25)
        formula1.next_to(formula,DOWN,buff=.25)
        self.play(Write(formula))
        self.play(Write(formula1))

        line1 = Text("Do đó, D và C tương ứng là ảnh của A và B qua phép vị tự V(O, 2) \nVậy đoạn thẳng DC là ảnh của đoạn thẳng AB qua phép vị tự V(O, 2)",font_size=16)
     
        # Position the lines
        line1.to_edge(LEFT)
        line1.shift(DOWN*0.5)
        line1.shift(LEFT*0.5)

        # Group the lines and display them
        text_group = VGroup(line1)
        self.play(Write(text_group))
        self.next_slide()
        te2=Text("Do AB // CD nên theo hệ quả của định lí Thales trong tam giác ICD ta có:",font_size=16)
        te2.next_to(line1,DOWN,buff=0.25)
        te2.shift(RIGHT*.2)
        self.play(Write(te2))
        self.next_slide()
        l = Tex(r"$$\frac{IA}{IC}=\frac{IB}{ID}=\frac{AB}{CD}=\frac{1}{2}$$",font_size=16)
        l1=Tex(r"$$=> \overrightarrow{IC} = -2\overrightarrow{IA}=-2\overrightarrow{IB}$$",font_size=16)

        l.next_to(formula,DOWN,buff=2)
        l1.next_to(l,DOWN,buff=.25)
        self.play(Write(l),Write(l1))
        self.next_slide()
        vg=VGroup(cm_1,formula,formula1,line1,te2,l,l1)
        self.play(vg.animate.shift(UP*0.5))
        te22=Text(f"D,C tương ứng là ảnh của A và B qua phép vị tự V(I, – 2). Vậy đoạn thẳng CD \nlà ảnh của đoạn thẳng AB qua phép vị tự V(I, – 2).",font_size=16)
        te22.next_to(l1,DOWN,buff=0.25)
        te22.to_edge(LEFT)
        te22.shift(LEFT*1.7)
        te22.shift(RIGHT*1.5)
        self.play(Write(te22))
        print(te22.get_center())

        
